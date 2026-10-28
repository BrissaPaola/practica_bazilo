import os
import json
import re
import subprocess
import sys
from http.server import SimpleHTTPRequestHandler, HTTPServer

INDEX_DIR = os.path.dirname(os.path.abspath(__file__))
PROGRAMAS = os.path.join(INDEX_DIR, "programas")
COMANDO = [sys.executable, "bazilio_etapa6.py", "programas/hello.bzl"]
PLANTILLA = '''### Un programa en Bazilio ###
Main |:
    <w> "Hello Bazilio"
    (:) {%s}
:|
'''

class Handler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Si entran a la raíz o a index.html, los mandamos a la carpeta Frontend
        if self.path in ("/", "/index.html"):
            self.path = "/Frontend/index.html"
        super().do_GET()

    def do_POST(self):
        if self.path != "/generar":
            self.send_error(404)
            return
        largo = int(self.headers.get("Content-Length", 0))
        datos = json.loads(self.rfile.read(largo))
        notas = datos.get("notas", "").strip()

        if not notas or re.search(r'[{}"]', notas):
            self.responder({"ok": False, "log": "Notas vacías o con caracteres no válidos."})
            return

        os.makedirs(PROGRAMAS, exist_ok=True)
        with open(os.path.join(PROGRAMAS, "hello.bzl"), "w", encoding="utf-8") as f:
            f.write(PLANTILLA % notas)

        r = subprocess.run(COMANDO, capture_output=True, text=True, cwd=INDEX_DIR)
        self.responder({"ok": r.returncode == 0, "log": (r.stdout + r.stderr).strip()})

    def responder(self, obj):
        cuerpo = json.dumps(obj).encode()
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.send_header("Content-Length", str(len(cuerpo)))
        self.end_headers()
        self.wfile.write(cuerpo)

if __name__ == '__main__':
    puerto = int(os.environ.get("PORT", 8000))
    print(f"\n✨ Servidor corriendo con éxito.")
    print(f"👉 Entra a la dirección: http://localhost:{puerto}\n")
    HTTPServer(("", puerto), Handler).serve_forever()
    