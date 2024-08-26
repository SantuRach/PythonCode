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




















