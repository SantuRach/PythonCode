'''

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
# shallow copy : consider we have two lists list_a and list_b, if we will assign list_a to list_b
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
'''

# Exercise 31
# program to create a sublist of numbers and their squares from 1 to 10.
print("_" * 50)

list1 =  [[1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81], [10, 100]]







