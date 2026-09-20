import socket
import os

HOST = "0.0.0.0"
PORT = 4040
PAGE_DIR = "pages"

def load_page(path):
    # Convert URI path to a filename
    if path == "/":
        filename = "index.otxt"
    else:
        filename = path.lstrip("/") + ".otxt"

    full_path = os.path.join(PAGE_DIR, filename)

    if not os.path.exists(full_path):
        return None

    with open(full_path, "r", encoding="utf-8") as f:
        return f.read()

def handle_request(req):
    req = req.strip()

    if not req.startswith("orion://"):
        return "40 Invalid Request\r\n"

    # Extract path
    try:
        without_scheme = req[len("orion://"):]
        parts = without_scheme.split("/", 1)
        path = "/" if len(parts) == 1 else "/" + parts[1]
    except Exception:
        return "40 Invalid Request\r\n"

    # Load OTXT page
    body = load_page(path)
    if body is None:
        return "51 Not Found\r\n"

    return f"20 text/orion\r\n{body}"

def main():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(5)

    print(f"Orion Net server running on port {PORT}")

    while True:
        conn, addr = server.accept()
        data = conn.recv(1024)

        if not data:
            conn.close()
            continue

        response = handle_request(data.decode("utf-8"))
        conn.sendall(response.encode("utf-8"))
        conn.close()

if __name__ == "__main__":
    main()
