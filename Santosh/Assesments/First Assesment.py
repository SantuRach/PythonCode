'''
1. Write a python python program to calculate sum of all the numbers in the string.
str1= "Good 12 Morning 45 , Hope 2 you are 30 doing good"
output = 89"""

2. Write a python Program to convert first and last character to upper case.
str1= "python programming is very easy to learn"
output = "PythoN ProgramminG IS VerY EasY TO LearN"


3. Write a Python Program to find out prime number from give list of values
list1 = [13, 56, 77, 23, 29, 11]
output = [13, 23, 29, 11]

4. Write a python program to create below output dictionary with given string.
str1 = "India is best cricket teams"
output = {5: "IndiA", 2: "IS", 4: "BesT", 7:"CrickeT", 5: "TeamS"}
'''

# 1. Write a python python program to calculate sum of all the numbers in the string.
# str1= "Good 12 Morning 45 , Hope 2 you are 30 doing good"
# output = 89"""
print("-"*50)
str1= "Good 12 Morning 45 , Hope 2 you are 30 doing good"
sum = 0

list1 = str1.split(" ")

for word in list1:
    if word.isdigit():
        sum += int(word)
print(sum)

# Write a python Program to convert first and last character to upper case.
# str1= "python programming is very easy to learn"
# output = "PythoN ProgramminG IS VerY EasY TO LearN"
print("-"*50)

str1= "python programming is very easy to learn"

list1 = str1.split(" ")
list2 = []
output = ''

for word in list1:
   word = word[0].upper()+word[1:-1]+word[-1].upper()
   output += ' ' + word

print(output)

# 3. Write a Python Program to find out prime number from give list of values
# list1 = [13, 56, 77, 23, 29, 11]
# output = [13, 23, 29, 11]
print("-"*50)

list1 = [13, 56, 77, 23, 29, 11]
count = 0
output = []
for val in list1:
    for i in range(2, val-2):
        if val % i == 0:
            count = 1
    if count == 0:
        output.append(val)
    else:
        count = 0

print(output)

# 4. Write a python program to create below output dictionary with given string.
# str1 = "India is best cricket teams"
# output = {5: "IndiA", 2: "IS", 4: "BesT", 7:"CrickeT", 5: "TeamS"}
print("-"*50)

str1 = "India is best cricket teams"
list1 = str1.split(" ")
list15 = []
list10 = []
for word in list1:
    list10.append(len(word))
    word = word[0].upper()+word[1:-1]+word[-1].upper()
    list15.append(word)

dict1 = dict(zip(list10, list15))
print(dict1)





















