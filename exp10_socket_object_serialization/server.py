"""Receive a pickled object over TCP and return a serialized result."""

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
            raise ConnectionError("client closed the connection before sending the full object")
        chunks.extend(chunk)
    return bytes(chunks)


def receive_object(connection):
    size = struct.unpack("!I", receive_exact(connection, 4))[0]
    if size > 1_000_000:
        raise ValueError("serialized object exceeds the 1 MB demo limit")
    return pickle.loads(receive_exact(connection, size))


def send_object(connection, value):
    payload = pickle.dumps(value)
    connection.sendall(struct.pack("!I", len(payload)) + payload)


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)
        print(f"Object serialization server listening on {HOST}:{PORT}")
        print("Waiting for one client...")
        connection, address = server.accept()
        with connection:
            print("Connected by:", address)
            try:
                received = receive_object(connection)
                if not isinstance(received, StudentData):
                    raise ValueError("expected a StudentData object")
                if not isinstance(received.name, str) or not isinstance(received.numbers, list):
                    raise ValueError("object must contain a text name and a list of numbers")
                if not all(type(number) is int for number in received.numbers):
                    raise ValueError("numbers must be integers")
                print("Received object:", received.name, received.numbers)
                response = f"Hello {received.name}, sum = {sum(received.numbers)}"
                send_object(connection, response)
            except (ConnectionError, ValueError, pickle.UnpicklingError) as error:
                print("Request failed:", error)


if __name__ == "__main__":
    main()
