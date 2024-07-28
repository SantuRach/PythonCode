################################## Conditional statements ###############################

''''''''''''''' Syntax''''''''''''''''''''''''''''''

if (condition):
    Code1
else:
    Code2
'''
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
'''
