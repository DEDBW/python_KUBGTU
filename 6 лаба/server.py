import http.server
import socketserver
import os

PORT = 8000

class CGIHTTPRequestHandler(http.server.CGIHTTPRequestHandler):
    cgi_directories = ["/cgi-bin"]

if not os.path.exists("cgi-bin"):
    os.makedirs("cgi-bin")

if os.name != 'nt':
    os.chmod("cgi-bin/fitness_cgi.py", 0o755)

Handler = CGIHTTPRequestHandler

with http.server.HTTPServer(("", PORT), Handler) as httpd:
    print(f"CGI-сервер запущен на порту {PORT}")
    print("Для просмотра данных перейдите по адресу: http://localhost:8000/index.html")
    httpd.serve_forever()