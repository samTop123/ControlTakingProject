import keyboard
import socket
import os

if __name__ == "__main__":
    count = 0

    # Create a TCP socket
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Get the IP address of the current machine (localhost for local test)
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    # Connect to the server
    client.connect((IPAddr, 9999))

    # Send greeting and receive response
    client.send('hello From Client !'.encode())
    print(client.recv(1024).decode())

    while True:
        keyboard.press(str(client.recv(1024).decode()))