# Python program to repeat a given string 5 times.
import math

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

# Python program to solve this Pythagorous theorem.
print("_" * 100)
print("### Python program to solve this Pythagorous theorem.")
a = 3
b = 4
c = 5
"""
a = a**2
b = b**2
c = c**2
LHS = a+b
RHS = c
print("Pythagorous theorem is :", LHS == RHS)
"""
c = a**2 + b**2
print("Pythagorous theorem is :", math.sqrt(c))