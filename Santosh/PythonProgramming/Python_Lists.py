
"""
################################# Python Lists #################################
"""
# print even number
print("_" * 50)
list1 = [3, 6, 2, 7, 1, 4, 8]
for val in list1:
    if val % 2 == 0:
        print(val, end=" ")

# print odd number using indexing
print("\n")
print("_" * 50, "\n")
list1 = [3, 6, 2, 7, 1, 4, 8]
for val in range(len(list1)):
    if list1[val] % 2 != 0:
        print(list1[val], end=" ")

"""
################################# Lists Slicing #################################
"""
# print middle number
print("_" * 50)
list1 = [3, 6, 2, 7, 1, 4, 8]
print(list1[3:6], end=" ")

print("_" * 50)
print(list1[::-2], end=" ")

"""
################################# Lists Slicing #################################
"""
print("_" * 50)
print(dir(list))
"""
Add methods - 'append', 'insert', 'extend', 
Remove methods - 'clear', 'pop', 'remove', del
'index', 'sort', 'copy', 'count', 'reverse'

"""

################################# append #################################
# append method: This method add one data at time in list at the end.
print("_" * 50)
list1 = [1, 2, 3]
list1.append(100)
print(list1)

list1.append('Santosh')
print(list1)

list1.append([1, 2, 3])
print(list1)

################################# insert #################################
# insert() method : This method add data to the specific index position.
# 2 is the index position in the below example: list1.insert(2, 500)

print("_" * 50)
list1 = [1, 2, 3, 4]
list1.insert(2, 500)
print(list1)

################################# extend #################################
# extend method : This method helps to insert one list data to another list

print("_" * 50)
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd', 'e']
list1.extend(list2)
print(list1)

list2.extend(list1)
print(list2)

################################# Concatenation #################################
# it will not modify original lists
print("_" * 50)
list1 = [1, 2, 3, 4]
list2 = ['a', 'b', 'c', 'd', 'e']

list3 = list1 + list2
print(list3)

list3 = list2 + list1
print(list3)

################################# repeatation #################################
# it will not modify original lists. Multiply by n
print("_" * 50)
list1 = [1, 2, 3, 4]

list3 = list1 * 5
print(list3)

################################# Remove data from list #################################
# remove method : this method remove any specific data from the list and
# does not return it.
print("_" * 50)
list1 = [1, 2, 3, 4]

list3 = list1.remove(3)
print(list3)  #None
print(list1)  # [1, 2, 4]

################################# Pop #################################
# Pop method : this method remove any specific data from the list and return it.
# Default index is -1

print("_" * 50)
list1 = [1, 2, 3, 4]
# remove with default index
list3 = list1.pop()
print(list3)  # 4
print(list1)  # 1,2,3

# remove with specific index
print("_" * 50)
list1 = [1, 2, 3, 4]

list3 = list1.pop(2)
print(list3)  # 3
print(list1)  # 1,2,4

################################# Clear  #################################
# clear method : This method remove all the data from the list.

print("_" * 50)
list1 = [1, 2, 3, 4]
# remove with default index
list3 = list1.clear()
print(list3)  # None?
print(list1)  # []

################################# del  #################################
# del : this will remove complete list variable from the memory.
# del can delete in, float, list, string and any data type.

print("_" * 50)
list1 = [1, 2, 3, 4]
# remove with default index
del list1
#print(list1)   # throws error because it is deleted

################################# index  #################################
print("_" * 50)
list1 = [1, 2, 3, 4, 5, 6]

print(list1[2])
print(list1)

list1[2] = 600

print(list1[2])
print(list1)

################################# Count  #################################
# count method : This method count the occurance of any element.
print("_" * 50)
list1 = [1, 2, 3, 4, 5, 6, 2, 2]

print(list1.count(2)) #3


################################# sort  #################################
#sort() method : This  method sort the list data in ascending and descending order and
# modify the original list and
# Does not return any value

print("_" * 50)
list1 = [10, 2, 38, 44, 5, 6, 21, 25]

list1.sort() # Ascending order
print(list1)

list1.sort(reverse=True) # Descending order
print(list1)

################################# sorted  function #################################
#sorted() method : This  method sort the list data in ascending and descending order and
# does not modify the original list
# returns a value

print("_" * 50)
list1 = [10, 2, 38, 44, 5, 6, 21, 25]

print(sorted(list1))  # Ascending order

print(sorted(list1, reverse=True))  # Descending order

print(list1) # Original list is not modified

################################# Reverse  method #################################
# reverse() method : This  method reverses the list data  and
# modify the original list and
# Does not return any value

print("_" * 50)
list1 = [10, 2, 38, 44, 5, 6, 21, 25]
list1.reverse()
print(list1)

################################# Reversed  method #################################
# reversed() method : This  method reverses the list data  and
# does not modify the original list
# returns a value

print("_" * 50)
list1 = [10, 2, 38, 44, 5, 6, 21, 25]

output = list(reversed(list1))
print(output)
print(list1) # Original list is not modified

#################################  Copy method #################################

####################### Shalllow copy #######################
# shallow copy : consider we have two lists list_a and list_b, if we will assign list_a to list_b
# then update the list_b, data. the changes done in list_b will reflect in list_a as well
# here new list is not created instead address location (reference) is shared
print("_" * 50)
list1 = [10, 2, 38, 44, 5, 6, 21, 25]
list2 = list1

list1.append(100)
list1.insert(3, 999)

print(list1, id(list1))
print(list2, id(list2))

####################### Deep copy #######################
# Deep copy : consider we have two lists list_a and list_b, if we will assign list_a to list_b
# then update the list_b, data. the changes done in list_b will not reflect in list_a
# here new list is created. address location (reference) is new
print("_" * 50)
list1 = [10, 2, 38, 44, 5, 6, 21, 25]
list2 = list1.copy()

list1.append(100)
list1.insert(3, 999)

print(list1, id(list1))
print(list2, id(list2))


####################### max and min and sum of values #######################
print("_" * 50)

list_m = [3, 6, 8, 33, 22, 12,]

print("Max number :", max(list_m))
print("Minimum value :", min(list_m))
print("sum of list value :", sum(list_m))


####################### list comprehension #######################
print("_" * 50)

list_m = [3, 6, 8, 33, 22, 12,]

result = [i for i in list_m if i % 2 == 0]
print(result)


result = [(i, "Even")  if i % 2 == 0 else (i, "Odd") for i in list_m]
print(result)

# Exercise 1
#   Python program to calculate the square of each number from the given list.
print("_" * 50)

list1 = [3, 9, 8, 33, 22, 12,25]
for val in list1:
    print("Square of ", val, "is ", val**2)

# Exercise 2
# Python program to combine two lists.
print("_" * 50)

list1 = [3, 0, 8, 33, 22, 12,25]
list2 = [4, 5, 0, 'Santosh']
list3 = list1 + list2
print(list3)

# Exercise 3
# program to calculate the sum of all elements from a list.
print("_" * 50)

list1 = [3, 0, 8, 33, 22, 12,25]

print(sum(list1))

# Exercise 4
# program to find a product of all elements from a given list.
print("_" * 50)

list1 = [3, 7, 8, 33, 22, 12,25]
prod = 1
for val in list1:
    prod *= val
print("Product :", prod)

# Exercise 5
# program to find the minimum and maximum elements from the list.
print("_" * 50)

list1 = [3, 7, 8, 33, 22, 12,25]

print("Min :", min(list1))
print("Max :", max(list1))

# Exercise 6
# program to differentiate even and odd elements from the given list.
print("_" * 50)

list1 = [3, 7, 8, 33, 22, 12,25]
list_even = []
list_odd = []
for val in list1:
    if val % 2 == 0:
        list_even.append(val)
    else:
        list_odd.append(val)

print("Even :", list_even)
print("Odd :", list_odd)

# Exercise 7
# program to remove all duplicate elements from the list.
print("_" * 50)

list1 = [3, 7, 8, 33, 22, 12,25, 7, 22, 35]
list2 = []
for val in list1:
    if val not in list2:
        list2.append(val)

print("Odd :", list2)

# Exercise 8
# program to print a combination of 2 elements from the list whose sum is 10.
print("_" * 50)

# Exercise 9
# program to split the list into two-part, the left side all odd values and
# the right side all even values.
print("_" * 50)

list1 = [3, 7, 82, 33, 28, 12, 25, 73, 22, 35]
list_even = []
list_odd = []
for val in list1:
    if val % 2 == 0:
        list_even.append(val)
    else:
        list_odd.append(val)
list_odd.extend(list_even)
print(list_odd)

# Exercise 10
# program to get common elements from two lists.
print("_" * 50)

list1 = [3, 7, 82, 33, 28, 12, 25, 73, 22, 35]
list2 = [3, 7, 82, 55, 66, 77]
list3 = []

for val in list1:
    if val in list2:
        list3.append(val)

print(list3)

# Exercise 11
# program to reverse a list with for loop.
print("_" * 50)

list1 = [3, 7, 82, 33, 28, 12, 25, 73, 22, 35]
list2 = []

for val in range(len(list1)):
    list2.insert(0, list1[val])

print(list2)


# Exercise 12
# program to reverse a list with reversed func.
print("_" * 50)

list1 = [3, 7, 82, 33, 28, 12, 25, 73, 22, 35]
list2 = list(reversed(list1))

print(list2)

# Exercise 13
# program to reverse a list with reverse methods.
print("_" * 50)

list1 = [3, 7, 82, 33, 28, 12, 25, 73, 22, 35]
list1.reverse()

print(list1)

# Exercise 14
# program to copy or clone one list to another list.
print("_" * 50)

list1 = [3, 7, 82, 33, 28, 12, 25, 73, 22, 35]
list2 = [1, 2, 3, 4]
list1.extend(list2)

print(list1)

# Exercise 15
# program to print a specific list after removing the 1st, 3rd, and 6th elements from the list.
print("_" * 50)

list1 = [3, 7, 82, 33, 28, 12, 25, 73, 22, 35]

list1.remove(list1[0])
list1.remove(list1[2])
list1.remove(list1[5])

print(list1)

# Exercise 16
# program to remove negative values from the list.
print("_" * 50)

list1 = [3, -7, 82, 33, 28, 12, -25, 73, 22, 35, -9, 55]

for val in list1:
    if val < 0:
        list1.remove(val)

print(list1)

# Exercise 17
# program to get a list of all elements which are divided by 3 and 7.
print("_" * 50)

list1 = [3, -7, 82, 33, 28, 12, -25, 73, 22, 35, -9, -57, 21, 42]
list2 = []
for val in list1:
    if val%3 == 0 and val%7 == 0:
        list2.append(val)

print(list2)

# Exercise 18
# Program to get a list of words which has vowels in the given string.
print("_" * 50)

str1 = 'www Student ppp are qqqq learning  Python vvv'
list1 = str1.split(" ")
vowels = 'aeiouAEIOU'
list2 = []

for word in list1:
    for char in word:
        if char in vowels:
            list2.append(word)
            break

print(list2)

# Exercise 19
# program to sort list data, with the sort and sorted method.
print("_" * 50)

list1 = [3, -7, 82, 33, 28, 12, -25, 73, 22, 35, -9, -57, 21, 42]

list1.sort()
print(list1)

print("_" * 50)
list2 = sorted(list1)
print(list2)


# Exercise 20
# program to remove data from the list from a specific index using the pop method.
print("_" * 50)

list1 = [3, -7, 82, 33, 28, 12, -25, 73, 22, 35, -9, -57, 21, 42]

list1.pop(5)
print(list1)

# Exercise 21
# program to check whether a list contains a sublist.
print("_" * 50)

list1 = [3, -7, 82, 33, 28, 12, -25, 73, 22, 35, -9, -57, 21, 42]
list2 = [3, -7, 82, 33, 28, 12, -25, 6]
count = 0

for val in list2:
    if val in list1:
        count += 1

if count == len(list2):
    print("Sublist")
else:
    print("Not Sublist")

# Exercise 22
# program to find the second largest number from the list.
print("_" * 50)

list1 = [3, -7, 82, 33, 28, 12, -25, 73, 22, 35, -9, -57, 21, 42]
print(max(list1))

list1.remove(max(list1))
print(max(list1))

# Exercise 23
# program to merge all elements of the list in a single entity using a special character.
print("_" * 50)

list1 = ["a", "b", "c", "d"]
str1 = str(list1)
print("$".join(list1))

# Exercise 24
# program to get the difference between two lists.
print("_" * 50)

list1 = ["a", "b", "c", "d",4, 5]
list2 = [1,2,3,"a",4,5,"e"]
list3 = []
for val1 in list1:
    if val1 not in list2:
        list3.append(val1)

print(list3)

# Exercise 25
# program to reverse each element of the list.
print("_" * 50)

list1 = ['Sqa', 'Tools', 'Online', 'Learning', 'Platform']
list2 = []

for word in list1:
    list2.append(word[::-1])
print(list2)


# Exercise 26
# program to get keys and values from the list of dictionaries.
print("_" * 50)

list1 = [{'a':12}, {'b': 34}, {'c': 23}, {'d': 11}, {'e': 15}]
keys = []
values = []
for word in list1:
    for a, b in word.items():
        keys.append(a)
        values.append(b)
print(keys)
print(values)

# Exercise 27
# program to get all the unique numbers in the list.
print("_" * 50)

list1 = ["a", "b", "c", "d",4, 5]
list2 = [1,2,3,"a",4,5,"e"]
list3 = []
for val1 in list1:
    if val1 in list2:
        list3.append(val1)

print(list3)

# Exercise 28
# program to convert a string into a list.
print("_" * 50)

str1 = 'I am learning python'
list1 = str1.split(" ")

print(list1)

# Exercise 29
# Python program to remove all odd index elements.
print("_" * 50)

list1 = [12, 32, 33, 5, 4, 7, 33]
list2 = []

for i in range(len(list1)):
    if i % 2 == 0:
        list2.append(list1[i])
print(list2)


# Exercise 30
# program to convert multiple numbers from a list into a single number.
print("_" * 50)

list1 = [12, 32, 33, 5, 4, 7, 33]
val = ''
for i in list1:
    val += str(i)
print(val)

# Exercise 31
# program to create a sublist of numbers and their squares from 1 to 10.
print("_" * 50)

# list1 =  [[1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81], [10, 100]]

list1 = [(i, i**2) for i in range(1,11)]

print(list1)

# Exercise 32
# program to create a list of five consecutive numbers in the list.
print("_" * 50)

list1 = [[i+j*5-5 for i in range(1,6)] for j in range(1,5)]

print(list1)

# Exercise 33
# program to insert a given string at the beginning of all items in a list.
print("_" * 50)

list1 = [1,2,3,4,5]
str1 = 'Sqa'
list2 = []
for val in list1:
    char = str1+str(val)
    list2.append(char)
print(list2)

# Exercise 34
# program to iterate over two lists simultaneously and create a list of sublists.
print("_" * 50)

list1 = [1, 3, 5, 7, 9]
list2 = [8, 6, 4, 2, 10]

# Exercise 35
# program to move all positive numbers on the left side and negative numbers on the right side.
print("_" * 50)

list1 = [2, -4, 6, 44, -7, 8, -1, -10]
list2 = []
for val in list1:
    if val > 0:
        list2.insert(0, val)
    else:
        list2.insert(len(list2), val)

print(list2)

# Exercise 36
# program to move all zero digits to the end of a given list of numbers.
print("_" * 50)

list1 = [3, 4, 0, 0, 0, 0, 6, 0, 4, 0, 22, 0, 0, 3, 21, 0]
list2 = []
for val in list1:
    if val != 0:
        list2.insert(0, val)
    else:
        list2.insert(len(list2), val)

print(list2)

# Exercise 37
# program to find the list in a list of lists whose sum of elements is the highest.
print("_" * 50)

list1 = [[11, 2, 3], [4, 15, 6], [10, 11, 12], [7, 8, 19]]

sum_highest = 0

for val1 in list1:
    sum = 0
    for val2 in val1:
        sum += val2
        if sum > sum_highest:
            sum_highest = sum
            list_highest = val1

print(sum_highest)
print(list_highest)

# Exercise 38
# program to count empty dictionaries from the given list.
print("_" * 50)

list1 = [{}, {'a': 'sqatools'}, [], {'a': 123}, {},{},()]
empty_count = 0

for val in list1:
    if val == {}:
        empty_count += 1

print(empty_count)

# Exercise 39
# program to remove consecutive duplicates of given lists.
print("_" * 50)

list1 = [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
print(set(list1))
leng = len(list1)

for i in range(leng):
    if list1[i] == list1[i+1]:
        list1.remove(list1[i])
        leng = len(list1)

print(list1)

# Exercise 40
# program to split a given list into two parts where the length
# of the first part of the list is given.
print("_" * 50)

list1 = [4, 6, 7, 3, 2, 5, 6, 7, 6, 4]
length = 5

list1 = [[list1[i] for i in range(0,length)], [list1[i] for i in range(length,len(list1))]]

print(list1)

# Exercise 41
# program to insert items at a specific position in the list.
print("_" * 50)

list1 = [2, 4, 6, 8, 3, 22]
ind = 3
val = 55
list1[ind] = val
list1.index(list1[ind])

print(list1)

# Exercise 42
# program to select random numbers from the list.
print("_" * 50)

# Exercise 42
#  Python program to create a 3*3 grid with numbers.
print("_" * 50)

list1 = []
for i in range(3):
    list1.append([])
    for j in range(4,7):
        list1[i].append(j)

print(list1)

# Exercise 43
# Python program to zip two lists of lists into a list.
print("_" * 50)
[([1, 3], [2, 4]), ([5, 7], [6, 8]), ([9, 11], [10, 12, 14])]
list1 = [[1, 3], [5, 7], [9, 11]]
list2 = [[2, 4], [6, 8], [10, 12, 14]]
list3 = []
for i in range(len(list1)):
    list3.append((list1[i], list2[i]))

print(list3)

# method 2
list3 = list(zip(list1, list2))
print(list3)

# Exercise 44
# Python program to convert the first and last letter of
# each item from Upper case and lowercase.
print("_" * 50)

list1 = ['Learn', 'python', 'From', 'Sqa', 'tools']
list2 = []
for word in list1:
    list2.append(word[0].swapcase() + word[1:-1] + word[-1].swapcase())

print(list1)
print(list2)

# Exercise 45
# to find maximum and minimum values in the given heterogeneous list.
print("_" * 50)

list1 = ['san',1,2,3,'rach']
list2 = []
for value in list1:
    if isinstance(value, int):
        list2.append(value)

print("Max:", max(list2))
print("Min:", min(list2))

# Exercise 46
# program to sort a given list in ascending order according to the sum of its sublist.
print("_" * 50)

list1 = [[3, 5, 6], [2, 1, 3], [5, 1, 1], [1, 2, 1], [0, 4, 1]]
highest_sum = 0
sum1 = 0

# Exercise 47
# Python program to extract the specified sizes of strings from a given list
# of string values.
print("_" * 50)

list1 = ['Python', 'Sqatools', 'Practice', 'Program', 'test', 'list']
size = 8
list2 = []
for word in list1:
    if len(word) == size:
        list2.append(word)

print(list2)

# Exercise 48
# program to find the difference between consecutive numbers in a given list.
print("_" * 50)

list1 = [1, 1, 3, 4, 4, 5, 6, 7]

list2 = []
for i in range(len(list1)-1):
    diff = abs(list1[i] - list1[i+1])
    list2.append(diff)
print(list2)

# Exercise 49
# Python program to calculate the average of the given list.
print("_" * 50)

list1 = [3, 5, 7, 2, 6, 12, 3]


print("Average :", sum(list1)/len(list1))

# Exercise 50
# program to count integers in a given mixed list.
print("_" * 50)

list1 = [3, 5, 7, 2, 6, 12, 3, 'Hello', 'Sqa']
count = 0

for val in list1:
    if isinstance(val, int):
        count += 1

print(count)

# Exercise 51
# program to access multiple elements of the specified index from a given list.
print("_" * 50)

list1 = [2, 3, 4, 7, 8, 1, 5, 6, 2, 1, 8, 2]
Index_list = [0, 3, 5, 6]
list2 = []

for val in Index_list:
    list2.append(list1[val])

print(list2)

# Exercise 52
# Python program to check whether a specified list is sorted or not.
print("_" * 50)

list1 = [1, 2, 3, 5, 7, 8, 9]
list3 = sorted(list1)
if list1 == list3:
    print("Sorted")
else:
    print("Not Sorted")
#############################################
list1 = [3, 5, 1, 6, 8, 2, 4]
list3 = sorted(list1)
if list1 == list3:
    print("Sorted")
else:
    print("Not Sorted")

# Exercise 53
# Python program to remove duplicate dictionaries from a given list.
print("_" * 50)

list1 = [{'name': 'john'}, {'city': 'mumbai'}, {'Python': 'laguage'}, {'name': 'john'}]
list2 = []
for val in list1:
    if list1.count(val) <= 1:
        list2.append(val)

print(list2)

# Exercise 54
# Python program to check if the elements of a given list are unique or not.
print("_" * 50)
count = 1

list1 = [2, 5, 6, 7, 4, 11, 66, 21, 22, 3]
list2 = []
for val in list1:
    if list1.count(val) > 1:
        count = 0
        break

if count == 1:
    print("Unique")
else:
    print("Not Unique")

# Exercise 55
# program to remove duplicate sublists from the list.
print("_" * 50)
count = 1

list1 = [[1, 2], [3, 5], [1, 2], [6, 7]]
list2 = []
for val in list1:
    if list1.count(val) == 1:
        list2.append(val)

print(list2)

# Exercise 56
# Python program to create a list by taking an alternate item from the list.
print("_" * 50)
count = 1

list1 = [3, 5, 7, 8, 2, 9, 3, 5, 11]
list2 = []

for i in range(len(list1)):
    if i % 2 == 0:
        list2.append(list1[i])

print(list2)

# Exercise 57
# program to remove duplicate tuples from the list.
print("_" * 50)
count = 1

list1 = [(2, 3), (4, 6), (5, 1), (2, 3), (7, 9), (5, 1)]
list2 = []
for val in list1:
    if list2.count(val) < 1:
        list2.append(val)

print(list2)

# Exercise 58
# Python program to insert an element before each element of a list.
print("_" * 50)
count = 1

list1 = [3, 5, 7, 8, 9]
list2 = []
ele = 'San'

for i in range(0,len(list1)*2,2):
    list1.insert(i, ele)

print(list1)

# Exercise 59
# program to remove the duplicate string from the list.
print("_" * 50)
count = 1

list1 = ['python', 'is', 'a', 'best', 'language', 'python', 'best']
list2 = []
for val in list1:
    if list2.count(val) < 1:
        list2.append(val)

print(list2)

# Exercise 60
# program to get the factorial of each item in the list.
print("_" * 50)


list1 = [1, 2, 3, 4]
list2 = []
for val in list1:
    fact = 1
    for i in range(1, val+1):
        fact = fact * i
    list2.append(fact)

print(list2)

# Exercise 61
# program to get a list of Fibonacci numbers from 1 to 20.
print("_" * 50)

list1 = []
temp = 0
f0 = f2 = 0
f1 = 1
for val in range(0,20):
    list1.append(f0)
    f2 = f0 + f1
    f0 = f1
    f1 = f2
    print(list1)

# Exercise 62
# Python program to reverse all the numbers in a given list.
print("_" * 50)

list1 = [123, 145, 633, 654, 254]
list2 = []
for val in list1:
    str_rev = str(val)
    str_rev = str_rev[::-1]
    str_rev = int(str_rev)
    list2.append(str_rev)

print(list2)

# Exercise 63
# Python program to get palindrome numbers from a given list.
print("_" * 50)

list1 = [121, 134, 354, 383, 892, 232]
list2 = []
for val in list1:
    str_rev = str(val)
    str_rev = str_rev[::-1]
    str_rev = int(str_rev)
    if val == str_rev:
        list2.append(str_rev)

print(list2)

# Exercise 64
# program to get a count of vowels in the given list.
print("_" * 50)
count = 0

list1 = ['Learning', 'Python', 'From', 'SqaTool']
vowels = 'aeiouAEIOU'
for word in list1:
    for char in word:
        if char in vowels:
            count += 1

print(count)

# Exercise 65
# program to get the list of prime numbers in a given list.
print("_" * 50)

list1 = [11, 8, 7, 19, 6, 29]
list2 = []

for val in list1:
    count = 0
    for i in range(1, val//2):
        if val % i == 0 :
            count += 1
    if count == 1:
        print("Prime", val)
        list2.append(val)
    else:
        print("Not Prime", val)

print(list2)

# Exercise 66
# program to get a list with n elements removed from the left and right.
print("_" * 50)

list1 = [2, 5, 7, 9, 3, 4]

print("Remove 1 element from left", list1[1:])
print("Remove 1 element from right", list1[0:-1])
print("Remove 1 element from left", list1[2:])
print("Remove 1 element from right", list1[0:-2])


# Exercise 67
# program to create a dictionary with two lists.
print("_" * 50)

list1 = ['a', 'b', 'c', 'd', 'e']
list2 = [234, 123, 456, 343, 223]

temp = dict(zip(list1, list2))

print(temp)

# Exercise 68
# Python program to remove the duplicate item from the list using set.
print("_" * 50)

list1 = [2, 5, 7, 8, 2, 3, 4, 12, 5, 6]

list2 = set(list1)

print(list2)


# Exercise 69
# Python program to calculate the bill per fruit purchased from a given fruits list.
print("_" * 50)

fruit_list_Price = [['apple', 30], ['mango', 50], ['banana', 20], ['lichi', 50]]
fruit_quantity = [['apple', 2], ['mango', 10]]

for fruit, quantity in fruit_quantity:
    for fruit1, price in fruit_list_Price:
        if fruit == fruit1:
            print("Fruit :", fruit, '\n', "Bill :", quantity*price)


# Exercise 70
# Python program to calculate the bill per fruit purchased from a given fruits list.
print("_" * 50)

fruit_list_Price = [['apple', 30], ['mango', 50], ['banana', 20], ['lichi', 50]]
fruit_quantity = [['apple', 2], ['mango', 10]]

for fruit, quantity in fruit_quantity:
    for fruit1, price in fruit_list_Price:
        if fruit == fruit1:
            print("Fruit :", fruit, '\n', "Bill :", quantity*price)


# Exercise 71
# program to flatten a given nested list structure.
print("_" * 50)

list1 = [0, 12, [22, 32], 42, 52, [62, 72, 82], [92, 102, 112, 122]]
list2 = []
for word in list1:
    if type(word) is list:
        for key in word:
            list2.append(key)
    else:
        list2.append(word)

print(list2)

# Exercise 72
# Python program to convert tuples in the list into a sublist.
print("_" * 50)

list1 = [(3, 5), (6, 8), (8, 11), (12, 14), (17, 23)]
list2 = []
for word in list1:
    if type(word) is tuple:
        word = list(word)
        list2.append(word)
    else:
        list2.append(word)

print(list2)

# Exercise 73
# Python program to create a dictionary from a sublist in a given list.
print("_" * 50)

list1 = [['a', 5], ['b', 8], ['c', 11], ['d', 14], ['e', 23]]
list2 = []
list3 = []
for i, j in list1:
    list2.append(i)
    list3.append(j)

list4 = dict(zip(list2, list3)) # zip converts 2 lists to one dict
print(list4)


# Exercise 74
# program to replace ‘Java’ with ‘Python’ from the given list.
print("_" * 50)

list1 = ['Hello', 'student', 'are', 'learning', 'Java', 'Its', 'Java', 'Language']

# Exercise 75
# program to convert the 3rd character of each word to a capital
# case from the given list.
print("_" * 50)

list1 = ['Hello', 'student', 'are', 'learning', 'Java', 'Its', 'Java', 'Language']
list2 = []
for word in list1:
    if len(word) > 3:
        word = (word[0:3] + word[3].upper() + word[4:])
    list2.append(word)

print(list2)

# Exercise 76
# Python program to remove the 2nd character of
# each word from a given list.
print("_" * 50)

list1 = ['Hello', 'student', 'are', 'learning', 'is', 'Java', 'Its', 'Java', 'Language']
list2 = []
for word in list1:
    word = (word[0:1] + word[2:])
    list2.append(word)

print(list2)

# Exercise 77
# program to get a length of each word and add it as a dictionary
# from the given list.
print("_" * 50)

list1 = ['Hello', 'student', 'are', 'learning', 'is', 'Java', 'Its', 'Java', 'Language']
list2 = []
for word in list1:
    list2.append(len(word))

list3 = dict(zip(list1, list2))
print([list3])

# Exercise 78
# program to get a length of each word and add it as a dictionary
# from the given list.
print("_" * 50)

list1 = [{'Hello':5}, {'student': 7}, {'are': 3}, {'learning': 8}, {'Hello':5}, {'Language': 8}, {'are': 3}]
dict1 = {}
list2 = []
for word in list1:
    if word not in list2:
        list2.append(word)

print(list2)



# Exercise 79
# [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
print("_" * 50)

list1 = [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
sum = 0

for val in list1:
    round(val)
    sum += int(val)

print(sum)












