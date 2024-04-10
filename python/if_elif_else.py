name = input("Enter your name: ")
age = int(input("Enter your age: "))

if(age<18):
    print("Hello ", name, " Your age is ", age, " so are small")
    print("Better luck next time:")
elif(age>50):
    print("Hello ", name, " Your age is ", age, " so are old")
    print("Better luck next time:")
else:
    print("Hello",name,"Your age is",age,"so are perfect")
    print("Welcome:")