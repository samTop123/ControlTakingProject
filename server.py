import win32api
import keyboard
import PIL
import socket
import threading
import os

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
    # AF_INET - creating sockets that use IPv4 addresses.
    # SOCK_STREAM - creating sockets by the TCP protocol (TCP provides reliable, connection-oriented communication between two devices)

    server.bind(('0.0.0.0', 9999)) # 9999 - port, '0.0.0.0' - makes it accessible from any network interface on the machine

    server.listen(5) # how many connections are allowed in the same time in the server

    while True:
        client, addr = server.accept() 
        # addr - address of the client
        # client - A new socket object that represents the connection with the client. The server uses this socket to send and receive data

        print(client.recv(1024).decode())  # Receive greeting from client
        client.send((f'Hello From The Server ! {addr}').encode())

        while True:
            try:
                # Receive file name
                file_name_data = b""
                while True:
                    part = client.recv(1)
                    if not part:
                        raise ConnectionError  # Client disconnected
                    if part == b'\n': break
                    file_name_data += part
                file_name = file_name_data.decode()
                print(f"File name: {file_name}")

                # Receive file size
                size_data = b""
                while True:
                    part = client.recv(1)
                    if not part:
                        raise ConnectionError
                    if part == b'\n': break
                    size_data += part
                file_size = int(size_data.decode())
                print(f"File size: {file_size}")

                # Receive file bytes
                file_bytes = b""
                received_size = 0
                while received_size < file_size:
                    data = client.recv(1024)
                    if not data:
                        raise ConnectionError
                    file_bytes += data
                    received_size += len(data)

                if received_size == file_size:
                    os.makedirs("screenshots_server", exist_ok=True)
                    with open(f"screenshots_server/{file_name}", "wb") as file:
                        file.write(file_bytes)
                    print(f"Frame '{file_name}' received and saved.")
                else:
                    print(f"Incomplete frame '{file_name}'")

            except ConnectionError:
                print("Client disconnected.")
                break

"""
Error that I should fix ! : 
Incomplete frame 'my_image38.png'
Traceback (most recent call last):
  File "D:\ProgrammingTeam\NetworkAndProtocols\ControlTakingProject\server.py", line 35, in <module>
    file_name = file_name_data.decode()
                ^^^^^^^^^^^^^^^^^^^^^^^
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xc1 in position 2: invalid start byte
"""