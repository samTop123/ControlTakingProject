import server_screenshots
import keyboard_sending_server
import threading

if __name__ == "__main__":
    t1 = threading.Thread(target=server_screenshots.main, args=())
    t2 = threading.Thread(target=keyboard_sending_server.main, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done !")