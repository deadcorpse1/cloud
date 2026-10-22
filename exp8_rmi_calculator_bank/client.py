"""Interactive client for the Experiment 8 RMI service."""

import json
import socket

HOST = "127.0.0.1"
PORT = 6008


def remote_call(method, *args):
    request = json.dumps({"method": method, "args": args}) + "\n"
    with socket.create_connection((HOST, PORT), timeout=5) as client:
        with client.makefile("rwb") as stream:
            stream.write(request.encode("utf-8"))
            stream.flush()
            response = json.loads(stream.readline().decode("utf-8"))
    if not response["ok"]:
        raise ValueError(response["error"])
    return response["result"]


def main():
    print("Remote operations: factorial, mode, deposit, withdraw, balance, quit")
    while True:
        choice = input("Operation: ").strip().lower()
        try:
            if choice == "quit":
                break
            if choice == "factorial":
                print("Result:", remote_call("factorial", int(input("n: "))))
            elif choice == "mode":
                values = [int(item) for item in input("Integers separated by spaces: ").split()]
                print("Mode:", remote_call("mode", values))
            elif choice in ("deposit", "withdraw"):
                amount = float(input("Amount: "))
                result = remote_call(choice, amount)
                print("Updated balance:", f"{result['balance']:.2f}")
            elif choice in ("balance", "get_balance"):
                result = remote_call("get_balance")
                print("Current balance:", f"{result['balance']:.2f}")
            else:
                print("Choose factorial, mode, deposit, withdraw, balance, or quit.")
        except (ValueError, OSError, KeyError) as error:
            print("Request failed:", error)


if __name__ == "__main__":
    main()
