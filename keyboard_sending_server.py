import socket
import keyboard
import win32api
import win32con
import time
import threading

def send_key_event(client, event):
    if event.event_type == 'down':
        modifiers = []
        if keyboard.is_pressed('ctrl'):
            modifiers.append('ctrl')
        if keyboard.is_pressed('alt'):
            modifiers.append('alt')
        if keyboard.is_pressed('shift'):
            modifiers.append('shift')

        key = event.name
        if key not in modifiers:
            combo = '+'.join(modifiers + [key]) if modifiers else key
            try:
                client.send(f"KEY|{combo}\n".encode())
            except:
                print("Key send failed.")

def track_mouse(client):
    prev_pos = (0, 0)
    prev_left = prev_right = False

    while True:
        x, y = win32api.GetCursorPos()
        left = win32api.GetKeyState(win32con.VK_LBUTTON) < 0
        right = win32api.GetKeyState(win32con.VK_RBUTTON) < 0

        # Movement
        if (x, y) != prev_pos:
            client.send(f"MOUSE_MOVE|{x}|{y}\n".encode())
            prev_pos = (x, y)

        # Clicks
        if left != prev_left:
            action = 'down' if left else 'up'
            client.send(f"MOUSE_CLICK|left|{action}\n".encode())
            prev_left = left

        if right != prev_right:
            action = 'down' if right else 'up'
            client.send(f"MOUSE_CLICK|right|{action}\n".encode())
            prev_right = right

        time.sleep(0.001)

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(1)
    print("[*] Waiting for client...")
    client, addr = server.accept()
    print("[+] Connected:", addr)
    print(client.recv(1024).decode())  # Greeting

    threading.Thread(target=track_mouse, args=(client,), daemon=True).start()
    keyboard.hook(lambda e: send_key_event(client, e))
    keyboard.wait()
