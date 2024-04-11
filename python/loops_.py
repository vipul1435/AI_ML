# Loops are used to iterate over a sequence (list, tuple, string) or other iterable objects.

# There are two types of loops in Python: for and while.

# for loop
# The for loop in Python is used to iterate over a sequence (list, tuple, string) or other iterable objects. Iterating over a sequence is called traversal.

# Syntax of for Loop

list = [1, 2, 3, 4, 5]
for i in list:
    print(i, end=" ") # avoid new line

# print(*list) # directly print list elements

# for loop with range
# The range() function is used to generate a sequence of numbers. It is commonly used in for loops.
# The prameter of range() function are start, stop and step. here start is optional and default value is 0 and step is optional and default value is 1. and stop is mandatory.
# Note that stop value is not included in the range.
for i in range(2,6,2):
    print(i, end=" ")



# While loop
# The while loop in Python is used to iterate over a block of code as long as the test expression (condition) is true.
# We generally use this loop when we don't know the number of times to iterate beforehand.

# Syntax of while Loop

# while condition:
#     # body of while -> statements inside while loop
# i = 1
# while i <= 5:
#     print(i)
#     i += 1
