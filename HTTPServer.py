import http.server
import socketserver

PORT = 8080;
Handler = http.server.SimpleHTTPRequestHandler

Handler.extensions_map = {
    '.aac': 'audio/x-aac',
    '.mp4': 'video/mp4'
}

httpd = socketserver.TCPServer(("", PORT), Handler)

print("Serving at port", PORT)
httpd.serve_forever()
