str = "Hello World"

# accessing characters of string
print(str[0])
print(str[1])

# assiging new value to string

# str[0] = "h" # error, it is not allowed

# Accessing part of string

# Syntax: str[start:end] where start is inclusive and end is exclusive
print(str[0:5]) # Hello (0 to 4) 5 is not included
print(str[6:]) # World (6 to end)
print(str[:5]) # Hello (0 to 4)

# Negative indexing

# Negative indexing starts from -1 from end of string

print(str[-1]) # d
print(str[-5:]) # World

# stirng functions

# len() function used to get length of string
print(len(str)) # 11
# lower() function used to convert string to lower case
print(str.lower()) # hello world
# upper() function used to convert string to upper case
print(str.upper()) # HELLO WORLD
# strip() function used to remove white spaces from start and end of string

str = "  Hello World  "
str = str.strip()
print(str) # Hello World

# replace() function used to replace part of string with another string
str = "Hello World"
str = str.replace("World","Python")

print(str) # Hello Python

# endswith() function used to check if string ends with given string

str = "Hello World"
print(str.endswith("World")) # True

# startswith() function used to check if string starts with given string

print(str.startswith("Hello")) # True

# find() function used to find index of given string in string, it returns -1 if not found else first occurence index

print(str.find("World")) # 6

# count() function used to count number of occurences of given substring in string

print(str.count("o")) # 2

# split() function used to split string into list of strings based on given separator

str = "Hello,World"
res = str.split(",")
print(res) # ['Hello', 'World']
