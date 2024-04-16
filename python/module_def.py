'''
Lerts we are defining a module named module_def.py
we can use this module in other python files by importing it
'''

def add(a, b):
    return a + b

if __name__ == "__main__":
    print("The funtion is call from the same file")
else:
    print("The function is called from another file")