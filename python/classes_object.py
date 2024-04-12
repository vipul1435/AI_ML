# Classes are the blueprint of objects. They define the properties and behaviors of objects.

class Student:

# class variable
    school = "ABC School"

#defaul constructor
    def __init__(self): # Self is a reference to the current instance of the class like in c++ this pointer
#self is the address of the current object
        print("This is a constructor")
    
# parameterized constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        print("School: ", self.school)

# creating object of the class
s1 = Student("John", 25)
s1.display()