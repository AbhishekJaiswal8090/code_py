import multiprocessing
import time

def worker_function(num):
    print(f"Process {num} starting")
    time.sleep(2)
    print(f"Process {num} done")

if __name__ == "__main__":
    processes = []
    for i in range(4):  # Creating multiple processes
        process = multiprocessing.Process(target=worker_function, args=(i,))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    print("All processes completed!")