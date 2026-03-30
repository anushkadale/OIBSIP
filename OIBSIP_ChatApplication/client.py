import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect(("localhost", 12346))
print("Connected to server")

while True:

    message = input("You: ")

    client.send(message.encode())

    if message.lower() == "exit":
        break

    reply = client.recv(1024).decode()

    print("Server:", reply)

client.close()