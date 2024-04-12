class student:
     # class variable
    school = "ABC School"

    #defaul constructor
    def __init__(self): # Self is a reference to the current instance of the class like in c++ this pointer
        print("This is a constructor")

    # parameterized constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def marks(self, math, phy, chem):
        self.math = math
        self.phy = phy
        self.chem = chem
    
# static method- it is a method which is bound to the class and not the object of the class
# static method can not use the instance variable and they are common for all the instances of the class
# static method does not take self as a parameter
    @staticmethod #decorator
    def info():
        print("This is a student class")


# class method- it is a method which is bound to the class and not the object of the class
# class method can use the class variable and they are common for all the instances of the class
# class method take cls as a parameter

    @classmethod #decorator
    def changeSchool(cls, school):
        cls.school = school # changing the class variable

# Property decorator- it is used to define the getter, setter and deleter for the instance variable
# it is used to perform the operation on the instance variable -> they automatically regenerates the instance variable on the basis of the operation performed on the instance variable

    @property
    def percentage(self):
        return (self.math + self.phy + self.chem)/3
    
stu1 = student("Rahul", 20)
stu1.marks(100, 90, 80)
print(stu1.percentage)
print(student.school)
student.changeSchool("XYZ School")
print(student.school)
stu1.math = 50
print(stu1.percentage)