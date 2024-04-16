# Mutltithreading in Python-> it used to process multiple jobs in parallel. It is a way to achieve multitasking.

# Example without multithreading

import time
import threading

def calc_square(numbers):
    print("calculate square of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('square:', n*n)

def calc_cube(numbers):
    print("calculate cube of numbers")
    for n in numbers:
        time.sleep(0.2)
        print('cube:', n*n*n)

start_time = time.time()
numbers = [2, 3, 8, 9]
calc_square(numbers)
calc_cube(numbers)
end_time = time.time()

print("time taken:", end_time - start_time)


# Example with multithreading

start_time = time.time()
numbers = [2, 3, 8, 9]
t1 = threading.Thread(target=calc_square,args=(numbers,))
t2 = threading.Thread(target=calc_cube,args=(numbers,))

t1.start() # this will invoke calc_square function
t2.start() # this will invoke calc_cube function

t1.join() # this will wait until t1 is finished
t2.join() # this will wait until t2 is finished

end_time = time.time()
print("time taken:", end_time - start_time)
