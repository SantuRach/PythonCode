'''



"""
################################# Python tuple #################################
"""
# print even number
print("_" * 50)
print(dir(tuple)) # 'count', 'index'
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
tup1 = (1, 2, 'count', 'index', 3, 'Hello', (4,5,6), [7,8,9])
for val in tup1:
    print(val, type(val))

############################ tuple indexing ############################
# print all values in tuple
print("_" * 50)
tup1 = (1, 2, 'count', 'index', 3, 'Hello', (4,5,6), [7,8,9])
for i in range(len(tup1)):
    print(i, tup1[i])

############################ tuple slicing ############################
# print all values in tuple
print("_" * 50)

tup1 = (1, 2, 'count', 'index', 3, 'Hello', (4,5,6), [7,8,9])

print(tup1[0:]) # (1, 2, 'count', 'index', 3, 'Hello', (4, 5, 6), [7, 8, 9])
print(tup1[2:]) # ('count', 'index', 3, 'Hello', (4, 5, 6), [7, 8, 9])
print(tup1[1::2]) # (2, 'index', 'Hello', [7, 8, 9])
print(tup1[-1:5:1]) # ()
print(tup1[-3::1]) # 'Hello', (4,5,6), [7,8,9]

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
print("_"*50)
tup5 = (4, 6, 8, 1, 18, 2, 6, 2, 6, 2, 7, 1, 1, 1)

print("max value :", max(tup5))  # 55
print("Min value :", min(tup5))  # 12
print("Sum value :", sum(tup5))  # 184
'''

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
    val = val**2
    list1.append(val)

tup2 = tuple(list1)
tup2 = list(zip(tup1, tup2))
print(tup2)

# program to create a tuple and find an element from it by its index no.
print("_" * 25, '# Exercise 4', "_" * 25)
tup1 = (4, 6, 8, 3, 8, 6, 88, 66, 45)

tup2 = tup1.index(66)
print(tup2) #7


# program to assign values of tuples to several variables and print them.
print("_" * 25, '# Exercise 5', "_" * 25)
tup1 = (4, 6, 8)
var1 = 'a'
var1 = 'a'
var1 = 'a'

tup2 = tup1.index(66)
print(tup2) #7

















