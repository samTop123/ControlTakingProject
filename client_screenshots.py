import socket
import constants
import time
from PIL import ImageGrab
import os

UDP_IP = constants.SERVER_IP
UDP_PORT = constants.UDP_PORT
server_address = (UDP_IP, UDP_PORT)

print("UDP target IP: " + UDP_IP)
print("UDP target port: " + str(UDP_PORT))

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def main():
    count = 0

    while True:
        screenshot = ImageGrab.grab()
        screenshot.resize((800, 533))
        file_path = f"screenshots_client\\my_image{count}.jpg"
        screenshot.save(file_path, 'JPEG', quality=70)

        img_data = b""
        with open(f"screenshots_client\\my_image{count}.jpg", "rb") as f: 
            img_data = f.read()

        client.sendto(str(len(img_data)).encode(), server_address)
        chunk_size = 1024
        for i in range(0, len(img_data), chunk_size):
            chunk = img_data[i:i+chunk_size]
            client.sendto(chunk, server_address)

        count += 1
        time.sleep(0.15)
        try:
            os.remove(f"screenshots_client\\my_image{count-1}.jpg")
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()