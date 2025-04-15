import socket
import keyboard
import win32api
import win32con

def mouse_click(button, action):
    if button == 'left':
        if action == 'down':
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
        else:
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
    elif button == 'right':
        if action == 'down':
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
        else:
            win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)

def move_mouse(x, y):
    win32api.SetCursorPos((x, y))

if __name__ == '__main__':
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('SERVER_IP_HERE', 9999))  # Replace with server IP
    client.send("Hello from client!".encode())

    buffer = ""
    while True:
        try:
            data = client.recv(1024).decode()
            if not data:
                break

            buffer += data
            while '\n' in buffer:
                line, buffer = buffer.split('\n', 1)
                parts = line.strip().split('|')

                if not parts:
                    continue

                if parts[0] == 'MOUSE_MOVE':
                    x, y = int(parts[1]), int(parts[2])
                    move_mouse(x, y)
                elif parts[0] == 'MOUSE_CLICK':
                    mouse_click(parts[1], parts[2])
                elif parts[0] == 'KEY':
                    keyboard.press_and_release(parts[1])
        except Exception as e:
            print("[Error]", e)
            break
