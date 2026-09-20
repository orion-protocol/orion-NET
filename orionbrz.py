import socket
import sys

def fetch(uri: str) -> tuple[str, str]:
    if not uri.startswith("orion://"):
        raise ValueError("Not an Orion URI")

    without_scheme = uri[len("orion://"):]
    parts = without_scheme.split("/", 1)
    host = parts[0]
    path = "/" if len(parts) == 1 else "/" + parts[1]

    request_line = f"{uri}\r\n"

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, 4040))
    s.sendall(request_line.encode("utf-8"))
    data = s.recv(8192).decode("utf-8")
    s.close()

    if "\r\n" in data:
        status_line, body = data.split("\r\n", 1)
    else:
        status_line = data
        body = ""

    return status_line, body

def render_otxt(body: str) -> list[str]:
    lines = body.splitlines()
    links = []
    print()
    print("──────────────── ORION PAGE ────────────────")
    for line in lines:
        if line.startswith("```"):
            # simple code block delimiter, just print a separator
            print("──────── CODE ────────")
            continue
        elif line.startswith("# "):
            print(line[2:].upper())
        elif line.startswith("## "):
            print("  " + line[3:])
        elif line.startswith("### "):
            print("    " + line[4:])
        elif line.startswith("* "):
            print("• " + line[2:])
        elif line.startswith("- "):
            print("• " + line[2:])
        elif line.startswith("=>"):
            parts = line[2:].strip().split(" ", 1)
            uri = parts[0]
            label = parts[1] if len(parts) > 1 else uri
            links.append(uri)
            print(f"[{len(links)}] {label}")
        else:
            print(line)
    print("────────────────────────────────────────────")
    return links

def main():
    if len(sys.argv) != 2:
        print("Usage: python orionbrz.py orion://host/path")
        return

    current_uri = sys.argv[1]
    history = []

    while True:
        status, body = fetch(current_uri)
        print(f"\nSTATUS: {status}")
        if not status.startswith("20 "):
            print("Non-success status, press q to quit or b to go back.")
            cmd = input("> ").strip()
            if cmd == "b" and history:
                current_uri = history.pop()
                continue
            elif cmd == "q":
                break
            else:
                continue

        links = render_otxt(body)
        print(f"Current Url: {current_uri}")
        print("Commands: number = follow link, b = back, q = quit")
        cmd = input("> ").strip()

        if cmd == "q":
            break
        elif cmd == "b":
            if history:
                current_uri = history.pop()
            else:
                print("No history.")
        else:
            try:
                idx = int(cmd)
                if 1 <= idx <= len(links):
                    history.append(current_uri)
                    current_uri = links[idx - 1]
                else:
                    print("Invalid link number.")
            except ValueError:
                print("Unknown command.")

if __name__ == "__main__":
    main()
