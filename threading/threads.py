#multithreading in python
#when to use threading 
#I/O bound tasks

import threading
import time

def print_numbers():
    for i in range(5):
        time.sleep(2)
        print(f"Number:{i}")

def print_letter():
    for letter in "abcde":
        time.sleep(2)
        print(f"Letter {letter}")

# creating two threads (outside the functions)
t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letter)

t = time.time()
#starting the thread so the process goes on concurrently
t1.start()
t2.start()

#joining the thread so that multiple threads become single thraed 
t1.join()
t2.join()
finished_time = time.time() - t
print(finished_time)
