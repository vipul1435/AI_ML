# is vs == in Python
'''

is: is is used for reference comparison. In simple words, it checks if both the objects point to the same memory location or not.

==: == is used for value comparison. It checks if the values of the two operands are equal or not.

is: is reutrns True if both the operands are equal and immutable. If the operands are mutable, then it returns False.

Example:

a=10
b=10
print(a is b) # True
print(a==b) # True

a=[1,2,3]
b=[1,2,3]
print(a is b) # False
print(a==b) # True

a=(1,2,3)
b=(1,2,3)
print(a is b) # True
print(a==b) # True

here because of immutability of tuple, a is b returns True.

'''