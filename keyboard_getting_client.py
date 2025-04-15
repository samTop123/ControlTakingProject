import socket
import keyboard
import win32api

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('0.0.0.0', 9999))

    client.send('hello From Client !'.encode())

    while True:
        try:
            data = client.recv(1).decode()
            print(data)
            if str(data) == "1":
                data = client.recv(1024).decode().strip()
                if data:
                    print(f"Executing: {data}")
                    keyboard.press_and_release(data)
        except:
            break