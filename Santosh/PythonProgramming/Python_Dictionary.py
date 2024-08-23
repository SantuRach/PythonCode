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
dict1 = {'a': 5, 'b': 3, 'c': 6, 'd': 8}

for key, val in dict1.items():
    print('Square of ', key, ':', val ** 2)

# program to move items from dict1 to dict2.
print("_" * 25, '# Exercise 3', "_" * 25)
dict1 = {'a': 5, 'b': 3, 'c': 6, 'd': 8}
dict2 = {}
for key, val in dict1.items():
    dict2[key] = val

print(dict1)
print(dict2)

# program to concatenate two dictionaries.
print("_" * 25, '# Exercise 4', "_" * 25)
dict1 = {'Name': 'Santosh', 'Roll no': 2807, 'Address': 'Bangalore'}
dict2 = {'Age': 36, 'salary': '$25k'}

dict1.update(dict2)
print(dict1)

# program to get a list of odd and even keys from the dictionary.
print("_" * 25, '# Exercise 5', "_" * 25)
dict1 = {1: 25, 5: 'abc', 8: 'pqr', 21: 'xyz', 12: 'def', 2: 'utv'}
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
dict1 = dict(zip(list1, list2))

print('dict from 2 lists :', dict1)

# Program to store squares of even and cubes of odd numbers
# in a dictionary using dictionary comprehension.
print("_" * 25, '# Exercise 7', "_" * 25)
list1 = [4, 5, 6, 2, 1, 7, 11, 3]
dict1 = {}

for val in list1:
    if val % 2 == 0:
        dict1[val] = val ** 2
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
dict1 = {'d': 21, 'b': 53, 'a': 13, 'c': 41}

# Dprogram to sort a dictionary in  python using values.
print("_" * 25, '# Exercise 12', "_" * 25)
dict1 = {'d': 21, 'b': 53, 'a': 13, 'c': 41}

# program to add a key in a dictionary.
print("_" * 25, '# Exercise 12', "_" * 25)
dict1 = Input = {'name': 'yash', 'city': 'pune'}
dict2 = {}
for key, val in dict1.items():
    dict2[val] = key

print(dict2)

# program to get the sum of all the items in a dictionary.
print("_" * 25, '# Exercise 13', "_" * 25)
dict1 = {'x': 23, 'y': 10, 'z': 7}
sum = 0

for key, val in dict1.items():
    sum += val

print(sum)

# program to get the size of a dictionary.
# Hint : use sys.getsizeof(var) method.
print("_" * 25, '# Exercise 14', "_" * 25)
dict1 = {'x': 23, 'y': 10, 'z': 7}

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

for i in range(1, n + 1):
    dict1[i] = i ** 3

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

for i in range(1, n + 1):
    dict1[i] = i ** 2

print(dict1)

# program to find the product of all items in the dictionary.
print("_" * 25, '# Exercise 19', "_" * 25)

dict1 = {'a': 2, 'b': 4, 'c': 5}
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

dict1 = {'a': 10, 'b': 44, 'c': 5, 'd': 560}
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
dict1 = {'at': 'is', 'sqa-tools': 'fun'}

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
    str1 = str1.replace(key, '')

print(str1)

# program to remove duplicate values from dictionary values.
print("_" * 25, '# Exercise 25', "_" * 25)
dict1 = {'marks1': [23, 28, 23, 69], 'marks2': [25, 14, 25]}

for key, val in dict1.items():
    dict1[key] = set(val)

print(dict1)

# program to add two dictionaries if the keys are the same then add their value.
print("_" * 25, '# Exercise 26', "_" * 25)
dict1 = {'x': 10, 'y': 20, 'c': 50, 'f': 44}
dict2 = {'x': 60, 'c': 25, 'y': 56}
dict3 = {}

for key1, val1 in dict1.items():
    for key2, val2 in dict2.items():
        if key1 == key2:
            dict3[key1] = val1 + val2

print(dict3)

# program to print all the unique values in a dictionary.
print("_" * 25, '# Exercise 27', "_" * 25)
list1 = [{'name1': 'robert'}, {'name2': 'john'}, {'name3': 'jim'}, {'name4': 'robert'}]
list2 = []
for word in list1:
    for val in word.values():
        if val not in list2:
            list2.append(val)

print(list2)

# program to display different combinations of letters from dictionary values.
print("_" * 25, '# Exercise 28', "_" * 25)
dict1 = {'x': ['e', 'f'], 'y': ['a', 'b']}

# program to print the given dictionary in the form of tables.
print("_" * 25, '# Exercise 29', "_" * 25)
dict1 = {'names': ['virat', 'messi', 'kobe'], 'sport': ['cricket', 'football', 'basketball']}

# program to sort a list of values in a dictionary.
print("_" * 25, '# Exercise 30', "_" * 25)
dict1 = {'a1': [1, 5, 3], 'a2': [10, 6, 20]}

for key, val in dict1.items():
    dict1[key] = sorted(val)

print(dict1)

# program to get a product with the highest price from a dictionary.
print("_" * 25, '# Exercise 31', "_" * 25)
dict1 = {'price1': 450, 'price2': 600, 'price3': 255, 'price4': 400}
high = 0

for word in dict1:
    if dict1[word] > high:
        high = dict1[word]
        high_word = word

print(high_word, high)

# program to print a dictionary line by line.
print("_" * 25, '# Exercise 32', "_" * 25)
dict1 = {'virat': {'sport': 'cricket', 'team': 'india'}, 'messi': {'sport': 'football', 'team': 'argentina'}}

for key1, val1 in dict1.items():
    print(key1)
    for key2, val2 in val1.items():
        print(key2, ':', val2)
    print()

# program to print a dictionary line by line.
print("_" * 25, '# Exercise 33', "_" * 25)
dict1 = {'sqa': [1, 4, 6], 'tools': [3, 6, 9]}
list1 = []
for key1, val1 in dict1.items():
    val1.insert(0, key1)
    list1.append(val1)

print(list1)

# program to convert a list of dictionaries to a list of lists.
print("_" * 25, '# Exercise 34', "_" * 25)
list1 = [{'sqa': 123, 'tools': 456, 'sqa1': 123, 'tools1': 456}]
list2 = []
for word in list1:
    for key1, val1 in word.items():
        list2.append([key1])
        list2.append([val1])

print(list2)

# program to replace dictionary values with their average.
print("_" * 25, '# Exercise 35', "_" * 25)
dict1 = {'name': 'ketan', 'subject': 'maths', 'p1': 80, 'p2': 70}
num1 = dict1.pop('p1')
num2 = dict1.pop('p2')
dict1['p1+p2'] = (num1 + num2) / 2

print(dict1)

#  program to convert a list of Tuples into a dictionary
print("_" * 25, '# Exercise 36', "_" * 25)
list1 = [('mike', 1), ('Sarah', 20), ('Jim', 16)]
dict1 = {}

for word in list1:
    dict1[word[0]] = word[1]

print(dict1)

#  program to convert string to the dictionary.
print("_" * 25, '# Exercise 37', "_" * 25)
str1 = 'Apr=April; Mar=March'
dict1 = {}
list1 = str1.split("; ")
for word in list1:
    dict1[word[0:3]] = word[4:]

print(dict1)

#  program to convert a matrix into a dictionary.
print("_" * 25, '# Exercise 38', "_" * 25)
list1 = [[1, 2, 3], [4, 5, 6]]
dict1 = {}

for i in range(len(list1)):
    dict1[i + 1] = list1[i]

print(dict1)

#  program to check all values are the same in a dictionary.
print("_" * 25, '# Exercise 39', "_" * 25)

dict1 = {'virat': 50, 'rohit': 50, 'rahul': 50, 'hardik': 50}
temp = dict1['virat']
count = 0

for val in dict1.values():
    if val == temp:
        count += 1

if count == len(dict1):
    print('All values are same')
else:
    print('All values are not same')

#  program to create a dictionary grouping a sequence of key-value pairs into a dictionary of lists.
print("_" * 25, '# Exercise 40', "_" * 25)

dict1 = {'virat': 50, 'rohit': 40, 'virat': 30, 'rohit': 10}

#  program to split a given dictionary of lists into list of dictionaries.
# [ {t20:50, odi:70} ,{t20:40, odi:10}, {t20:30, odi:0}, {t20:45, odi:65} ]
print("_" * 25, '# Exercise 41', "_" * 25)

dict1 = {'t20': [50, 40, 30, 45], 'odi': [70, 10, 0, 65]}

#  program to remove a specified dictionary from a given list.
# Remove 4th dict
print("_" * 25, '# Exercise 42', "_" * 25)

list1 = [{'t20': 50, 'odi': 70}, {'t20': 40, 'odi': 10}, {'t20': 30, 'odi': 0}, {'t20': 45, 'odi': 65}]

list1.pop(3)

print(list1)

#  program to convert string values of a given dictionary, into integer/float datatypes.
# Remove 4th dict
print("_" * 25, '# Exercise 43', "_" * 25)

dict1 = {'a': '30', 'b': '20', 'c': '20'}
dict2 = {'a': '3.33', 'b': '20.50', 'c': '12.5'}

for key1, val1 in dict1.items():
    dict1[key1] = int(val1)

for key2, val2 in dict2.items():
    dict2[key2] = float(val2)

print(dict1)
print(dict2)

#  Python dictionary contains a list as a value. Python program to clear the list values in the said dictionary.
print("_" * 25, '# Exercise 44', "_" * 25)

dict1 = {'virat': [50, 30], 'rohit': [40, 10]}

for val in dict1.values():
    val.clear()

print(dict1)

#  Python dictionary contains a list as a value. Python program to clear the list values in the said dictionary.
print("_" * 25, '# Exercise 45', "_" * 25)

dict1 = {'virat': [50, 30], 'rohit': [40, 10]}

#  program to extract a list of values from a given list of dictionaries
print("_" * 25, '# Exercise 46', "_" * 25)

list1 = [{'t20': 50, 'odi': 70}, {'t20': 40, 'odi': 10}, {'t20': 30, 'odi': 0}, {'t20': 45, 'odi': 65}]
list_t20 = []
list_odi = []
for word in list1:
    print(len(word))  # to cover other exercise
    for key, val in word.items():
        if key == 't20':
            list_t20.append(val)
        else:
            list_odi.append(val)

print(list_t20)
print(list_odi)

#  program to create nested Dictionary using List.
print("_" * 25, '# Exercise 47', "_" * 25)

dict1 = {8: 'sqa', 6: 'tools', 7: 'python'}
list1 = [1, 2, 3]
list2 = []

for word in dict1.items():
    list2.append(word)
dict2 = dict(zip(list1, list2))
print(dict2)

#  program to remove keys with values greater than n.
print("_" * 25, '# Exercise 48', "_" * 25)

dict1 = {'sqa': 3, 'tools': 5, 'python': 7}
rem_val = 6
dict2 = {}

for key, val in dict1.items():
    if val < rem_val:
        dict2[key] = val
print(dict2)

#  program to remove keys with substring values.
print("_" * 25, '# Exercise 49', "_" * 25)

dict1 = {1: 'sqatools is best', 2: 'for learning python'}
substr = ['best', ' excellent']

dict2 = {}

#  program to filter even numbers from a given dictionary value.
print("_" * 25, '# Exercise 50', "_" * 25)

dict1 = {'a': [11, 4, 6, 15], 'b': [3, 8, 12], 'c': [5, 3, 10]}

#  program to find the keys of maximum values in a given dictionary.
#  Find keys of first 2 max values from the dictionary.
print("_" * 25, '# Exercise 51', "_" * 25)

dict1 = {'a': 18, 'b': 50, 'c': 36, 'd': 47, 'e': 60}
list1 = []

for val in dict1.values():
    list1.append(val)

res = sorted(list1)
for key1, val1 in dict1.items():
    if val1 == res[-1] or val1 == res[-2]:
        print(key1, end=" ")

#  program to find the shortest list of values with the keys in a given dictionary.
print("_" * 25, '# Exercise 52', "_" * 25)

dict1 = {'a': [10, 12], 'b': [10], 'c': [10, 20, 30, 40], 'd': [20]}

for key, val in dict1.items():
    if len(val) == 1:
        print(key)

#  program to count the frequency in a given dictionary.
print("_" * 25, '# Exercise 53', "_" * 25)

dict1 = {'a': 10, 'b': 20, 'c': 25, 'd': 10, 'e': 30, 'f': 20}
list1 = []
dict2 = {}
for key, val in dict1.items():
    list1.append(val)

for ele in list1:
    count = list1.count(ele)
    dict2[ele] = count

print(dict2)

#  program to create key-value list pairings in a given dictionary.
print("_" * 25, '# Exercise 54', "_" * 25)

dict1 = {1: ['Virat Kohli'], 2: ['Rohit Sharma'], 3: ['Hardik Pandya']}
list1 = []
dict2 = {}
for key, val in dict1.items():
    val = str(val)
    dict2[key] = val[2:-2]
print([dict2])

#  program to group the elements of a given list based on the given function.
#  Hint : Function name: len().
print("_" * 25, '# Exercise 55', "_" * 25)

list1 = ['abc', 'defg', 'hijkl']
dict2 = {}
for word in list1:
    dict2[len(word)] = word
print([dict2])

#  program to initialize a dictionary with default values.
print("_" * 25, '# Exercise 56', "_" * 25)

list1 = ['Virat', 'Rohit']
dict1 = {'sport': 'cricket', 'salary': 100000}

#  program to delete a list of keys from a dictionary.
#  Keys to be removed:  [ ‘a’, ‘d’, ‘e’ ].
print("_" * 25, '# Exercise 58', "_" * 25)

dict1 = {'a': 19, 'b': 20, 'c': 21, 'd': 20, 'e': 50}

dict1.pop('a')
dict1.pop('d')
dict1.pop('e')

print(dict1)

#method 2
dict1 = {'a': 19, 'b': 20, 'c': 21, 'd': 20, 'e': 50}
del_key = ['a', 'd', 'e']

for key in del_key:
    del dict1[key]

print(dict1)

#  program to rename key of a dictionary.
print("_" * 25, '# Exercise 59', "_" * 25)

dict1 = {'a': 19, 'b': 20, 'c': 21, 'd': 20, 'e': 50}

dict1['f'] = dict1.pop('e')
print(dict1)

#  program to Invert a given dictionary with non-unique hashable values.
print("_" * 25, '# Exercise 60', "_" * 25)

dict1 = {'alex': 1, 'bob': 2, ' martin': 1, 'robert': 2}
list1 = []
list2 = []
list3 = []
list4 = []

for key, val in dict1.items():
    if val == 1:
        list1.append(key)
        if val not in list3:
            list3.append(val)
    elif val == 2:
        list2.append(key)
        if val not in list4:
            list4.append(val)

dict2 = dict.fromkeys(list3, list1)
dict2.update(dict.fromkeys(list4, list2))

print(dict2)

#  program to Sort Dictionary by values summation
print("_" * 25, '# Exercise 61', "_" * 25)

#  program to convert a dictionary into n sized dictionary.
print("_" * 25, '# Exercise 62', "_" * 25)

dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
N = 3
count = 0
dict2 = {}
list1 = []
list2 = []
list3 = []

for word in dict1.items():
    if count < N:
        count += 1
        list1.append(word)
    else:
        list2.append(word)
list1 = dict(list1)
list2 = dict(list2)

list3.append(list1)
list3.append(list2)
print(list3)

#  program to reverse each string value in the dictionary and add an
#  underscore before and after the Keys.
print("_" * 25, '# Exercise 63', "_" * 25)

dict1 = {'a': 'Python', 'b': 'Programming', 'c': 'Learning'}
dict2 = {}
for key, val in dict1.items():
    key = '_' + key + '_'
    dict2[key] = val[::-1]

print(dict2)

#  program to sum unique elements from dictionary list values.
print("_" * 25, '# Exercise 64', "_" * 25)

dict1 = {'a': [6, 7, 2, 8, 1], 'b': [2, 3, 1, 6, 8, 10], 'd': [1, 8, 2, 6, 9]}
sum1 = 0
list1 = []
for key, val in dict1.items():
    for value in val:
        if value not in list1:
            list1.append(value)
            sum1 += value

print(sum1)

