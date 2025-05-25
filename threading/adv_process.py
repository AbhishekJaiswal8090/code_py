#multiprocessing with process pool ecxecutor

from concurrent.futures import ProcessPoolExecutor
import time

def square_num(number):
    time.sleep(2)
    return f"square {number * number}"

numbers=[1,2,3,4,5]

if __name__== '__main__':
    with ProcessPoolExecutor(max_workers=3) as executor:
        results =executor.map(square_num,numbers)

    for result in results:
        print(result)    
