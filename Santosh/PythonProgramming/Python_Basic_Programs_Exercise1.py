import math
from datetime import datetime
from datetime import date

# Python program to repeat a given string 5 times.
print("_" * 100)
print("### Python program to repeat a given string 5 times.")
s = "SQA_tools "
print(s*5)

# Python program to get the Average of given numbers.
print("_" * 100)
print("### Python program to repeat a given string 5 times.")
a = 40
b = 50
c = 30
print("Average of a,b,c is :", (a+b+c)/3)

# Program to get the median of given numbers.
print("_" * 100)
print("### Python Program to get the median of given numbers.")
list1 = [19, 60, 61, 66, 4, 3]
list1.sort()
temp = (len(list1))/2
print(temp)
print("Median of list1 is :",list1[int(temp)])

# Python program to print the square and cube of a given number.
print("_" * 100)
print("### Python program to print the square and cube of a given number.")
a = 9
print("Square of a is :", a**2)
print("Cube of a is :", a**3)

# Python program to interchange values between variables.
print("_" * 100)
print("### Python program to interchange values between variables.")
a = 10
b = 20

c = a
a = b
b = c
""" Better logic could be ,
a, b = b, a 
"""
print("a is :", a)
print("b is :", b)

# Python program to solve this Pythagoras theorem.
print("_" * 100)
print("### Python program to solve this Pythagoras theorem.")
a = 3
b = 4
c = 5
"""
a = a**2
b = b**2
c = c**2
LHS = a+b
RHS = c
print("Pythagoras theorem is :", LHS == RHS)
"""
c = a**2 + b**2
print("Pythagoras theorem is :", math.sqrt(c))


# Python program to calculate the area of a circle.
print("_" * 100)
print("### Python program to calculate the area of a circle.")
Pi = 3.14
radius = 4

print("Area of a circle is :", Pi*radius**2)


# Python program to check whether the given number is an Armstrong number or not.
print("_" * 100)
print("### Python program to check whether the given number is an Armstrong number or not.")
x = num = 153
rev = 0
# rem = 0

while x>0:
    rem = x % 10
    rev = rev + rem**3
    x = x//10

if rev == num:
        print("Number is an Armstrong.")

else:
        print("Number is an not Armstrong.")

# Python program to print the current date in the given format
print("_" * 100)
print("### Python program to print the current date in the given format")

date = date.today()
print("Today date is ", date.strftime("%Y %b %d"))

"""
# Python program to calculate days between 2 dates
print("_" * 100)
print("### Python program to print the current date in the given format")

date_1 = date(2023, 1, 5)
date_2 = date(2023, 1, 22)
result = (date_2-date_1).days
print("Difference is ", result, "days")
"""

# Python program to get the factorial of the given number.
print("_" * 100)
print("### Python program to get the factorial of the given number.")
x = rem = num = 10
y = 1
# rem = 0

while x>1:

    y = rem * (x-1)
    rem = y
    x = x-1

print("Factorial of",num ,"is", y)


# Python program to get the Fibonacci series between 0 to 50.
print("_" * 100)
print("### Python program to get the Fibonacci series between 0 to 50.")
num = 50
var1 = 0
var2 = 1
var3 = 0
count = 0
print("Fibonacci series between 0 to 50 is: ", var1, var2)
#print("Fibonacci series between 0 to 50 is: ", var2)

while var3 < 50:
    if count != 0:
         print(var3)
    var3 = var1 + var2
    var1 = var2
    var2 = var3
    count = 1

# Python program to find the square root of a number.
print("_" * 100)
print("### Python program to find the square root of a number.")
x = num = 25
y = math.sqrt(x)
print(y)


# Python program to check leap year.
print("_" * 100)
print("### Python program to check leap year.")
num = 2024
rem = num % 4
if rem == 0:
        print("Leap year")
else:
        print("Not leap year")