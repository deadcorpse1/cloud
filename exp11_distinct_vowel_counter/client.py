"""Send text to the server and display its distinct-vowel count."""

import json
import socket

HOST = "127.0.0.1"
PORT = 6011


def main():
    text = input("Enter text: ")
    request = json.dumps({"text": text}) + "\n"
    with socket.create_connection((HOST, PORT), timeout=5) as client:
        with client.makefile("rwb") as stream:
            stream.write(request.encode("utf-8"))
            stream.flush()
            response = json.loads(stream.readline().decode("utf-8"))
    if not response["ok"]:
        print("Server error:", response["error"])
        return
    vowels = ", ".join(response["vowels"]) or "none"
    print(f"Distinct vowels: {response['count']} ({vowels})")


if __name__ == "__main__":
    main()
