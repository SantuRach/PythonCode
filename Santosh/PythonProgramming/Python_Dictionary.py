'''









"""
################################# Python Dictionary #################################

Properties:
1. defined in curly basis
2. duplicate keys not allowed, but duplicate values are allowed
3. mutable
4. dict store data in key-value pair
5. Only immutable data type can be added as key (FITS SB)
6. indexing and slicing is not allowed

"""
print("_" * 50)
print(dir(dict))
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__',
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__',
# '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__',
# '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
# '__subclasshook__',
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem',setdefault',
# 'update', 'values']

dict1 = {'a': 123, 'b': 456, 'c': 789}

print(dict1, type(dict1))

# Extend a dict
print("_" * 50)
dict1['d'] = 321
print(dict1, type(dict1))

print("_" * 50)
dict1['e'] = 321
print(dict1)

# dict with duplicate key (latest value get overwrite)
print("_" * 50)
dict1 = {'a': 123, 'b': 456, 'a': 789}
print(dict1, type(dict1))  # {'a': 789, 'b': 456} <class 'dict'>

# immutable data type can be added as key (FITS SB)
print("_" * 50)
dict1 = {'a': 123, 'b': 456, 'c': 789}
dict1[20] = [4, 6, 7]
dict1[True] = 'Python Programming'
dict1[4.5] = 55
dict1[(1, 2, 3)] = {'Name': 'Rahul', 'age': 25}

print(dict1)
print(dict1[(1, 2, 3)])  # {'Name': 'Rahul', 'age': 25}
print(dict1[4.5])  # 55

################################# loop on dict #################################
print("_" * 50)
dict2 = {'Name': 'Santosh', 'Surname': 'Rachotimath', 'Age': 36, 'City': 'Bengaluru'}

# prints only keys
for data in dict2:
    print(data)

# prints only keys, values in tuple format
print("_" * 50)
for data in dict2.items():
    print(data, type(data))

# prints only keys, values in original format
print("_" * 50)
for i, j in dict2.items():
    print('Key :', i, 'Value :', j)

################################# Methods dict #################################
print("_" * 50)
print(dir(dict))
# ['__class__', '__class_getitem__', '__contains__', '__delattr__', '__delitem__', '__dir__',
# '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getstate__',
# '__gt__', '__hash__', '__init__', '__init_subclass__', '__ior__', '__iter__', '__le__',
# '__len__', '__lt__', '__ne__', '__new__', '__or__', '__reduce__', '__reduce_ex__', '__repr__',
# '__reversed__', '__ror__', '__setattr__', '__setitem__', '__sizeof__', '__str__',
# '__subclasshook__',
# 'clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem',setdefault',
# 'update', 'values']

#################### get method ####################
# Get value on the basis of key
print("_" * 50)
dict2 = {'Name': 'Santosh', 'Surname': 'Rachotimath', 'Age': 36, 'City': 'Bengaluru'}

print('My name is :', dict2.get('Name'))  # Santosh

#################### keys method ####################
# keys method will leist the keys in the dict
print("_" * 50)
dict2 = {'Name': 'Santosh', 'Surname': 'Rachotimath', 'Age': 36, 'City': 'Bengaluru'}
list1 = dict2.keys()
print('Keys in the dict2 are :', list1)  # dict_keys(['Name', 'Surname', 'Age', 'City'])
print('Keys in the dict2 are :', list(list1))  # ['Name', 'Surname', 'Age', 'City']

#################### Values method ####################
# Values method will list the values in the dict
print("_" * 50)
dict2 = {'Name': 'Santosh', 'Surname': 'Rachotimath', 'Age': 36, 'City': 'Bengaluru'}
print('Values in the dict2 are :', dict2.values())  # dict_values(['Santosh', 'Rachotimath', 36, 'Bengaluru'])
print('Values in the dict2 are :', list(dict2.values()))  # ['Santosh', 'Rachotimath', 36, 'Bengaluru']

#################### Update method ####################
# Update method - Updates one dict data to another
print("_" * 50)
dict1 = {'Name': 'Santosh', 'Surname': 'Rachotimath', 'Age': 36, 'City': 'Bengaluru'}
dict2 = {'DoB': '28-Aug-1989', 'Sex': 'M'}

dict1.update(dict2)

print(dict1)
print(dict2)

#################### Pop method ####################
# pop method - removes data from dict and return it
print("_" * 50)
dict1 = {'Name': 'Santosh', 'Surname': 'Rachotimath', 'Age': 36, 'City': 'Bengaluru'}
dict2 = {'DoB': '28-Aug-1989', 'Sex': 'M'}

val = dict1.pop('City')
print(val)  #Bengaluru

print('Updated dict : ', dict1)  # {'Name': 'Santosh', 'Surname': 'Rachotimath', 'Age': 36}

#################### Popitem method ####################
# pop method - removes data from dict and return last key value pair.

print("_" * 50)
dict1 = {'Name': 'Santosh', 'Surname': 'Rachotimath', 'Age': 36, 'City': 'Bengaluru'}
dict2 = {'DoB': '28-Aug-1989', 'Sex': 'M'}

val = dict1.popitem()
print(val)  #Bengaluru

print('Removed item : ', dict1)  # {'Name': 'Santosh', 'Surname': 'Rachotimath', 'Age': 36}

#################### clear method ####################
# Clear method - removes all data from dict. only content will be deleted

print("_" * 50)
dict1 = {'Name': 'Santosh', 'Surname': 'Rachotimath', 'Age': 36, 'City': 'Bengaluru'}
dict2 = {'DoB': '28-Aug-1989', 'Sex': 'M'}

dict1.clear()
print(dict1)  # {}

#################### delete function ####################
# delete method - removes dict permanently.
# Also to remove particular key-value pair.

print("_" * 50)
dict1 = {'Name': 'Santosh', 'Surname': 'Rachotimath', 'Age': 36, 'City': 'Bengaluru'}
dict2 = {'DoB': '28-Aug-1989', 'Sex': 'M'}

#del dict1
del dict1['Name']
print(dict1)

#################### Copy function ####################
# shallow copy : consider we have two lists list_a and list_b, if we will assign list_a to list_b
# then update the list_b, data. the changes done in list_b will reflect in list_a as well
# here new list is not created instead address location (reference) is shared

print("_" * 50)
dict1 = {'Name': 'Santosh', 'Surname': 'Rachotimath', 'Age': 36, 'City': 'Bengaluru'}

dict2 = dict1
dict1['DoB'] = '28-Aug-1989'
print(dict1, id(dict1))
print(dict2, id(dict2))

# Deep copy : consider we have two lists list_a and list_b, if we will assign list_a to list_b
# then update the list_b, data. the changes done in list_b will not reflect in list_a
# here new list is created. address location (reference) is new
print("_" * 50)
dict1 = {'Name': 'Santosh', 'Surname': 'Rachotimath', 'Age': 36, 'City': 'Bengaluru'}

dict2 = dict1.copy()
dict1['DoB'] = '28-Aug-1989'
print(dict1, id(dict1))
print(dict2, id(dict2))

#################### set default key method ####################
# set default key - This method sets the default 'value' for the key, if key is not available

print("_" * 50)
dict1 = {'Name': 'Santosh', 'Surname': 'Rachotimath', 'Age': 36, 'City': 'Bengaluru'}

result1 = dict1.setdefault('Name', 'Rahul')
print(result1)
print(dict1)  # {'Name': 'Santosh', 'Surname': 'Rachotimath', 'Age': 36, 'City': 'Bengaluru'}

result1 = dict1.setdefault('Sex', 'M')
print(result1)
print(dict1)  #{'Name': 'Santosh', 'Surname': 'Rachotimath', 'Age': 36, 'City': 'Bengaluru', 'Sex': 'M'}

#################### fromkey method ####################
# fromkey - This method sets the default 'value' for the key, if key is not available

print("_" * 50)
x = ('a', 'b', 'c', 'd')
y = (78, 77, 88.9, True)

result = dict.fromkeys(x, y)
print("x,y", result)

result2 = dict.fromkeys(x, y)
print("x,y", result2)

#################### Practice programs ####################

# write a python program to create a dictionary from given string.
# output = {'Hello' : 5, 'Good' : 4, 'Morning,' : 8, 'Hope' : 4, 'you' : 3, 'are' : 3...... }
print("_" * 50)
str1 = "Hello Good Morning, Hope you are enjoying learning python"

list1 = str1.split(" ")

list2 = []
for word in list1:
    list2.append(len(word))

dict1 = dict(zip(list1, list2))
print(dict1)

# write a python to store even data with square and odd data with cube in the dict.
print("_" * 50)
list1 = [4, 7, 2, 8, 1, 6, 9, 3]
result = {}

for val in list1:
    if val % 2 == 0:
        prod = val ** 2
        result[val] = prod
    else:
        prod = val ** 3
        result[val] = prod

print(result)
'''
#################### Exercise ####################
# program to swap tuples
print("_" * 25, '# Exercise 1', "_" * 25)
