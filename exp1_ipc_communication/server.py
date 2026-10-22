import socket
 
HOST = '127.0.0.1'
PORT = 5000
 
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(1)
 
print("Server is waiting for connection...")
conn, addr = server.accept()
print("Connected by:", addr)
 
data = conn.recv(1024).decode()
numbers = list(map(int, data.split()))
result = sum(numbers)
 
message = f"Sum = {result}"
conn.send(message.encode())
 
conn.close()
server.close()

