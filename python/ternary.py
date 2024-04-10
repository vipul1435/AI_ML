# first type ternary use

number = int(input("Enter number: "))
print("Number is even") if number%2==0 else print("Number is odd")

# second type ternary use

result = ("Number is odd","Number is even")[number%2==0]
print(result)
