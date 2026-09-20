import socket
import sys

def parse_uri(uri):
    if not uri.startswith("orion://"):
        raise ValueError("Not an Orion URI")

    without_scheme = uri[len("orion://"):]
    parts = without_scheme.split("/", 1)

    host = parts[0]
    path = "/" if len(parts) == 1 else "/" + parts[1]

    return host, 4040, path

def main():
    if len(sys.argv) != 2:
        print("Usage: python orion_client.py orion://host/path")
        return

    uri = sys.argv[1]
    host, port, path = parse_uri(uri)

    request_line = f"{uri}\r\n"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    s.sendall(request_line.encode("utf-8"))

    data = s.recv(4096).decode("utf-8")
    s.close()

    if "\r\n" in data:
        status_line, body = data.split("\r\n", 1)
    else:
        status_line = data
        body = ""

    print("Status:", status_line)
    print("Body:")
    print(body)

if __name__ == "__main__":
    main()
