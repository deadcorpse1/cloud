"""RMI service for factorial, array mode, and simple bank operations."""

import json
import math
import socket
import threading
from collections import Counter

HOST = "127.0.0.1"
PORT = 6008
balance = 1000.0
balance_lock = threading.Lock()


def factorial(n):
    """Return n! for a non-negative integer."""
    if type(n) is not int or n < 0:
        raise ValueError("factorial expects a non-negative integer")
    return math.factorial(n)


def mode(values):
    """Return the most frequent item; ties use its first appearance."""
    if not isinstance(values, list) or not values:
        raise ValueError("mode expects a non-empty array")
    try:
        counts = Counter(values)
    except TypeError as error:
        raise ValueError("array elements must be simple hashable values") from error
    highest_count = max(counts.values())
    return next(value for value in values if counts[value] == highest_count)


def bank_amount(value):
    if isinstance(value, bool) or not isinstance(value, (int, float)):
        raise ValueError("amount must be a positive number")
    if not math.isfinite(value) or value <= 0:
        raise ValueError("amount must be a positive finite number")
    return float(value)


def invoke(method, args):
    global balance
    if not isinstance(args, list):
        raise ValueError("args must be an array")

    if method == "factorial" and len(args) == 1:
        return factorial(args[0])
    if method == "mode" and len(args) == 1:
        return mode(args[0])
    if method == "deposit" and len(args) == 1:
        amount = bank_amount(args[0])
        with balance_lock:
            balance += amount
            return {"balance": round(balance, 2)}
    if method == "withdraw" and len(args) == 1:
        amount = bank_amount(args[0])
        with balance_lock:
            if amount > balance:
                raise ValueError("insufficient funds")
            balance -= amount
            return {"balance": round(balance, 2)}
    if method == "get_balance" and not args:
        with balance_lock:
            return {"balance": round(balance, 2)}
    raise ValueError(f"unknown method or invalid arguments: {method}")


def handle_client(connection, address):
    with connection, connection.makefile("rwb") as stream:
        print(f"Client connected: {address}")
        for line in stream:
            try:
                request = json.loads(line.decode("utf-8"))
                result = invoke(request.get("method"), request.get("args"))
                response = {"ok": True, "result": result}
            except (json.JSONDecodeError, AttributeError, TypeError, ValueError) as error:
                response = {"ok": False, "error": str(error)}
            stream.write((json.dumps(response) + "\n").encode("utf-8"))
            stream.flush()


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        print(f"RMI server listening on {HOST}:{PORT}; starting bank balance is 1000.00")
        while True:
            connection, address = server.accept()
            threading.Thread(
                target=handle_client, args=(connection, address), daemon=True
            ).start()


if __name__ == "__main__":
    main()
