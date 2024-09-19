num1 = 10
num2 = '20'
#print(num1+num2) # stops program executuion
#print('Good Morning')

def try_exceptional_handling():
    try:
        num1 = 10
        num2 = '20'
        print(num1 + num2)
    except Exception as e:
        print(e)
        print('Addtion of int and str is not allowed')
    print('Good Morning')


#try_exceptional_handling()

# Explicitly raise exception to stop the program to execute further
print('_'*50)
def try_exceptional_handling_with_raise():
    try:
        num1 = 10
        num2 = '20'
        print(num1 + num2)
    except Exception as e:
        print(e)
        print('Addtion of int and str is not allowed')
        raise
    print('Good Morning') #this wont execute if ant exception occured

#try_exceptional_handling_with_raise()


# try except & else condition

def try_exceptional_handling_with_else():
    try:
        num1 = 10
        num2 = 0
        print('Divide', num1//num2)
    except Exception as e:
        print(e)
    else: # only executes when there is no exception
        print('Division is successful')

#try_exceptional_handling_with_else()


# try except & block

def try_exceptional_handling_with_block():
    try:
        num1 = 100
        num2 = '300'
        print('addition: ', num2+num1)
    except Exception as e:
        print(e)
    finally: # executes everytime
        print('Addition is successful')


# try_exceptional_handling_with_block()

# handle multiple exception for the operation

def math_operations_wit_multiple_exception():
    try:
        num1 = 100
        num2 = 200
        num3 = 300
        print('addition: ', num2 + num1 + num3)
    except Exception as e:


































