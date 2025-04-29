import socket
import constants
from tkinter import *
from PIL import Image, ImageTk
from io import BytesIO
from win32api import GetSystemMetrics

SERVER_IP = constants.SERVER_IP
UDP_PORT = constants.UDP_PORT

def decode_image_from_mem(received_data) -> ImageTk.PhotoImage:
    # Decode image from memory
    image_stream = BytesIO(received_data)
    img = Image.open(image_stream)
    img = img.resize((GetSystemMetrics(0), int(GetSystemMetrics(1)*0.9)))
    tk_img = ImageTk.PhotoImage(img)

    return tk_img

def display_on_canvas(my_canvas, tk_img):
    my_canvas.image = tk_img
    my_canvas.create_image(0, 0, image=tk_img, anchor='nw')

def update(count, root, my_canvas, server):
    try:
        # Receive image size safely
        while True:
            size_data, addr = server.recvfrom(1024)
            try:
                img_size = int(size_data.decode())
                break  # Break if decoding works
            except:
                continue  # If we accidentally got binary data first

        # Receive image data (raw bytes only)
        received_data = b""
        while len(received_data) < img_size:
            data, _ = server.recvfrom(1024)
            received_data += data

        tk_img = decode_image_from_mem(received_data)

        display_on_canvas(my_canvas, tk_img)

    except Exception as e:
        print(f"Error loading image: {e}")

    root.after(112, lambda: update(count + 1, root, my_canvas, server))

def main():
    count = 0
    server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    server.bind((SERVER_IP, UDP_PORT))

    root = Tk()
    root.geometry("950x667")
    root.title("Screenshare")

    my_canvas = Canvas(root, width=950, height=667)
    my_canvas.pack(fill="both", expand=True)

    update(count, root, my_canvas, server)
    mainloop()

if __name__ == "__main__":
    main()