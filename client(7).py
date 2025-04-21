import socket
import threading

client = socket.socket()
client.connect(('localhost', 5555))

def listen():
    while True:
        try:
            msg = client.recv(1024).decode()
            if msg:
                print("Received:", msg)
        except:
            break

threading.Thread(target=listen, daemon=True).start()

while True:
    msg = input()
    if msg.lower() == 'exit':
        break
    client.send(msg.encode())

client.close()

