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
def addition2(*args):
    sum1 = sum(args)
    print(sum1)

addition2(10, 10)