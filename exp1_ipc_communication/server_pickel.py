import socket
import pickle

server = socket.socket()
server.bind(('127.0.0.1', 5001))
server.listen(1)

print("Server waiting...")
conn, addr = server.accept()
print("Client connected")

data = pickle.loads(conn.recv(4096))

name = data[0]
numbers = data[1]

print("Name:", name)
print("Numbers:", numbers)

total = sum(numbers)
response = f"Hello {name}, Sum = {total}"

conn.send(pickle.dumps(response))

conn.close()
server.close()