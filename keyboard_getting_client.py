import socket
import keyboard

if __name__ == "__main__":
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    hostname = socket.gethostname()
    IPAddr = socket.gethostbyname(hostname)

    client.connect((IPAddr, 9999))

    client.send('hello From Client !'.encode())
    # Not receiving any response in this version

    while True:
        data = client.recv(1024).decode().strip()
        if data:
            try:
                keyboard.press_and_release(data)
                print(f"Pressed: {data}")
            except:
                print(f"Invalid key: {data}")
