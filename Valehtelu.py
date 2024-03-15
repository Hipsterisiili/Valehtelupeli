import http.server
import socketserver
import webbrowser
import signal
import sys

PORT = 8000

class MyHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.path = '/index.html'
        return http.server.SimpleHTTPRequestHandler.do_GET(self)

def cleanup(signum, frame):
    print("\nInterrupted. Cleaning up...")
    sys.exit(0)

def main():
    signal.signal(signal.SIGINT, cleanup)

    handler = MyHandler

    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print(f"Serving at port {PORT}")
        webbrowser.open(f"http://localhost:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
        finally:
            httpd.server_close()

if __name__ == "__main__":
    main()

