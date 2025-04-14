import socket
import os

if __name__ == '__main__':
    # Create a TCP socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Bind the server to all interfaces on port 9999
    server.bind(('0.0.0.0', 9999))

    # Start listening for incoming connections (up to 5 queued connections)
    server.listen(5)

    while True:
        # Accept a new client connection
        client, addr = server.accept()
        print(client.recv(1024).decode())  # Receive greeting message from client
        client.send((f'Hello From The Server ! {addr}').encode())  # Send greeting back

        while True:
            try:
                # Receive fixed-length file name (100 bytes)
                file_name = client.recv(100).decode().strip()
                print(f"File name: {file_name}")

                # Receive fixed-length file size (10 bytes)
                file_size = int(client.recv(10).decode())
                print(f"File size: {file_size}")

                # Receive the file data in chunks
                file_bytes = b""
                received_size = 0
                while received_size < file_size:
                    # Read up to 4096 bytes, but no more than remaining
                    data = client.recv(min(4096, file_size - received_size))
                    if not data:
                        raise ConnectionError  # Client disconnected unexpectedly
                    file_bytes += data
                    received_size += len(data)

                # Save the received frame to disk
                os.makedirs("screenshots_server", exist_ok=True)
                with open(f"screenshots_server/{file_name}", "wb") as f:
                    f.write(file_bytes)
                print(f"Frame '{file_name}' received and saved.")

            except ConnectionError:
                print("Client disconnected.")
                break