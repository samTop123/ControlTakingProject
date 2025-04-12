import win32api
import keyboard
from PIL import ImageGrab
import socket
import threading
import datetime
import os
import numpy as np

if __name__ == "__main__":
    count = 0

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    client.connect((IPAddr, 9999))

    client.send('hello From Client !'.encode())
    print(client.recv(1024).decode())

    while not keyboard.is_pressed('q'):
        screenshot = ImageGrab.grab()
        file_path = f"screenshots_client\\my_image{count}.png"
        screenshot.save(file_path, 'PNG')
        count += 1

        try:
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)

            client.send(f"{file_name}\n".encode())
            client.send(f"{file_size}\n".encode())

            with open(file_path, "rb") as file:
                while True:
                    data = file.read(1024)
                    if not data: break
                    client.sendall(data)

            print("Frame sent !")
        except ConnectionResetError:
            print("Connection closed by server.")
            break