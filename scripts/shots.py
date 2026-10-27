"""Captura de tela exata do site em vários tamanhos (Chrome headless via DevTools Protocol).
Uso e motivo: runbooks/capturar-telas.md.  Requer: python -m pip install websockets"""
import json, subprocess, time, base64, os, sys, tempfile, shutil, urllib.request
from websockets.sync.client import connect

CHROME = os.environ.get("CHROME", r"C:\Program Files\Google\Chrome\Application\chrome.exe")
OUT = os.environ.get("RCA_OUT", tempfile.gettempdir())
BASE = os.environ.get("RCA_URL", "http://localhost:8791/index.html")
PORT = 9333
# cada item: nome, largura, altura, celular(1/0), query, rolagem(px)[, expressão JS a imprimir]
JOBS = json.loads(sys.argv[1])

prof = tempfile.mkdtemp(prefix="rca-chrome-")
proc = subprocess.Popen([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                         f"--remote-debugging-port={PORT}", f"--user-data-dir={prof}",
                         "--no-first-run", "--no-default-browser-check", "about:blank"],
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    for _ in range(50):
        try:
            tabs = json.load(urllib.request.urlopen(f"http://127.0.0.1:{PORT}/json"))
            break
        except Exception:
            time.sleep(0.2)
    page = [t for t in tabs if t["type"] == "page"][0]
    ws = connect(page["webSocketDebuggerUrl"], max_size=None)
    seq = [0]

    def cmd(method, **params):
        seq[0] += 1
        ws.send(json.dumps({"id": seq[0], "method": method, "params": params}))
        while True:
            msg = json.loads(ws.recv())
            if msg.get("id") == seq[0]:
                return msg.get("result", {})

    cmd("Page.enable")
    if not os.environ.get("INTRO"):  # sem INTRO=1, a intro é pulada (sessionStorage já marcado)
        cmd("Page.addScriptToEvaluateOnNewDocument",
            source="try{sessionStorage.setItem('rca_intro_v1','1')}catch(e){}")
    for name, w, h, mobile, query, scroll, *ev in JOBS:
        cmd("Emulation.setDeviceMetricsOverride", width=w, height=h, deviceScaleFactor=1, mobile=bool(mobile))
        cmd("Page.navigate", url=f"{BASE}{query}")
        time.sleep(3.2)  # tempo real: imagens carregadas e transições de entrada terminadas
        if scroll:
            cmd("Runtime.evaluate", expression=f"window.scrollTo(0,{scroll})")
            time.sleep(1.2)
        if ev:
            r = cmd("Runtime.evaluate", expression=ev[0], returnByValue=True)
            print("eval", name, json.dumps(r.get("result", {}).get("value")))
        shot = cmd("Page.captureScreenshot", format="png")
        path = os.path.join(OUT, f"{name}.png")
        open(path, "wb").write(base64.b64decode(shot["data"]))
        print("ok", path)
    ws.close()
finally:
    proc.terminate()
    time.sleep(0.5)
    shutil.rmtree(prof, ignore_errors=True)
