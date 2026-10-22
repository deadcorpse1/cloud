"""Serialize a Python object and send it to the matching TCP server."""

import pickle
import socket
import struct

HOST = "127.0.0.1"
PORT = 6010


class StudentData:
    def __init__(self, name, numbers):
        self.name = name
        self.numbers = numbers


def receive_exact(connection, length):
    chunks = bytearray()
    while len(chunks) < length:
        chunk = connection.recv(length - len(chunks))
        if not chunk:
            raise ConnectionError("server closed the connection before sending the full object")
        chunks.extend(chunk)
    return bytes(chunks)


def send_object(connection, value):
    payload = pickle.dumps(value)
    connection.sendall(struct.pack("!I", len(payload)) + payload)


def receive_object(connection):
    size = struct.unpack("!I", receive_exact(connection, 4))[0]
    if size > 1_000_000:
        raise ValueError("serialized response exceeds the 1 MB demo limit")
    return pickle.loads(receive_exact(connection, size))


def main():
    name = input("Enter your name: ")
    numbers = list(map(int, input("Enter integers separated by spaces: ").split()))
    data = StudentData(name, numbers)
    with socket.create_connection((HOST, PORT), timeout=5) as client:
        send_object(client, data)
        print("Server response:", receive_object(client))


if __name__ == "__main__":
    main()
