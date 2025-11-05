from http.server import SimpleHTTPRequestHandler, HTTPServer

HOST = "0.0.0.0"
PORT = 8000

server = HTTPServer((HOST, PORT), SimpleHTTPRequestHandler)
print(f"Servidor corriendo en http://{HOST}:{PORT}")
server.serve_forever()
