import socket
import threading

clients = []

def handle_client(client):
    while True:
        try:
            msg = client.recv(1024).decode()
            if not msg: break
            for c in clients:
                if c != client:
                    c.send(msg.encode())
        except:
            break
    clients.remove(client)
    client.close()

server = socket.socket()
server.bind(('localhost', 5555))
server.listen()
print("Chat server started on port 5555...")

while True:
    client, addr = server.accept()
    print(f"New connection from {addr}")
    clients.append(client)
    threading.Thread(target=handle_client, args=(client,)).start()
