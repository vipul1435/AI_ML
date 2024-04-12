# overing -> the process of redefining a method in a subclass

# operators & their dunder methods
# + -> __add__()
# - -> __sub__()
# * -> __mul__()
# / -> __truediv__()
# // -> __floordiv__()
# % -> __mod__()
# ** -> __pow__()
# < -> __lt__()
# <= -> __le__()
# == -> __eq__()
# != -> __ne__()
# > -> __gt__()

class Complex:
    def __init__(self,real, imag):
        self.real = real
        self.imag = imag
    
    def print(self):
        print(f"{self.real} + {self.imag}i")

    def __add__(self,num):
        return Complex(self.real + num.real, self.imag + num.imag)

num1 = Complex(2,3)
num2 = Complex(1,2)
result = num1 + num2
result.print()
