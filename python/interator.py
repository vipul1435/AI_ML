# interator are in python are objects that can be iterated upon.
# An object which will return data, one element at a time.
# Technically speaking, Python iterator object must implement two special methods, __iter__() and __next__(), collectively called the iterator protocol.

# Example
class myList:
    def __init__(self):
       self.data = [1, 2, 3, 4, 5]
       self.index = -1;

    def __iter__(self):
        return self
    
    def __next__(self):
        self.index += 1
        if self.index == len(self.data):
            raise StopIteration
        return self.data[self.index]