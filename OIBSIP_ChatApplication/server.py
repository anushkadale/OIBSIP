import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(("localhost", 12346))
server.listen()

print("Server started. Waiting for connection...")

client, address = server.accept()

print("Connected with", address)

while True:

    message = client.recv(1024).decode()

    if message.lower() == "exit":
        print("Client disconnected")
        break

    print("Client:", message)

    reply = input("You: ")

    client.send(reply.encode())

server.close()