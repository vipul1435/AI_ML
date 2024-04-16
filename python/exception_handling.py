try:
    age = int(input("Enter your age: "))
    print("Your age is: ", age)
except Exception as e:
    print("Invalid input", e)


# raise exception like throw in javascript

try:
    age = int(input("Enter your age: "))
    if age < 18:
        raise ValueError("You are not allowed to enter")
    print("Your age is: ", age)
except ValueError as e:
    print("Invalid input", e)

# try except else
try:
    age = int(input("Enter your age: "))
except ValueError as e:
    print("Invalid input", e)
else:
    print("Program executed successfully")

# try except finally

try:
    age = int(input("Enter your age: "))
except ValueError as e:
    print("Invalid input", e)
finally:
    print("Program executed successfully")

# type of exception- ZeroDivisionError, ValueError, TypeError, FileNotFoundError, ModuleNotFoundError, ImportError, KeyboardInterrupt, MemoryError, RecursionError, IndentationError, TabError, SyntaxError, NameError, AttributeError, KeyError, IndexError, NotImplementedError, StopIteration, SystemExit, Exception