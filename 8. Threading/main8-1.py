import threading
import time

def thread_1():
    while True:
        print("Thread1 action!")
        time.sleep(1.0)

t1 = threading.Thread(target=thread_1)
t1.daemon = True
t1.start()

while True:
    print("Main Action!")
    time.sleep(2.0)