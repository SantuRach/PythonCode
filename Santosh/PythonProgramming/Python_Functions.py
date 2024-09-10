

"""
################################# Python Functions #################################

function concept
1. function can be defined without any parameter.
2. With out calling the function, code will not execute.
3. We can assign value to Function with parameter with 2 ways
   - Pass by value  e.g. addition(40, 50)
   - Pass by reference  e.g. addition(x, y)
4. Function parameter can have default value.
   - If param has default, then no need to pass value while calling function.
   - If New value has assign to default param while calling function,
     then default value will be overwrite.
   - If One function has two params one is default param and second non default param
     then default params always follows the non default params

"""

#  Syntax
"""
def addition():
    num1 = 10
    num2 = 20
    num3 = num1 + num2
    print('Sum : ', num3)

addition()
"""

########################### Function call ###########################
print('_' * 50)


def addition():
    num1 = 10
    num2 = 20
    num3 = num1 + num2
    print('Sum : ', num3)


addition()
addition()
addition()
addition()

########################### Pass by values ###########################
print('_' * 50)


def addition_values(num1, num2):
    num3 = num1 + num2
    print(num3)


addition_values(10, 200)
addition_values(11, 200)
addition_values(12, 300)
addition_values(13, 201)

########################### Pass by reference ###########################
print('_' * 50)


def addition_values(num1, num2):
    num3 = num1 + num2
    print(num3)


x = 10
y = 12
a = 22
b = 10
addition_values(x, y)
addition_values(a, b)

########################### Pass by default ###########################
print('_' * 50)


def prod_values(num1=5, num2=9):
    num3 = num1 * num2
    print('Product is:', num3)


prod_values(10, 10)
prod_values(10)
prod_values()
prod_values(num2=6, num1=9)


###############################
##### * args : args parameter accept the n number values and can be consider.

def function_c(a1, a2, b3, b4, b5):
    print("multiply :", a1 * a2 * b3 * b4 * b5)


# function_c(5, 7, 8, 2)
# TypeError: function_c() missing 1 required positional argument: 'b5'

# function_c(4, 7, 2, 8, 1, 14, 56)
# TypeError: function_c() takes 5 positional arguments but 7 were given

print("_" * 50)


def function_d(*args):
    print(args)
    # print("addition  of values :", sum(args))
    for val in args:
        print(val)


# function_d(5, 6)
function_d(15, 16, 12)
print("_" * 50)
function_d(12, 26, 35, 67)
print("_" * 50)
function_d(4.5, (4, 5, 6), 'Python', [3, 6, 1, 2], {'a': 123, 'b': 345})
print("_" * 50)


def args_multiply(*keerthi):
    mul_val = 1
    for val in keerthi:
        mul_val = mul_val * val

    print("output :", mul_val)


args_multiply(4, 5)
args_multiply(12, 26, 35)
args_multiply(12, 26, 35, 11, 22)

print("_" * 50)


#################################
# use of **kwargs : This parameter accepts the values in the key value pair

def get_user_details(**kwargs):
    print("kwargs :", kwargs)

    for key, val in kwargs.items():
        print(key, ":", val)


get_user_details(username='Rahul', email='rahul@gmail.com', phone=534543543, address="Mumbai")

print("_" * 50)


def get_user_details_numbers(*args, **kwargs):
    print(args)
    print("kwargs :", kwargs)

    for key, val in kwargs.items():
        print(key, ":", val)


get_user_details_numbers(5, 6, 22, 77, 12, name="Chetan", lastname="karu", phone=3543534534, email='chetan@gmail.com')

print("_" * 50)


############### Return statement in function #########
# return statement : return statement provide functionality to the function to return
#                     any value that can store in any variable


def addition_data(v1, v2):
    return v1 + v2


output = addition_data(40, 50)
print("addition :", output)


# write a python function to add first two variables and multiply by third variable
def multiplication_data(v1, v2, v3):
    output = addition_data(v1, v2)
    return output * v3


#print("Good morning")

def divide_data(n1, n2):
    return n1 / n2


result = multiplication_data(5, 6, 7)
print("result :", result)

divide_result = divide_data(result, 5)
print("Divide result :", divide_result)

print("_" * 50)


# return statement with multiple return values
def math_operation(v1, v2, v3):
    add = v1 + v2
    mul = v2 * v3
    divide = v3 / v1
    return add, mul, divide


a, b, c = math_operation(20, 30, 40)
print("addition :", a)  # 50
print("multiplication :", b)  # 1200
print("Division :", c)

result = math_operation(50, 70, 90)
print("result :", result)  # (120, 6300, 1.8)
print("result :", result[2])  # 1.8

####################################################################################
#   function program to add two numbers.
print("_" * 25, '# Exercise 1', "_" * 25)

# Method 1
print("_" * 50)


def addition1(x, y):
    sum = x + y
    print(sum)


addition1(4, 5)

# Method 2
print("_" * 50)


def addition2(*args):
    sum1 = sum(args)
    print(sum1)


addition2(10, 5)

# Method 3
print("_" * 50)


def addition3(*args):
    sum1 = sum(args)
    print(sum1)


addition3(10, 10)

####################################################################################
#   Python function program to print the input string 10 times.
print("_" * 25, '# Exercise 2 #', "_" * 25)


def print10(x):
    print(x * 10)


print10('Santosh ')

####################################################################################
#   function program to print a table of a given number.
print("_" * 25, '# Exercise 3 #', "_" * 25)


def table(x):
    for i in range(1, 11):
        print(x, '*', i, '=', x * i)


table(5)

####################################################################################
#   function program to find the maximum of three numbers.
print("_" * 25, '# Exercise 4 #', "_" * 25)


def maxim(*args):
    print('Max of numbers is : ', max(args))


maxim(17, 21, -9)

####################################################################################
#   function program to find the sum, prod of all the numbers in a list.
print("_" * 25, '# Exercise 5 #', "_" * 25)


def addition3(*args):
    sum = 0
    prod = 1
    for val in list1:
        sum += val
        prod *= val
    print(sum)
    print(prod)


list1 = [-8, 6, 1, 9, 2]
addition3(list1)

####################################################################################
#   function program to find the sum, prod of all the numbers in a list.
print("_" * 25, '# Exercise 6 #', "_" * 25)


def rev_str(*args):
    print(str1[::-1])


str1 = 'Python1234'
rev_str(str1)

####################################################################################
#   Python function program to check whether a number is in a given range.
print("_" * 25, '# Exercise 7 #', "_" * 25)


def range1(*args):
    if num in range(2, 21):
        print('Present in range')
    else:
        print('Not Present in range')


num = 20
range1(num)

####################################################################################
#   function program that takes a list and returns a new list with unique elements of the first list.
print("_" * 25, '# Exercise 8 #', "_" * 25)


def sort_list(x):
    a = set(x)
    print(a)


list1 = [2, 2, 3, 1, 4, 4, 4, 4, 4, 6]
sort_list(list1)

####################################################################################
# function program that take a number as a parameter and checks whether the number is prime or not.
print("_" * 25, '# Exercise 9 #', "_" * 25)


def prime(x):
    count = 0
    for i in range(2, x - 1):
        if x % i == 0:
            count = 1
    if count == 0:
        print('Prime')
    else:
        print('Not Prime')


num = 11
prime(num)

####################################################################################
# function function program to find the even numbers from a given list.
print("_" * 25, '# Exercise 10 #', "_" * 25)


def func1(l):
    for val in l:
        if val % 2 == 0:
            list2.append(val)
    print(list2)


list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list2 = []
func1(list1)

####################################################################################
# function program to create and print a list where the values are squares of numbers between 1 to 10.
print("_" * 25, '# Exercise 11 #', "_" * 25)


def func2(l):
    for i in range(1, l):
        print(i ** 2, end=", ")


func2(10)
print()
####################################################################################
# function program to find the LCM of two numbers.
print("_" * 25, '# Exercise 12 #', "_" * 25)


def lcm(x, y):
    for i in range(2, x + 1):
        if x % i == y % i == 0:
            print('LCM is :', i)
            break


lcm(14, 21)

####################################################################################
# function program to calculate the sum of numbers from 0 to 10.
print("_" * 25, '# Exercise 13 #', "_" * 25)


def summation(x):
    sum1 = 0
    for i in range(x + 1):
        sum1 += i
    print('summation :', sum1)


summation(10)

####################################################################################
# function program to find the HCF of two numbers.
print("_" * 25, '# Exercise 14 #', "_" * 25)


def hcf(x, y):
    for i in range(2, x + 1):
        if x % i == y % i == 0:
            hcf = i
    print('HCF :', hcf)


hcf(18, 54)

####################################################################################
# function program to create a function with *args as parameters.
print("_" * 25, '# Exercise 15 #', "_" * 25)


def func4(*args):
    print(args)
    for val in args:
        print(val ** 3)


func4(5, 6, 8, 7)

####################################################################################
# function program to get the factorial of a given number.
print("_" * 25, '# Exercise 16 #', "_" * 25)


def factorial(num):
    prod = 1
    for i in range(1, num + 1):
        prod *= i
    print('factorial', prod)


factorial(10)

####################################################################################
# Python function program to get the Fibonacci series up to the given number.
print("_" * 25, '# Exercise 17 #', "_" * 25)


def fibonacci(num):
    f0 = 0
    f1 = 1
    list1 = []
    list1.append(f0)
    list1.append(f1)
    for i in range(num - 2):
        f = f0 + f1
        f0 = f1
        f1 = f
        list1.append(f)
    print(list1)


fibonacci(10)

####################################################################################
# function program to check whether a combination of two numbers has a sum of 10 from the given list.
print("_" * 25, '# Exercise 18 #', "_" * 25)
list1 = [2, 5, 6, 4, 7, 3, 8, 9, 1]


def check_sum(num):
    for i in range(len(list1)):
        for j in range(i + 1, len(list1)):
            if list1[i] + list1[j] == 10:
                print('True')
                break
        break


check_sum(list1)

####################################################################################
# function program to get unique values from the given list.
print("_" * 25, '# Exercise 19 #', "_" * 25)
list1 = [4, 6, 1, 7, 6, 1, 5]
list2 = []


def unique(num):
    for val in list1:
        # list2 = set(list1)
        if val not in list2:
            list2.append(val)
    print(list2)


unique(list1)

# function program to get the duplicate characters from the string.
print("_" * 25, '# Exercise 20 #', "_" * 25)
str1 = 'Programming'
list2 = []


def duplicate(str1):
    for char in str1:
        if str1.count(char) > 1:
            if char not in list2:
                list2.append(char)
    print(list2)


duplicate(str1)

####################################################################################
# function program to get the square of all values in the given dictionary.
print("_" * 25, '# Exercise 21 #', "_" * 25)
dict1 = {'a': 4, 'b': 3, 'c': 12, 'd': 6}


def square(dict1):
    dict2 = {}
    for key, val in dict1.items():
        dict2[key] = val ** 2
    print(dict2)


square(dict1)

####################################################################################
# Python function program to create dictionary output from the given string.
# Note: Combination of the first and last character from each word should be
# key and the same word will the value in the dictionary.
print("_" * 25, '# Exercise 22 #', "_" * 25)

str1 = 'Python is easy to Learn'


def first_last(str1):
    list1 = str1.split(" ")
    dict1 = {}
    for word in list1:
        key = word[0] + word[-1]
        dict1[key] = word
    print(dict1)


first_last(str1)

####################################################################################
# function program to print a list of prime numbers from 1 to 100.
print("_" * 25, '# Exercise 23 #', "_" * 25)

str1 = 'Python is easy to Learn'


def prime(num):
    list1 = []
    for i in range(2, num):
        count = 0
        for j in range(2, i):
            if i % j == 0:
                count = 1
        if count == 0:
            list1.append(i)
    print(list1)


prime(100)

####################################################################################
# function program to check whether the given year is a leap year.
print("_" * 25, '# Exercise 24 #', "_" * 25)

str1 = 'Python is easy to Learn'


def leap(num):
    if num % 4 == 0:
        print('Leap year')
    else:
        print('Not leap year')


leap(2023)

####################################################################################
# function program to reverse an integer.
print("_" * 25, '# Exercise 25 #', "_" * 25)

str1 = 'Python is easy to Learn'


def leap(num):
    num = str(num)
    str1 = num[::-1]
    print(str1, type(num))


leap(2023)

####################################################################################
# Calculator
print("_" * 25, '# Calculator #', "_" * 25)


def calculator():
    def addition(num1, num2):
        return num1 + num2

    def substraction(num1, num2):
        return num1 - num2
    def multiplication(num1, num2):
        return num1 * num2

    def division(num1, num2):
        return num1 / num2

    num1 = int(input('Enter first number :'))
    num2 = int(input('Enter Second number :'))
    operation = int(input('************************************* \n Enter 1 for addition \n'
                          'Enter 2 for Substraction \n'
                          ' Enter 3 for Multiplication \n'
                          ' Enter 4 for Division \n'
                          'Enter 5 to Exit \n \n'))

    if operation == 1:
        print(f'Sum of numbers {num1} & {num2} is :', addition(num1, num2))
    elif operation == 2:
        print(f'Substraction of numbers {num1} & {num2} is :', substraction(num1, num2))
    elif operation == 3:
        print(f'Multiplication of numbers {num1} & {num2} is :', multiplication(num1, num2))
    elif operation == 3:
        print(f'Division of numbers {num1} & {num2} is :', division(num1, num2))
    else:
        exit()

while(True):
    calculator()