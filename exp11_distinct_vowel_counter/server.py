"""TCP server that counts distinct vowels in client-supplied text."""

import json
import socket

HOST = "127.0.0.1"
PORT = 6011
VOWELS = set("aeiou")


def count_distinct_vowels(text):
    return len({character.lower() for character in text if character.lower() in VOWELS})


def handle_client(connection, address):
    print("Connected by:", address)
    with connection, connection.makefile("rwb") as stream:
        for line in stream:
            try:
                request = json.loads(line.decode("utf-8"))
                text = request.get("text")
                if not isinstance(text, str):
                    raise ValueError("request must contain text as a string")
                response = {
                    "ok": True,
                    "count": count_distinct_vowels(text),
                    "vowels": sorted({c.lower() for c in text if c.lower() in VOWELS}),
                }
            except (json.JSONDecodeError, AttributeError, ValueError) as error:
                response = {"ok": False, "error": str(error)}
            stream.write((json.dumps(response) + "\n").encode("utf-8"))
            stream.flush()


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        print(f"Distinct-vowel server listening on {HOST}:{PORT}")
        while True:
            connection, address = server.accept()
            handle_client(connection, address)


if __name__ == "__main__":
    main()
