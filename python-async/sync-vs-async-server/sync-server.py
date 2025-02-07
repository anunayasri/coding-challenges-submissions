import time
from http.server import HTTPServer, SimpleHTTPRequestHandler


class SyncHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        # Simulate 10ms workload
        time.sleep(0.01)
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello from sync server!")


def run_sync_server():
    port = 9000
    server = HTTPServer(("0.0.0.0", port), SyncHandler)
    print(f"Starting sync server on port {port}...")
    server.serve_forever()


if __name__ == "__main__":
    run_sync_server()
