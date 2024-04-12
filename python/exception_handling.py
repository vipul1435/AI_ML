try:
    age = int(input("Enter your age: "))
    print("Your age is: ", age)
except Exception as e:
    print("Invalid input", e)