################################## Conditional statements ###############################

''''''''''''''' Syntax''''''''''''''''''''''''''''''

for inp in range (start_value;start_value:difference):
    Code1

'''

#  program to print reverse
print("_" * 50)
for i in range(10, 5, -1):
    print(i)


# Example 1
# program to find those numbers which are divisible by 7 and multiple of 5,
# between 1500 and 2700 (both included).
print("_" * 50)

for i in range(1500, 2700, 1):
    if (i % 7 == 0 and i % 5 == 0):
        print(i)

# Example 2
# program to construct the following pattern, using a nested for loops.
# *
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *
print("_" * 50)
str1 = '*'
for i in range(0, 5, 1):
    print(str1 * i)
for j in range(5, 0, -1):
    print(str1 * j)

# Example 3
# Write a program to get the Fibonacci series between 0 to 20 using python.
print("_" * 50)

inp1 = 0
inp2 = 1

for i in range(0, 20, 1):
    print(inp1)
    inp3 = inp1 + inp2
    inp1 = inp2
    inp2 = inp3

# Example 4
# program that accepts a word from the user and converts
# all uppercases in the word to lowercase
print("_" * 50)

inp1 = "SANds"
if inp1.isupper():
    print(inp1.lower())
else:
    print(inp1.lower())

# Example 5
# program that accepts a string and calculates the number
# of digits and letters using python.
print("_" * 50)

str1 = "python12348"
alpha = numeric = 0

for i in str1:
    if i.isalpha():
        alpha += 1
    elif i.isnumeric():
        numeric += 1
    else:
        print("Invalid")

print(alpha)
print(numeric)

# Example 6
# Python for loop program to print the alphabet pattern ‘O’

print("_" * 50)
str1 = "*"

print("  ", str1 * 3, end="\n")
for j in range(5):
    print(str1, "     ", str1)
print("  ", str1 * 3, end="")
print("\n")

# Example 7
# print all natural numbers in reverse (from n to 1)
print("_" * 50)

n = 10
#n = int(input("Enter number: "))

for j in range(n, 0, -1):
    print(j, end=" ")
print("\n")

# Example 8
# count the number of digits in a number
print("_" * 50)

n = '123456789123456789123456789123456789'
#n = int(input("Enter number: "))
count = 0

for j in n:
    count += 1
print(count)

# Example 9
# calculate the sum of digits of a number using python
print("_" * 50)

num1 = 123456
#n = int(input("Enter number: "))
count = 0
last_digit = last_digit1 = 0

print(num1)

for j in n:
    last_digit = num1 % 10
    last_digit1 = last_digit1 + last_digit
    num1 = int(num1 / 10)

print(last_digit1)

# Example 10
# program to enter a number and print its reverse using python
print("_" * 50)

num1 = 123456
#n = int(input("Enter number: "))
count = 0
last_digit = last_digit1 = 0

print(num1)

for j in n:
    if num1 != 0:
        last_digit = num1 % 10
        print(last_digit, end="")
        #       last_digit1 = last_digit1 + last_digit
        num1 = int(num1 / 10)

# Example 11
# program to print all natural numbers in reverse (from n to 1)
# using a while loop in python.
print("_" * 50)

num1 = 99
#n = int(input("Enter number: "))
count = 0
last_digit = last_digit1 = 0

while num1 >= 1:
    print(num1)
    num1 -= 1

# Example 12
# frequency of each digit in a number.
print("_" * 50)

num10 = 1356565656555
#n = int(input("Enter number: "))
num9 = str(num10)
count = 0

for i in num9:
    if i == '5':
        count += 1

print(count)

# Example 13
# numbers into words
print("_" * 50)

num101 = 1234567809
#print(num10, type(num10))
# n = int(input("Enter number: "))
num9 = str(num101)
str1 = ""

for i in num9:
    if i == '1':
        print("One", end=" ")
    elif i == '2':
        print("Two", end=" ")
    elif i == '3':
        print("Three", end=" ")
    elif i == '4':
        print("Four", end=" ")
    elif i == '5':
        print("Five", end=" ")
    elif i == '6':
        print("Six", end=" ")
    elif i == '7':
        print("Seven", end=" ")
    elif i == '8':
        print("Eight", end=" ")
    elif i == '9':
        print("Nine", end=" ")
    elif i == '0':
        print("Zero", end=" ")

# Example 14
# Python loops program to find the power of a number using Python
# for loop. Take values as an input base number and power, and get
# the total value using a loop.
print("\n")
print("_" * 50)

base1 = 2
power1 = 5
result = 1

for i in range(power1):
    result *= base1
print(result)

# Example 15
# program to calculate the factorial of a number using Python Loops.
print("_" * 50)

num10 = 10
#n = int(input("Enter number: "))
result = 1

for i in range(1, num10, 1):
    result *= i

print(result)


# Example 16
# program to print all Prime numbers between 1 to n using Python Loops.
print("_" * 50)

num1 = 11
#n = int(input("Enter number: "))
count = 0

for i in range(1, num1+1):
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
        if i == j == 1:
            print(i)

    if count == 2:
        print(i)
    count = 0



# Example 17
# program to check whether a number is an Armstrong number
print("_" * 50)

num10 = 153
#n = int(input("Enter number: "))
num9 = str(num10)
total = 0

for i in num9:
    total = total + int(i)**3

if total == num10:
    print("Armstrong")
else:
    print("Not Armstrong")


# Example 18
#  Python loops program to print all Perfect numbers between 1 to n
print("_" * 50)

num10 = 28
# n = int(input("Enter number: "))
total = 0

for i in range(1, num10, 1):
    if num10 % int(i) == 0:
        total += int(i)
        print(i)

if total == num10:
    print("Perfect")
else:
    print("Not Perfect")

# Example 19
#  print the multiplication table of any number using Python Loops
print("_" * 50)

num10 = 9
# n = int(input("Enter number: "))

for i in range(1, 11, 1):
        print(num10,'*',i,"=",num10*i)


# Example 20
#  Python loops program to print the pattern T using Python Loops
print("_" * 50)

num10 = '*'
# n = int(input("Enter number: "))

for i in range(1, 3, 1):
        print(num10*9)
for i in range(1, 6, 1):
        print("  ",num10*3)

# Example 21
#  Write a program to get input from the user if it is a number insert it into an empty
#  list using Write a program to get input from the user if it is a number
#  insert it into an empty list using
print("_" * 50)

# n = int(input("Enter number: "))
input = '125python'
list1 = []

for i in input:
        print(i)
        if i.isnumeric():
            list1.append(int(i))
print(list1)

# Example 22
#  apply loop on list
print("_" * 50)

list1 = [11,55,54,56,44,99,564]

for element in list1:
    print(element)

# Example 23
#  apply loop on list to print in reverse
print("_" * 50)
list1 = [11, 55, 54, 56, 44, 99, 564]

leng = int(len(list1))

for element in range(-1,-leng-1,-1):
    print(list1[element])

# Example 24
#  Apply loop on string values
print("_" * 50)
str1 = 'python programming'

for char in str1:
    print(char)

# Example 25
#  Apply loop on string values - reverse
print("_" * 50)
str1 = 'python programming'
leng = len(str1)
print(leng)
for char in range(-1, -leng-1,-1):
    print(str1[char], end="")

# Example 26
#  apply loop on dictionary
print("_" * 50)
dict1 = {'Name': 'Santosh', 'Surname': 'Rachotimath', 'Age': 36}

for key in dict1:
    print(key)

# Example 27
#  apply loop on dictionary using function item to print in tuple format
print("_" * 50)
dict1 = {'Name': 'Santosh', 'Surname': 'Rachotimath', 'Age': 36}

for key in dict1.items():
    print(key)

# Example 28
#  apply loop on dictionary
print("_" * 50)
dict1 = {'Name': 'Santosh', 'Surname': 'Rachotimath', 'Age': 36}
keys = dict1.values()
#for key in dict1:
print(keys)

# Example 29
#  apply loop on dictionary tp print both key and Values
print("_" * 50)
dict1 = {'Name': 'Santosh', 'Surname': 'Rachotimath', 'Age': 36}
for key1, value1 in dict1.items():
    print(key1, value1)

# Example 30
#  apply loop on dictionary
print("_" * 50)
dict1 = {
    'Teaching':
        {
            'Maths': ['M1', 'M2', 'M3'],
            'English': ['E1', 'E2', 'E3'],
            'Hindi': ['H1', 'H2', 'H3']
        },
    'Accounts':
        {
            'Acc1': [123, 456, 789],
            'Acc2': [147, 258, 369],
            'Acc3': [321, 654, 987]
        },
    'Student':
        {
            'Class8': ['8A', '8B', '8C'],
            'Class9': ['9A', '9B', '9C'],
            'Class10': ['10A', '10B', '10C'],
        }
}
print("=" * 40)
for key1, value1 in dict1.items():
    print("Department: ", key1)
    for key2, value2  in value1.items():
        print("Department", key1, "has: ", key2)
        for key3 in value2:
            print(key2," has: ", key3)
    print("=" * 40)

# Example 31
#  program to get input from the user if it is a string insert it into an empty list
print("_" * 50)
str1 = '123santosh546'
list1 = []
for key in str1:
    if key.isalpha():
        list1.append(key)
print(list1)


# Example 31
#  program to get input from the user if it is a string insert it into an empty list
print("_" * 50)
str1 = '123santosh546'
list1 = []
for key in str1:
    if key.isalpha():
        list1.append(key)
print(list1)


# Example 32
#  program to get the Fibonacci series between 0 to 10 using Python Loops.
print("_" * 50)
fibo_0 = 0
fibo_final = 0
fibo_1 = 1
fibo_num = 10
print(fibo_0,fibo_1, end=" ")
for fibo_num in range(9):
    fibo_final = fibo_0 + fibo_1
    fibo_0 = fibo_1
    fibo_1 = fibo_final
    print(fibo_final, end=" ")


# Example 33
#  program to check the validity of password input by users using Python Loops.
print("_" * 50)
upper = lower = num = special = count = 0
password1 = '$AN526456gyu5u0'
list1 = ['$','#','@']
for char in password1:
    count += 1
    if char.isalpha():
        if char.isupper():
            upper = 1
        else:
            lower = 1
    elif char.isnumeric():
        num = 1
    elif char in list1:
        special = 1
    else:
        continue

if upper == lower == num == special == 1 and count >= 5 and count <= 15:
    print("Valid password")
else:
    print("InValid password")


# Example 33
#  program to print the values of the keys of a dictionary using Python
print("_" * 50)
dict1 = {'Name': 'Virat', 'Sports': 'Cricket', 'DOC': 28081989}
for i, j in dict1.items():
    print(j)

#  program to program to print the keys and values of a dictionary using Python Loops
print("_" * 50)
dict1 = {'Name': 'Virat', 'Sports': 'Cricket', 'DOC': 28081989}
for i, j in dict1.items():
    print(i,j)


# Example 33
#  sum of the first 10 natural numbers using the while loop
print("_" * 50)
num1 = 11
start = sum1 = 0

while start < num1:
    sum1 += start
    start += 1

print(sum1)

# Example 34
#  program to print the days in a week except Sunday using a while loop in Python.
print("_" * 50)
for num in range(1,10):
    if(num == 6):
        break
    print(num)
