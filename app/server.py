from http.server import BaseHTTPRequestHandler, HTTPServer
import socket

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            pod_ip = socket.gethostbyname(socket.gethostname())
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(f"OK | pod_ip={pod_ip}\n".encode())
        else:
            self.send_response(404)
            self.end_headers()

if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8080), SimpleHandler)
    print("Server running on port 8080...")
    server.serve_forever()
