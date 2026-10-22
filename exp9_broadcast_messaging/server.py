"""Broadcast newline-delimited messages from any client to all clients."""

import socket
import threading

HOST = "127.0.0.1"
PORT = 6009
clients = set()
clients_lock = threading.Lock()
broadcast_lock = threading.Lock()


def broadcast(message):
    payload = (message + "\n").encode("utf-8")
    with broadcast_lock:
        with clients_lock:
            recipients = list(clients)
        for connection in recipients:
            try:
                connection.sendall(payload)
            except OSError:
                remove_client(connection)


def remove_client(connection):
    with clients_lock:
        clients.discard(connection)
    try:
        connection.close()
    except OSError:
        pass


def handle_client(connection, address):
    reader = connection.makefile("r", encoding="utf-8", newline="\n")
    name = f"{address[0]}:{address[1]}"
    try:
        name = reader.readline().strip() or name
        broadcast(f"[server] {name} joined")
        for line in reader:
            message = line.rstrip("\r\n")
            if message == "/quit":
                break
            if message:
                print(f"{name}: {message}")
                broadcast(f"{name}: {message}")
    except (ConnectionError, OSError, UnicodeDecodeError):
        pass
    finally:
        reader.close()
        remove_client(connection)
        broadcast(f"[server] {name} left")


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        print(f"Broadcast server listening on {HOST}:{PORT}")
        print("Start clients in separate terminals. Press Ctrl+C to stop the server.")
        try:
            while True:
                connection, address = server.accept()
                with clients_lock:
                    clients.add(connection)
                threading.Thread(
                    target=handle_client,
                    args=(connection, address),
                    daemon=True,
                ).start()
        except KeyboardInterrupt:
            print("\nStopping broadcast server...")
        finally:
            with clients_lock:
                active_clients = list(clients)
                clients.clear()
            for connection in active_clients:
                connection.close()


if __name__ == "__main__":
    main()
