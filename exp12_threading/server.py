import socket
import threading

clients = []
lock = threading.Lock()
cs_lock = threading.Lock()

def handle_client(conn):
    while True:
        try:
            msg = conn.recv(1024).decode()

            if not msg:
                break

            print("Received:", msg)

            if msg.startswith("MSG:"):
                with lock:
                    for c in clients:
                        if c != conn:
                            try:
                                c.send(msg[4:].encode())
                            except:
                                pass

            elif msg.startswith("CS:"):
                algorithm, pid = msg[3:].split(":")
                pid = int(pid)

                with cs_lock:
                    print(algorithm, "- Process", pid, "enters CS")
                    conn.send(b"GRANTED: Enter critical section")
                    print("Process", pid, "exits CS")

        except:
            break

    with lock:
        if conn in clients:
            clients.remove(conn)

    conn.close()

server = socket.socket()
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind(("127.0.0.1", 5000))
server.listen()

print("Server started. Waiting for clients...")

while True:
    conn, addr = server.accept()

    with lock:
        clients.append(conn)

    print("Connected:", addr)
    threading.Thread(target=handle_client, args=(conn,), daemon=True).start()