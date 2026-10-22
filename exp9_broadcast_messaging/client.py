"""Connect to the broadcast server and send/receive chat messages."""

import socket
import threading

HOST = "127.0.0.1"
PORT = 6009


def receive_messages(connection):
    try:
        reader = connection.makefile("r", encoding="utf-8", newline="\n")
        for line in reader:
            print("\n" + line.rstrip("\r\n") + "\n> ", end="", flush=True)
        reader.close()
    except (ConnectionError, OSError, UnicodeDecodeError):
        pass


def main():
    name = input("Your name: ").strip() or "Anonymous"
    with socket.create_connection((HOST, PORT)) as connection:
        connection.sendall((name + "\n").encode("utf-8"))
        threading.Thread(
            target=receive_messages,
            args=(connection,),
            daemon=True,
        ).start()
        print("Type a message to broadcast, or /quit to leave.")
        try:
            while True:
                message = input("> ")
                connection.sendall((message + "\n").encode("utf-8"))
                if message == "/quit":
                    break
        except (BrokenPipeError, ConnectionResetError):
            print("The server disconnected.")


if __name__ == "__main__":
    main()
