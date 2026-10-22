import socket

client = socket.socket()
client.connect(("127.0.0.1", 5000))

while True:
    print("\n1. Message Passing")
    print("2. Ricart-Agrawala")
    print("3. Token Ring")
    print("4. Centralized Coordinator")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        msg = input("Enter message: ")
        client.send(("MSG:" + msg).encode())

    elif choice in ["2", "3", "4"]:
        pid = input("Enter process ID: ")

        if choice == "2":
            algorithm = "Ricart-Agrawala"
        elif choice == "3":
            algorithm = "Token Ring"
        else:
            algorithm = "Centralized Coordinator"

        client.send(f"CS:{algorithm}:{pid}".encode())

        response = client.recv(1024).decode()
        print("Server:", response)

    elif choice == "5":
        break

    else:
        print("Invalid choice")

client.close()