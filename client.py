import keyboard
from PIL import ImageGrab
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

    while not keyboard.is_pressed('q'):
        # Capture a screenshot
        screenshot = ImageGrab.grab()
        file_path = f"screenshots_client\\my_image{count}.png"
        screenshot.save(file_path, 'PNG')
        count += 1

        try:
            # Get file name and size
            file_name = os.path.basename(file_path)
            file_size = os.path.getsize(file_path)

            # Send fixed-length file name (100 characters, padded with spaces)
            client.send(file_name.ljust(100).encode())

            # Send fixed-length file size (10 digits, padded with zeros)
            client.send(str(file_size).zfill(10).encode())

            # Send file content in chunks
            with open(file_path, "rb") as f:
                while True:
                    data = f.read(4096)
                    if not data:
                        break
                    client.sendall(data)

            print("Frame sent!")

        except ConnectionResetError:
            print("Connection closed by server.")
            break
