'''
Real world example : Multi processing for cpu bound task
Scenario: Factorial Calculation
espqcially for large numbers
inolve significant computational work , multiprocessing
can be used to distribute the workload across 
multiple CPU cores  , improving performance
'''

import time
import multiprocessing
import math
import sys

#increase the maximum number of digits for nteger conversion
sys.set_int_max_str_digits(100000)

#function to compuet the factorial

def compute_fact(number):
    print(f"Computing factorial of {number}")
    result=math.factorial(number)
    print(f"factorial of {number } is {result}")
    return result

if __name__=="__main__":
    numbers=[5000,6000,7000]
    start_time=time.time()

    #create a pool of worker processes
    with multiprocessing.Pool() as pool:
         results=pool.map(compute_fact,numbers)
    end_time=time.time()
    print(f"Results :{results}")
    print(f"Time taken {end_time -start_time} second")    

