'''
Lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.
A lambda function is defined using the lambda keyword.
A lambda function can be take as an argument in another function.
it is stored in a variable.
'''

# Example 1

# lambda function to add two numbers
add = lambda a, b: a + b

print(add(2, 3)) # 5

# Example 2

# Lmabda function as an argument in another function

def myfunc(n):
    return lambda a: a * n

mydoubler = myfunc(2)
print(mydoubler(11)) # 22

list1 = [1, 2, 3, 4, 5]

#advance function

# map() function
# map() function returns a map object(which is an iterator) of the results after applying the given function to each item of a given iterable (list, tuple etc.)

mappped_list = list(map(lambda x: x**2, list1))

print(mappped_list) # [1, 4, 9, 16, 25]

# filter() function
# filter() function constructs an iterator from elements of an iterable for which a function returns true.

filtered_list = list(filter(lambda x: x % 2 == 0, list1))

print(filtered_list) # [2, 4]

# reduce() function
# reduce() function is defined in functools module.
# reduce() function is used to apply a particular function passed in its argument to all of the list elements mentioned in the sequence passed along.

from functools import reduce

reduced_list = reduce(lambda x, y: x + y, list1)

print(reduced_list) # 15