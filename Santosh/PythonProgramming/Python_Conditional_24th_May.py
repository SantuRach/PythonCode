################################## Conditional statements ###############################

''''''''''''''' Syntax''''''''''''''''''''''''''''''

if (condition):
    Code1
else:
    Code2
'''


# Example 1
print("_" * 50)
a = 10
b = 10
if (a==b):
    print("a and b are same")
else:
    print("a and b are not same")

# Example 2
print("_" * 50)
a = 10
b = 3
if (a%b == 0):
    print("a is divisible by b")
else:
    print("a is not divisible by b")

# Example 3 Even or Odd- Input function
print("_" * 50)
#int is important else it will consider input as string
a = int(input("Enter value of a:"))
print(a, type(a))
if (a%2 == 0):
    print("Even", type(a))
else:
    print("Odd", type(a))

# Example 3 to check number divisible by 3 & 7
a = int(input("Enter value of a:"))

if (a%3 == 0 and a%7 == 0):
    print("Number is divisible by 3 & 7")
else:
    print("Number is not divisible by 3 & 7")


# Exercise 1
# If else program to get all the numbers divided by 3 from 1 to 30.
print("_" * 50)
a = 1

for a in range (1,31):
    if(a%3 == 0):
        print(a)

# Exercise 2
# If else program to assign grades as per total marks.

#    marks > 40: Fail
#    marks 40 – 50: grade C
#    marks 51 – 60: grade B
#    marks 61 – 70: grade A
#    marks 71 – 80: grade A+
#    marks 81 – 90: grade A++
#    marks 91 – 100: grade Excellent
#    marks > 100: Invalid marks

print("_" * 50)
marks = int(input("Enter marks :"))

if(marks < 40):
        print("Fail")
elif(marks >= 40 and marks <=50):
    print("grade C")
elif(marks > 50 and marks <=60):
    print("grade B")
elif(marks > 60 and marks <=70):
    print("grade A")
elif(marks > 70 and marks <=80):
    print("grade A+")
elif(marks > 80 and marks <=90):
    print("grade A++")
elif(marks > 90 and marks <=100):
    print("grade Excellent")
else:
    print("Invalid marks")

# Exercise 3
# program to print the square of the number if it is divided by 11.
print("_" * 50)
num1 = int(input("Enter number :"))

if(num1 % 11 == 0):
        print("Square of number num1 is:", num1**2)


# Exercise 4
# program to check given number is a prime number or not.
print("_" * 50)
num1 = int(input("Enter number :"))
temp = num1
for num1 in range (2,num1+1):
    if(temp % num1 == 0):
        if(num1 == temp):
            print("Prime")
        else:
            print("Not prime")
            exit()


# Exercise 5
# program to check number is part of the Fibonacci series from 1 to 10.
print("_" * 50)
fib = [0,1,1,2,3,5,8,13,21,34]
inp = int(input("Enter number: "))
#   if inp in fib:
#       print("Present in Fibo series")
#   else:
#       print("Not Present in Fibo series")

count = 0
for num1 in range (0,10):
    if fib[num1] == inp:
        count = 1

if count == 1:
    print("Present in Fibo series")
else:
    print("Not Present in Fibo series")



# Exercise 6
# Python nested If else program to describe the interview process
print("_" * 50)
round1 = input("Enter round1 result: ")
round2 = input("Enter round2 result: ")

if round1 == 'passed':
    if round2 == 'passed':
        print("Placed")
    else:
        print("Not Placed")
else:
    print("Not Placed")

# Exercise 7
# Python program to find the largest number among three numbers.
print("_" * 50)
num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
if num1 > num2:
    if num1 > num3:
        print("num1 is greatest")
    else:
        print("num3 is greatest")
else:
    if num2 > num3:
        print("num2 is greatest")
    else:
        print("num3 is greatest")


# Exercise 8
# program to check any person eligible to vote or not
print("_" * 50)
num1 = int(input("Enter age: "))

if num1 >= 18:
        print("Eligible")
else:
        print("Not Eligible")

# Exercise 9
# program to check whether a number is palindrome.
print("_" * 50)
num1 = int(input("Enter number: "))
num2 = str(num1)

if num1 == int(num2[::-1]):
        print("Palindrome")
else:
        print("Not Palindrome")

# program to check whether a string is palindrome.
print("_" * 50)
num1 = input("Enter string: ")

if num1 == num1[::-1]:
        print("Palindrome")
else:
        print("Not Palindrome")


# Exercise 10
# program to check whether a given character is uppercase or not.
print("_" * 50)
num1 = input("Enter string: ")

if num1.isupper():
        print("Capital")
else:
        print("Not Capital")


# Exercise 11
# program to check whether the given number is an integer or not.
print("_" * 50)
num1 = input("Enter number: ")
num1 = int(num1)

if (type(num1) == int):
        print("Integer")
else:
        print("Not Integer")


# Exercise 12
# program to print all the numbers from 10-15 except 13
print("_" * 50)
for num8 in range(10, 15):
    if num8 != 13:
        print(num8, end="-")


# Exercise 12
# Python program to find the electricity bill. According to the following conditions:
# Up to 50 units rs 0.50/unit
# Up to 100 units rs 0.75/unit
# Up to 250 units rs 1.25/unit
# above 250 rs 1.50/unit
# an additional surcharge of 17% is added to the bill
print("_" * 50)
inp_unit = 350
inp1 = inp2 = inp3 = inp4 = 0
for num8 in range(0, inp_unit+1):
    if num8 <= 50:
        inp1 = num8*0.5
    elif num8 <= 100:
        inp2 = ((num8-50) * 0.75)
    elif num8 <= 250:
        inp3 = ((num8-100) * 1.25)
    else:
        inp4 = ((num8-250) * 1.5)

print((inp1+inp2+inp3+inp4)*1.17)


# Exercise 13
# Python program to check whether the input number if a multiple of two print “Fizz”
# instead of the number and for the multiples of three print “Buzz”. For numbers that are
# multiples of both two and three print “FizzBuzz”.
print("_" * 50)
num1 = 6

if num1 % 2 == 0 or num1 % 3 == 0:
    if num1 % 2 == 0:
        if num1 % 3 == 0:
            print("FizzBuzz")
        else:
            print("Fizz")
    else:
            print("Buzz")
            


# Exercise 14
# Program to check whether an alphabet is a vowel
print("_" * 50)
vowel = ['a','e','i','o','u']
inp1 = 'i'

if inp1 in vowel:
    print("Vowel")
else:
    print("Not Vowel")


# Exercise 15
# Python program to check whether the input number is a float or not
# if yes then round up the number to 2 decimal
print("_" * 50)

inp1 = 25.36554478

if type(inp1) == float:
    print(round(inp1,2))
else:
    print("Not float")

# Exercise 16
# program to check whether the given input is a complex type or not.
print("_" * 50)

inp1 = 5+6

if type(inp1) == complex:
    print("True")
else:
    print("False")


# Exercise 17
# Python program to print the absolute value of a number defined by the user.
print("_" * 50)

inp1 = 665
print(abs(inp1))

# Exercise 18
# Python program to check whether the last digit of a number
# defined by the user is divisible by 4 or not.
print("_" * 50)

inp1 = 58
rem = inp1%10
if rem%4 == 0:
    print("Divisible by 4")
else:
    print("Not Divisible by 4")