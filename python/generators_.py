# Generators in Python are iterators, but you can only iterate over them once. It’s because they do not store all the values in memory, they generate the values on the fly:

# you are generate a list of infinite numbers without storing them in memory. so we can say that generators are used to generate a sequence of numbers or values without storing them in memory.

# Example

def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

for i in fibonacci():
    if(i > 1000):
        break
    print(i , end = " ")

# Note - In python there is no max limit on value of integer. It depends on the system architecture.


# List Set ans dictionary comprehensions

# List comprehensions provide a concise way to create lists. Common applications are to make new lists where each element is the result of some operation applied to each member of another sequence or iterable, or to create a subsequence of those elements that satisfy a certain condition.

# Example

# Without list comprehension
squares = []
for i in range(10):
    squares.append(i**2)

print(squares)

# With list comprehension

squares = [i**2 for i in range(10)]

print(squares)


# it is same for set


# Zip function

# The purpose of zip() is to map the similar index of multiple containers so that they can be used just using as single entity.

# Example

name = ['Tom', 'Jerry', 'Spike']

age = [20, 21, 22]

zipped_data = zip(name, age)
for i in zipped_data:
    print(i)

# Now  convert the zipped data into dictionary

zipped_data = zip(name, age)
dictionary = dict(zipped_data) # convert the zipped data into dictionary-> dierct method i.e typecasting
print(dictionary)

distionary = {name:age for name,age in zipped_data}

print(dictionary)