import socket
import pickle

client = socket.socket()
client.connect(('127.0.0.1', 5001))

name = input("Enter name: ")
numbers = list(map(int, input("Enter numbers: ").split()))

data = (name, numbers)
client.send(pickle.dumps(data))

response = pickle.loads(client.recv(4096))
print("Server Response:", response)

client.close()