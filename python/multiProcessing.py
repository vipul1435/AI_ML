# Mutltiprocesing in Python-> it used to process multiple jobs in parallel. It is a way to achieve multitasking.

# Multiprocessing vs multi-threading

'''Multiprocessing is a technique of utilizing two or more processors in a computer to process data. It is similar to multitasking, but allows the execution of processes concurrently. It is a technique of executing multiple processes concurrently in a single processor machine.
Multithreading refers to the ability of a processor to execute multiple threads concurrently, where each thread runs a process. Multiprocessing refers to the ability of a system to run multiple processors in parallel, where each processor can run one or more threads.'''


# Example 1: Multiprocessing in Python
'''
import multiprocessing as mp

result = []

def square_list(mylist):
    global result
    for num in mylist:
        result.append(num*num)
    print("Result inside the process:", result) # Result inside the process: [1, 4, 9, 16]

if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    p1 = mp.Process(target=square_list, args=(numbers,))

    p1.start()
    p1.join()

    print("Result outside the process:", result) # Result outside the process: []
'''


# As we can see that the result is empty outside the process. This is because the processes do not share memory. They have separate memory space. So, the changes made in the result list inside the process are not reflected outside the process.

# To solve this problem, we can use the array or Value from the multiprocessing module. These objects are shared between processes. So, the changes made in the result list inside the process will be reflected outside the process.

# Example

import multiprocessing as mp

def square_list(mylist,result,val):
    val.value = 5.35
    for idx, val in enumerate(mylist):
        result[idx] = val * val
    print("Result inside the process:",result[:])

if __name__ == "__main__":
    numbers = [1, 2, 3, 4]
    result = mp.Array('i',4) # shared array
    val = mp.Value('d',0.0) # shared value
    p1 = mp.Process(target=square_list, args=(numbers,result,val))

    p1.start()
    p1.join()

    print("Result outside the process:", result[:]) # Result outside the process: [1, 4, 9, 16]
    print("Value outside the process:", val.value) # Value outside the process: 5.35
