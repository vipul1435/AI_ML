list = [1,2,3]

#slicing the list

print(list[0:2]) # [1,2] start is inclusive and end is exclusive

print(list[1:]) # [2,3] start is inclusive and end is exclusive

print(list[:2]) # [1,2] start is inclusive and end is exclusive

# methods of list

# append() method used to add element at end of list

list.append(4)
print(list) # [1,2,3,4]

# insert() method used to add element at given index
# Syntax: list.insert(index,element)
list.insert(1,5) # [1,5,2,3,4]

#assending order
list.sort() # [1,2,3,4,5] 
#descending order
list.sort(reverse=True) # [5,4,3,2,1]

# reverse() method used to reverse the list
list.reverse() # [5,4,3,2,1]

# remove() method used to remove element from list, it removes first occurence of element

list.remove(3) # [5,4,2,1]

# pop() method used to remove element from list based on index, if index is not given it removes last element

list.pop(1) # [5,2,1]


# Tuple

# Tuple is immutable, once created can't be changed

# Tuple is created using () brackets
tup = (1,2,3) 

