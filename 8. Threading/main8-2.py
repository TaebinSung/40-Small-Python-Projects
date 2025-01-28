import threading
import time

def sum(name, value):
    for i in range(0,value):
        print(f"{name} : {i}")
        time.sleep(0.5)

t1 = threading.Thread(target=sum, args=('thread 1', 10))
t2 = threading.Thread(target=sum, args=('thread 2', 10))

t1.start()
t2.start()

print("Main Thread")