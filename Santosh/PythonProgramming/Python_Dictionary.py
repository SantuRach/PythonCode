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

#################### Exercise ####################

# program to add elements to the dictionary.
print("_" * 25, '# Exercise 1', "_" * 25)
dict1 = {}
dict1['a'] = 123
dict1['b'] = 456
dict1['c'] = 789
dict1['Name'] = 'Santosh'
dict1['Age'] = 36.5
dict1[123] = True
dict1[36.5] = 'Age'

print(dict1)

# program to print the square of all values in a dictionary.
print("_" * 25, '# Exercise 2', "_" * 25)
dict1 = {'a': 5, 'b':3, 'c': 6, 'd' : 8}

for key, val in dict1.items():
    print('Square of ', key,':', val**2)

# program to move items from dict1 to dict2.
print("_" * 25, '# Exercise 3', "_" * 25)
dict1 = {'a': 5, 'b':3, 'c': 6, 'd' : 8}
dict2 = {}
for key, val in dict1.items():
    dict2[key] = val

print(dict1)
print(dict2)

# program to concatenate two dictionaries.
print("_" * 25, '# Exercise 4', "_" * 25)
dict1 = {'Name': 'Santosh', 'Roll no': 2807 , 'Address': 'Bangalore'}
dict2 = {'Age' : 36, 'salary': '$25k'}

dict1.update(dict2)
print(dict1)

# program to get a list of odd and even keys from the dictionary.
print("_" * 25, '# Exercise 5', "_" * 25)
dict1 = {1: 25, 5:'abc', 8:'pqr', 21:'xyz', 12:'def', 2:'utv'}
dict1_Even = {}
dict1_Odd = {}

for val in dict1:
    if val % 2 == 0:
        dict1_Even[val] = dict1[val]
    else:
        dict1_Odd[val] = dict1[val]
print('Even :', dict1_Even)
print('Odd :', dict1_Odd)

# Program to create a dictionary from two lists.
print("_" * 25, '# Exercise 6', "_" * 25)
list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [12, 23, 24, 25, 15, 16]
dict1 = dict(zip(list1,list2))

print('dict from 2 lists :', dict1)

# Program to store squares of even and cubes of odd numbers
# in a dictionary using dictionary comprehension.
print("_" * 25, '# Exercise 7', "_" * 25)
list1 = [4, 5, 6, 2, 1, 7, 11, 3]
dict1 = {}

for val in list1:
    if val % 2 == 0:
        dict1[val]= val**2
    else:
        dict1[val] = val ** 3

print(dict1)

# program to clear all items from the dictionary.
print("_" * 25, '# Exercise 8', "_" * 25)
dict1 = {4: 16, 5: 125, 6: 36, 2: 4, 1: 1, 7: 343, 11: 1331, 3: 27}
print("Before : ", dict1)
dict1.clear()
print("Afetr : ", dict1)

# program to remove duplicate values from Dictionary.
print("_" * 25, '# Exercise 9', "_" * 25)
dict1 = {'a': 12, 'b': 2, 'c': 12, 'd': 5, 'e': 35, 'f': 5}
dict2 = {}
for key, val in dict1.items():
    if val not in dict2.values():
        dict2[key] = val

print(dict2)

# program to create a dictionary from the string.
print("_" * 25, '# Exercise 10', "_" * 25)
str1 = 'SQATools'
list1 = []
list2 = []

for char in str1:
    if char not in list1:
        list1.append(char)
        count = str1.count(char)
        list2.append(count)

dict2 = dict(zip(list1, list2))
print(dict2)

# Dictionary program to sort a dictionary using keys.
print("_" * 25, '# Exercise 11', "_" * 25)
dict1 = {'d' : 21, 'b' : 53,  'a': 13, 'c': 41}

# Dprogram to sort a dictionary in  python using values.
print("_" * 25, '# Exercise 12', "_" * 25)
dict1 = {'d' : 21, 'b' : 53,  'a': 13, 'c': 41}

# program to add a key in a dictionary.
print("_" * 25, '# Exercise 12', "_" * 25)
dict1 = Input = {'name':'yash', 'city': 'pune'}
dict2 = {}
for key, val in dict1.items():
    dict2[val] = key

print(dict2)

# program to get the sum of all the items in a dictionary.
print("_" * 25, '# Exercise 13', "_" * 25)
dict1 = {'x' : 23, 'y' : 10 , 'z' : 7}
sum = 0

for key, val in dict1.items():
    sum += val

print(sum)

# program to get the size of a dictionary.
# Hint : use sys.getsizeof(var) method.
print("_" * 25, '# Exercise 14', "_" * 25)
dict1 = {'x' : 23, 'y' : 10 , 'z' : 7}

# program to check whether a key exists in the dictionary or not.
print("_" * 25, '# Exercise 15', "_" * 25)
dict1 = {'Name': 'Santosh', 'Surname': 'Rachotimath', 'Age': 36, 'City': 'Bengaluru'}
str1 = 'Surname'
count = 0

for key in dict1.keys():
    if key == str1:
        count = 1

if count == 1:
    print("Exists")
else:
    print("Does Not Exists")

# program to create a dictionary in the form of (n^3) i.e. if key=2 value=8
print("_" * 25, '# Exercise 16', "_" * 25)
n = 10
dict1 = {}

for i in range(1,n+1):
    dict1[i] = i**3

print(dict1)

# program to insert a key at the beginning of the dictionary.
print("_" * 25, '# Exercise 17', "_" * 25)
dict1 = {'course': ' python', 'institute': 'sqatools'}
dict2 = {'name': 'Santosh'}

dict2.update(dict1)

print(dict2)

# program to create a dictionary where keys are between 1 to 5 and values are squares of the keys.
print("_" * 25, '# Exercise 18', "_" * 25)
n = 5
dict1 = {}

for i in range(1,n+1):
    dict1[i] = i**2

print(dict1)

# program to find the product of all items in the dictionary.
print("_" * 25, '# Exercise 19', "_" * 25)

dict1 = { 'a' : 2, 'b' : 4, 'c' : 5}
prod = 1

for val in dict1.values():
    prod *= val

print(prod)

# program to remove a key from the dictionary.
print("_" * 25, '# Exercise 20', "_" * 25)

#1
dict1 = {'a': 2, 'b': 4, 'c': 5}
result = dict1.popitem()
print(dict1)
#2
print("_" * 25, '# Exercise 20', "_" * 25)
dict1 = {'a': 2, 'b': 4, 'c': 5}

dict1.pop('b')
print(dict1)

# program to find maximum and minimum values in a dictionary.
print("_" * 25, '# Exercise 21', "_" * 25)

dict1 = {'a': 10, 'b': 44, 'c': 5,  'd': 560}
list1 = []
for val in dict1.values():
    list1.append(val)

print('Max :', max(list1))
print('Max :', min(list1))

# program to group the same items into a dictionary value.
print("_" * 25, '# Exercise 22', "_" * 25)

list1 = [1, 3, 4, 4, 2, 5, 3, 1, 5, 5, 2]

# program to replace words in a string using a dictionary.
print("_" * 25, '# Exercise 23', "_" * 25)
str1 = 'learning python at sqa-tools'
dict1 = { 'at' : 'is', 'sqa-tools' : 'fun'}

list1 = str1.split(" ")

for key, value in dict1.items():
    for word in list1:
        if key == word:
            print(word, value)
            str1 = str1.replace(word, value)

print(str1)

# program to remove a word from the string if it is a key in a dictionary.
print("_" * 25, '# Exercise 24', "_" * 25)
str1 = 'sqatools is best for learning python'
dict1 = {'best': 2, 'learning': 6, 'sqa': 5}

for key, val in dict1.items():
    str1 = str1.replace(key,'')

print(str1)

'''

# program to remove duplicate values from dictionary values.
print("_" * 25, '# Exercise 25', "_" * 25)

