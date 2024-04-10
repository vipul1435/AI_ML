dist = {
    "name":"Vipul",
    "age":23,
    "skills":{
        "python":5,
        "java":4,
        "c":3
    }
}

# accessing dictionary
print(dist["name"]) # Vipul

# accessing nested dictionary
print(dist["skills"]["python"]) # 5

# adding new key value pair
dist["city"] = "Delhi"

print(dist) # {'name': 'Vipul', 'age': 23, 'skills': {'python': 5, 'java': 4, 'c': 3}, 'city': 'Delhi'}

# removing key value pair
dist.pop("age")

# type casting dictionary to list

#this will return list of keys
print(list(dist.keys())) # ['name', 'skills', 'city']

#this will return list of values
print(list(dist.values())) # ['Vipul', {'python': 5, 'java': 4, 'c': 3}, 'Delhi']

#this will return list of key value pairs in tuple
print(list(dist.items())) # [('name', 'Vipul'), ('skills', {'python': 5, 'java': 4, 'c': 3}), ('city', 'Delhi')]

# get() function used to get value of key, if key is not present it returns None
print(dist.get("name")) # Vipul

#get() function is more useful when key is not present as compared to direct access as it will throw error
# dist["address"] # error -> not recommended  

#update() function used to update dictionary with new key value pairs

dist.update({"name":"Vipul Jain","age":23})
print(dist) # {'name': 'Vipul Jain', 'skills': {'python': 5, 'java': 4, 'c': 3}, 'city': 'Delhi', 'age': 23}

# clear() function used to remove all key value pairs from dictionary
dist.clear()

print(dist) # {}

# set is unordered collection of unique elements and is mutable but elements should be immutable
# set can not store list or dictionary as element as they are mutable

# set is created using {} brackets
set_dt = {1,2,3}

print(set_dt) # {1, 2, 3}

# declaring empty set

set_dt = set()

# adding element to set
set_dt.add(4)
set_dt.add((1,2,3))

# set_dt.add([1,2,3]) # error, list is mutable

#removing element from set

set_dt.remove(4)

#clearing set
set_dt.clear()

#pop() function used to remove random element from set

set_dt = {1,2,3,4,5}
set_dt.pop()
print(set_dt) # set()

# union() function used to get union of two sets
set1 = {1,2,3}
set2 = {3,4,5}

union_set = set1.union(set2) # union returns new set which is union of two sets
print(union_set) # {1, 2, 3, 4, 5}

# intersection() function used to get intersection of two sets
intersection_set = set1.intersection(set2) # intersection returns new set which is intersection of two sets

print(intersection_set) # {3}   

# both union and intersection functions does not change original sets

# difference() function used to get difference of two sets

difference_set = set1.difference(set2) # difference returns new set which is difference of two sets

print(difference_set) # {1, 2}