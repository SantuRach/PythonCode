"""
################################# Python tuple #################################
"""
# print even number
print("_" * 50)
print(dir(tuple))  # 'count', 'index'
# ['__add__', '__class__', '__class_getitem__',
# '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__',
# '__format__', '__ge__', '__getattribute__', '__getitem__',
# '__getnewargs__', '__getstate__', '__gt__', '__hash__',
# '__init__', '__init_subclass__', '__iter__', '__le__',
# '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__',
# '__reduce_ex__', '__repr__', '__rmul__', '__setattr__', '__sizeof__',
# '__str__', '__subclasshook__',
# 'count', 'index']

# print all values in tuple
print("_" * 50)
tup1 = (1, 2, 'count', 'index', 3, 'Hello', (4, 5, 6), [7, 8, 9])
for val in tup1:
    print(val, type(val))

############################ tuple indexing ############################
# print all values in tuple
print("_" * 50)
tup1 = (1, 2, 'count', 'index', 3, 'Hello', (4, 5, 6), [7, 8, 9])
for i in range(len(tup1)):
    print(i, tup1[i])

############################ tuple slicing ############################
# print all values in tuple
print("_" * 50)

tup1 = (1, 2, 'count', 'index', 3, 'Hello', (4, 5, 6), [7, 8, 9])

print(tup1[0:])  # (1, 2, 'count', 'index', 3, 'Hello', (4, 5, 6), [7, 8, 9])
print(tup1[2:])  # ('count', 'index', 3, 'Hello', (4, 5, 6), [7, 8, 9])
print(tup1[1::2])  # (2, 'index', 'Hello', [7, 8, 9])
print(tup1[-1:5:1])  # ()
print(tup1[-3::1])  # 'Hello', (4,5,6), [7,8,9]

############################ tuple delete ############################
print("_" * 50)
tup4 = (4, 6, 8, 1, 18, 2, 6, 2, 6, 2, 7)

# del tup4  : This will delete the tuple variable from memory
# print(tup4)
# del tup4[2:5]  # 'tuple' object does not support item deletion


############################ tuple count ############################
print("_" * 50)
tup4 = (4, 6, 8, 1, 18, 2, 6, 2, 6, 2, 7, 1, 1, 1)

print("count of 1 is : ", tup4.count(1))

############################ tuple index ############################
print("_" * 50)
tup4 = (4, 6, 8, 1, 18, 2, 6, 2, 6, 2, 7, 1, 1, 1)

print("Index is: ", tup4.index(18))

############# Get max, min, and sum of values #######
print("_" * 50)
tup5 = (4, 6, 8, 1, 18, 2, 6, 2, 6, 2, 7, 1, 1, 1)

print("max value :", max(tup5))  # 55
print("Min value :", min(tup5))  # 12
print("Sum value :", sum(tup5))  # 184

# program to create a tuple with 2 lists of data.
print("_" * 25, '# Exercise 1', "_" * 50)

list1 = [4, 6, 8]
list2 = [7, 1, 4]
list3 = []
tup1 = list(zip(list1, list2))
print(tup1)

# program to find the maximum value from a tuple.
print("_" * 25, '# Exercise 2', "_" * 50)

tup1 = (4, 6, 8, 77, 9, 6, 888, 1, 0, -9)

print("Maximum : ", max(tup1))
print("Minimum : ", min(tup1))
print("Sum : ", sum(tup1))

# program to create a list of tuples from a list having a number and its square in each tuple.
print("_" * 25, '# Exercise 3', "_" * 25)
tup1 = (4, 6, 8, 3)
list1 = []

for val in tup1:
    val = val ** 2
    list1.append(val)

tup2 = tuple(list1)
tup2 = list(zip(tup1, tup2))
print(tup2)

# program to create a tuple and find an element from it by its index no.
print("_" * 25, '# Exercise 4', "_" * 25)
tup1 = (4, 6, 8, 3, 8, 6, 88, 66, 45)

tup2 = tup1.index(66)
print(tup2)  #7

# program to assign values of tuples to several variables and print them.
print("_" * 25, '# Exercise 5', "_" * 25)
tup1 = (4, 6, 8)
(a, b, c) = tup1
print("a :", a)
print("b :", b)
print("c :", c)

# program to add an item to a tuple.
print("_" * 25, '# Exercise 6', "_" * 25)
tup1 = (4, 6, 8)
list1 = list(tup1)
list1.append(55)
tup1 = tuple(list1)
print(tup1)

# tuple program to convert a tuple into a string.
print("_" * 25, '# Exercise 7', "_" * 25)
tup1 = ('s', 'q', 'a', 't', 'o', 'o', 'l', 's')
str1 = ''

for char in tup1:
    str1 += char

print(str1)

# program to get the 2nd element from the front and the 3rd element from the back of the tuple.
print("_" * 25, '# Exercise 8', "_" * 25)
tup1 = ('s', 'q', 'a', 't', 'o', 'o', 'l', 's')

print(tup1[1], tup1[-3])

# program to check whether an element exists in a tuple or not.
print("_" * 25, '# Exercise 9', "_" * 25)
tup1 = ('s', 'q', 'a', 't', 'o', 'o', 'l', 's')
Ele = 'm'
if Ele in tup1:
    print('True')
else:
    print('False')

# program to add a list in the tuple.
print("_" * 25, '# Exercise 10', "_" * 25)
tup1 = ('s', 'q', 'a', 't', 'o', 'o', 'l', 's')
list1 = [1, 2, 3]
tup1 = list(tup1)
tup1.extend(list1)
print(tuple(tup1))

# program to add row-wise elements in Tuple Matrix
print("_" * 25, '# Exercise 11', "_" * 25)
tup1 = (3, 6)
list1 = [[('sqa', 4)], [('tools', 8)]]

# program to create a tuple having squares of the elements from the list.
print("_" * 25, '# Exercise 12', "_" * 25)
list1 = [(1, 5, 7), (3, 6), 9]
list2 = []

for word in list1:
    if type(word) is tuple:
        for val in word:
            prod = val ** 2
            list2.append(prod)
    else:
        prod = word ** 2
        list2.append(prod)

print(tuple(list2))

# program to multiply adjacent elements of a tuple.
print("_" * 25, '# Exercise 13', "_" * 25)
tup1 = (1, 2, 3, 4, 5, 6)
list1 = []

for i in range(len(tup1) - 1):
    prod = tup1[i] * tup1[i + 1]
    list1.append(prod)
print(tuple(list1))

# program to join tuples if the initial elements of the sub-tuple are the same.
print("_" * 25, '# Exercise 14', "_" * 25)
list1 = [(3, 6, 7), (7, 8, 4), (7, 3), (3, 0, 5), (1, 2), (1, 3, 4, 5)]
list_final = []

for tup in list1:
    for tup2 in list1:
        if tup != tup2:
            if tup[0] == tup2[0]:
                list2 = (list(tup))
                list3 = (list(tup2))
                list2.extend(list3[1:])
                list_final.append(tuple(list2))
                list1.remove(tup2)

print('Result is : ', list_final)

# program to convert a list into a tuple and multiply each element by 2.
print("_" * 25, '# Exercise 15', "_" * 25)
list1 = [12, 65, 34, 77]
list2 = []

for val in list1:
    val = val * 2
    list2.append(val)

print('Result is : ', tuple(list2))

# Python tuple program to remove an item from a tuple.
print("_" * 25, '# Exercise 16', "_" * 25)
tup1 = ('p', 'y', 't', 'h', 'o', 'n')
list2 = list(tup1)
list2.remove(list2[3])

print('Result is : ', tuple(list2))

# program to slice a tuple.
print("_" * 25, '# Exercise 17', "_" * 25)
tup1 = (1, 2, 3, 4, 5, 6)

print('Result is 1: ', tup1[0:3])
print('Result is 2: ', tup1[3:])

# program to slice a tuple.
print("_" * 25, '# Exercise 17', "_" * 25)
tup1 = (1, 2, 3, 4, 5, 6)

print('Result is 1: ', tup1[0:3])
print('Result is 2: ', tup1[3:])

# program to find an index of an element in a tuple.
print("_" * 25, '# Exercise 18', "_" * 25)
tup1 = ('p', 'y', 't', 'h', 'o', 'n')

print('Index of t is: ', tup1.index('t'))

# program to convert a tuple into a dictionary.
print("_" * 25, '# Exercise 19', "_" * 25)
tup1 = ((5, 's'), (6, 'l'))
tup1 = dict(tup1)
print('Index of t is: ', tup1)

# program to reverse a tuple.
print("_" * 25, '# Exercise 20', "_" * 25)
tup1 = (1, 2, 3, 4, 5, 6)

print('Reverse is : ', tup1[::-1])

# program to convert a tuple into a dictionary.
print("_" * 25, '# Exercise 21', "_" * 25)
tup1 = [('s', 2), ('q', 1), ('a', 1), ('s', 3), ('q', 2), ('a', 4)]

# program to pair all combinations of 2 tuples.
print("_" * 25, '# Exercise 22', "_" * 25)
tup1 = (1, 2)
tup2 = (3, 4)
list1 = []
for val in tup1:
    for val1 in tup2:
        list1.append((val, val1))
        list1.append((val1, val))

print(list1)

# program to remove tuples of length i.
print("_" * 25, '# Exercise 23', "_" * 25)

leng = 2
list1 = [(2, 5, 7), (3, 4), (8, 9, 0, 5)]
for tup in list1:
    if len(tup) == leng:
        list1.remove(tup)

print(list1)

# tuple program to remove tuples from the List having an element as None.
print("_" * 25, '# Exercise 23', "_" * 25)

#list1 = [(1,6,7), (None, None),(5, 4)]
list1 = [(None, 2), (None, None), (5, 4), (1, 6, 7), (1, None)]
for tup in list1:
    for val in tup:
        if val == None:
            list1.remove(tup)
            break

print(list1)

# program to remove Tuples from the List having every element as None.
print("_" * 25, '# Exercise 24', "_" * 25)

list1 = [(None, 2), (None, None), (5, 4), (1, 6, 7), (1, None)]

for tup in list1:
    count = 0
    for val in tup:
        if val == None:
            count += 1
            print("1")
        else:
            print('S')
    if count == len(tup):
        list1.remove(tup)

print(list1)

# program to calculate the frequency of elements in a tuple.
print("_" * 25, '# Exercise 25', "_" * 25)

tup1 = ('a', 'b', 'c', 'd', 'b', 'a', 'b')
dict1 = {}

for char in tup1:
    if char not in dict1:
        dict1[char] = 0
    if char in dict1:
        dict1[char] += 1

print(dict1)

# program to assign the frequency of tuples to each tuple.
print("_" * 25, '# Exercise 26', "_" * 25)

tup1 = [('s', 'q'), ('t', 'o', 'o', 'l'), ('p', 'y'), ('s', 'q')]
dict1 = {}

for char in tup1:
    if char not in dict1:
        dict1[char] = 0
    if char in dict1:
        dict1[char] += 1

print(dict1)

# program to test whether a tuple is distinct or not.
print("_" * 25, '# Exercise 27', "_" * 25)

tup1 = (1, 2, 3, 4, 3)
tup2 = (1, 2, 3, 4, 3)

for i in range(len(tup1)):
    if tup1.count(i) > 1:
        print("Not Distinct")
    else:
        print("Distinct")

# program to convert a tuple of string values to a tuple of integer values.
print("_" * 25, '# Exercise 28', "_" * 25)

tup1 = ('4563', '68', '1')
list1 = []
for i in range(len(tup1)):
    val = int(tup1[i])
    list1.append(val)
print(tuple(list1))

# program to convert a given tuple of integers into a number.
print("_" * 25, '# Exercise 29', "_" * 25)

tup1 = (4, 5, 3, 8)
res = ''
for val in tup1:
    i = str(val)
    res += i
print(res)

# program to multiply ith element from each tuple from a list of tuples.
print("_" * 25, '# Exercise 30', "_" * 25)

list1 = [(4, 8, 3), (3, 4, 0), (1, 6, 2)]
i = 1
prod = 1

for val in list1:
    prod *= val[i]

print(prod)

# Python tuple program to flatten a list of lists into a tuple.
print("_" * 25, '# Exercise 31', "_" * 25)

list1 = [['s'], ['q'], ['a'], ['t'], ['o'], ['o'], ['l'], ['s', 'R']]
list2 = []
for val in list1:
    for char in val:
        list2.append(char)

print(list2)

# program to flatten a tuple list into a string
print("_" * 25, '# Exercise 32', "_" * 25)

list1 = [('s', 'q', 'a'), ('t', 'o'), ('o', 'l', 's')]
str1 = ''
for val in list1:
    for char in val:
        str1 += str(char)

print(str1)

# program to convert a tuple into a list by adding the string after every element of the tuple.
print("_" * 25, '# Exercise 33', "_" * 25)

tup1 = (1, 2, 3, 4, 5)
str1 = 'sqatools'
list1 = []
for val in tup1:
    list1.append(val)
    list1.append(str1)

print(list1)

# program to concatenate two tuples.
print("_" * 25, '# Exercise 34', "_" * 25)

tup1 = (1, 2, 3, 4, 5)
tup2 = (6, 7)

list1 = []
list1.append(tup1)
list1.append(tup2)

print(list1)

# program to concatenate two tuples.
print("_" * 25, '# Exercise 35', "_" * 25)

list1 = [('very', 8), ('i', 6), ('am', 5), ('happy', 0)]
list2 = ['i', 'am', 'very', 'happy']
list3 = []
for char in list2:
    for word in list1:
        if char in word:
            list3.append(word)

print(list3)

# program to concatenate two tuples.
print("_" * 25, '# Exercise 36', "_" * 25)

list1 = (1, 1, 1)
length = len(list1)
prod = 0

for val in list1:
    prod += val * 2 ** (length - 1)
    length -= 1

print(prod)

# program to swap tuples
print("_" * 25, '# Exercise 37', "_" * 25)

tup1 = (1, 2, 3)
tup2 = (4, 5)
print(tup1)
print(tup2)

tup1, tup2 = tup2, tup1

print(tup1)
print(tup2)

# program to swap tuples
print("_" * 25, '# Exercise 38', "_" * 25)

tup1 = (1, 2, 3, 4)
tup2 = (4, 5)
print(tup1)
print(tup2)

tup1, tup2 = tup2, tup1

print(tup1)
print(tup2)
