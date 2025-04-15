import socket
import keyboard
import mouse

def on_key(event):
    if event.event_type == 'down':
        client.send("1".encode())
        modifiers = []
        if keyboard.is_pressed('ctrl'):
            modifiers.append('ctrl')
        if keyboard.is_pressed('alt'):
            modifiers.append('alt')
        if keyboard.is_pressed('shift'):
            modifiers.append('shift')

        # Don't include modifier key by itself (like 'ctrl' with no other key)
        if event.name not in modifiers:
            modifiers.append(event.name)
            combo = '+'.join(modifiers)
            try:
                client.send((combo + '\n').encode())
            except:
                pass

if __name__ == '__main__':
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('0.0.0.0', 9999))
    server.listen(1)
    client, addr = server.accept()

    print(client.recv(1024).decode())  # Receive greeting
    keyboard.hook(on_key)
    keyboard.wait()  # Keep running