#multi thrading with thread pool executor

from concurrent.futures import ThreadPoolExecutor
import time

def print_number(number):
    t = time.time()
    print(f"starts now {t}")
    time.sleep(2)
    return f"Number :{number}"

numbers =[1,2,3,4,5,6,7,8,9,10]


with ThreadPoolExecutor(max_workers=5) as executor:
    results=executor.map(print_number ,numbers)

for result in results:
    print(result)        

