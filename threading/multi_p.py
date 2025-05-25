import time 
import multiprocessing

def square_num():
    for i in range(5):
        time.sleep(2)
        print(f"square is {i*i}")

def cube_num():
    for i in range(5):
        time.sleep(2)
        print(f"Cube is {i*i*i}")

if __name__ == "__main__":
    # creating two processes
    p1 = multiprocessing.Process(target=square_num)
    p2 = multiprocessing.Process(target=cube_num)
    t = time.time()
    # start the processes
    p1.start()
    p2.start()
    # wait for process to complete
    p1.join()
    p2.join()
    finished_time = time.time() - t
    print(f"Total time taken: {finished_time}")