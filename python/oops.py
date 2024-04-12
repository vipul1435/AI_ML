# Abstraction -> Hiding the implementation details and showing only the necessary details of the object.
# Encapsulation -> Binding the data and the functions that manipulate the data in a single unit.
# Inheritance -> The mechanism of a deriving new class from an old one.
# Polymorphism -> The ability to take various forms.    

# del keyword is used to delete the object or variable of a class

# for make any variable or method private we use __ before the variable or method name

class Student:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def display(self):
        print("Name: ", self.__name)
        print("Age: ", self.__age)

    @staticmethod
    def __info():
        print("This is a student class")

# single inheritance
class Subject(Student):
    def __init__(self, name, age, subject):
        super().__init__(name, age) # calling the parent class constructor
        self.__subject = subject

    def display(self):
        super().display()
        print("Subject: ", self.__subject)