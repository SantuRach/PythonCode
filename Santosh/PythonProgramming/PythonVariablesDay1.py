#   Data types
#       1. Int type
#       2. Float type
#       3. String type
#       4. Char type

#   Rules to define a variable
#       1. There should not be space in a variable name
#       2. Special characters are not allowed in variable name
#       3. Number is not allowed in the beginning of variable name
#       4. There is no limitation for variable name length
#       5. There is no limitation for variable name length
#       5. Variables are case-sensitive
#       5. Variable should start from begin of the line

"""
Operators
        + : Addition
        - : Subtraction
        * : Multiplication
        / : Division
        // : Division
        % : Remainder
        ** : power Operation
        == : Equal to
        = : assignment
        != : not Equal to
"""
# Int data type
print("_" * 100)
print("### Int data type")
var1 = 10
print(var1)
print(type(var1))
print(id(var1))

# String data type
print("_" * 100)
print("### String data type")
var2 = "Good Morning Santosh"
print(var2)
print(type(var2))
print(id(var2))

# Multiple Variable having same value will have same address. Memory utilisation
print("_" * 100)
print("### Multiple Variable having same value will have same address. Memory utilisation")
a = 10
b = 10
print(id(a))
print(id(b))

# Assign multiple values to multiple variables
print("_" * 100)
print("### Assign multiple values to multiple variables")
p, q, r = 50, 'Santosh', "Hello Santosh"
print("Value of p: ", p, "with address", id(p))
print("Value of q: ", q, "with address", id(q))
print("Value of r: ", r, "with address", id(r))

# Addition operator
print("_" * 100)
print("### Addition operator")
a = 100
b = 101
c = a + b
print(c)
print("Addition is :", c)
print(a + b)

# Subtraction operator
print("_" * 100)
print("### Subtraction operator")
a = 600
b = 345
c = a - b
print(c)
print("Subtraction is :", c)
print(a - b)

# Multiplication operator
print("_" * 100)
print("### Multiplication operator")
a = 12
b = 3
c = a * b
d = "Santosh "
print(c)
print("Multiplication is :", c)
print("Multiplication is :", a * b)
print("Multiplication of string :", d * 5)
print(a * b)

# Division with / operator and // operator
print("_" * 100)
print("### Division with / operator and // operator")
a = 14
b = 3
c = a / b
d = a // b
print(c)
print("Division with / operator :", c)
print("Division with / operator :", a / b)
print(d)

print("Division with // operator :", d)
print("Division with // operator :", a // b)
print(c)

# Remainder operator
print("_" * 100)
print("### Remainder operator")
a = 14
b = 3
c = a % b
print(c)
print("Remainder operator :", c)
print("Remainder operator :", a % b)

# Power operator
print("_" * 100)
print("### Power operator")
a = 10
b = 3
c = a ** b
print(c)
print("Power of a to b :", c)
print("Power of a to b :", a ** b)

# Equal to operator
print("_" * 100)
print("### Equal to operator")
a = 10
b = 3
c = 10
print("Compare a to b :", a == b)
print("Compare a to b :", c == b)
print("Compare a to b :", c == a)

# NotEqual to operator
print("_" * 100)
print("### NotEqual to operator")
a = 20
b = 10
c = 10
print("Compare a to b :", a != b)
print("Compare a to b :", c != b)
print("Compare a to b :", c != a)

# Solve the equation
# (a+b)*2 = a*2 + b*2 + 2*a*b
print("_" * 100)
a = 5
b = 6
LHS = (a + b) ** 2
print("LHS is : ", LHS)

RHS = a ** 2 + b ** 2 + 2 * a * b
print("RHS is : ", RHS)

print("RHS is equal to LHS : ", LHS == RHS)
