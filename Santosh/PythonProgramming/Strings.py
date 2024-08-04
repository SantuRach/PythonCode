
print("_" * 80)
str1 = 'Hello'
str2 = "Python programming"
str3 = """Python programming
i love
i code it
"""

print(str1, type(str1))
print(str2, type(str2))
print(str3, type(str3))

print("_" * 80)
str5 = "Program"
for char in str5:
    print(char)

######################### String formatting #########################

############## String Concatenation ##############
print("_" * 80)
name = 'Santosh'
age = 36
place = 'bangalore'
place1 = ['bangalore', 'Mumbai', 'Chennai']
print("_" * 80)
# 1. Concatenation (+)
print("My name is "+ name + "My age is age " +str(age)+ ". i live in" + place)
print("_" * 80)
# 2. dot (.) format method
print("My name is {}. My age is age {}. i live in {}".format(name, age, place))
print("_" * 80)
# 3.  f string formatting
print(f"My name is {name}. My age is  {age}. i live in {place1[2]}")

############## String Slicing ##############
# str2[start_index:end_index:difference]

print("_" * 80)
str2 = "Python programming"

result = str2[0:9] #Python pr
print(result)

result = str2[0:-1] #Python programmin
print(result)

len= len(str2)
result = str2[0:len+1] #Python programming
print(result)

result = str2[-6:-9] #blank. not print anything. ALways left to right reading
print(result)

result = str2[-6:-5] #a
print(result)

result = str2[:-5] #Python progra
print(result)

result = str2[5:] #n programming
print(result)

result = str2[5::2] #npormig . differnce prints by skipping 2
print(result)

result = str2[-1:-16:-1] #gnimmargorp noh . differnce reverese
print(result)


############## String methods ##############
print("_" * 80)
print(dir(str))
"""
__add__ => 
__class__ => 
__contains__ => 
__delattr__ => 
__dir__ => 
__doc__ => 
__eq__ => 
__format__ => 
__ge__ => 
__getattribute__ => 
__getitem__ => 
__getnewargs__ => 
__getstate__ => 
__gt__ => 
__hash__ => 
__init__ => 
__init_subclass__ => 
__iter__ => 
__le__ => 
__len__ => 
__lt__ => 
__mod__ => 
__mul__ => 
__ne__ => 
__new__ => 
__reduce__ => 
__reduce_ex__ => 
__repr__ => 
__rmod__ => 
__rmul__ => 
__setattr__ => 
__sizeof__ => 
__str__ => 
__subclasshook__ => 
capitalize => 
casefold => 
center => 
count => 
encode => 
endswith => 
expandtabs => 
find => 
format => 
format_map => 
index => 
isalnum => 
isalpha => 
isascii => 
isdecimal => 
isdigit => 
isidentifier => 
islower => 
isnumeric => 
isprintable => 
isspace => 
istitle => 
isupper => 
join => 
ljust => 
lower => 
lstrip => 
maketrans => 
partition => 
removeprefix => 
removesuffix => 
replace => 
rfind => 
rindex => 
rjust => 
rpartition => 
rsplit => 
rstrip => 
split => 
splitlines => 
startswith => 
strip => 
swapcase => 
title => 
translate => 
upper => 
zfill =>

"""
str1 = 'Good Morning Santosh'

print("Upper : ", str1.upper()) #GOOD MORNING SANTOSH
print("Lower : ", str1.lower()) #good morning santosh
print("Lower : ", str1.swapcase()) #gOOD mORNING sANTOSH
print("_" * 80)
str1 = 'GOOD MORNING SANTOSH'
print("Lower : ", str1.isupper()) # true
print("Lower : ", str1.islower()) # False
print("_" * 80)
str1 = 'good morning santosh'
print("Lower : ", str1.isupper()) # False
print("Lower : ", str1.islower()) # true

print("_" * 80)
str1 = 'good morning santosh'
print("Title : ", str1.title()) # Good Morning Santosh
print("Title : ", str1.istitle()) # False

print("_" * 80)
str1 = 'Good Morning Santosh'
print("Title : ", str1.istitle()) # True

print("_" * 80)
str1 = 'Good Morning SantOsh'
print("Count of o : ", str1.count('o')) # 3 # it is case sensitive

# str.Count method
print("_" * 80)
str1 = 'Good Morning SantOsh'
str2 = ""

for char in str1:
    if char in str2:
        continue
    else:
        print(char, str1.count(char))
        str2 += char

print(str2) #prints without duplicates


# str.index method
print("_" * 80)
str1 = 'Good Morning SantOsh'
print(str1.index('o')) # 1
print(str1.index('San')) # 13
#print(str1.index('w')) #substring not found


# str.find method
print("_" * 80)
str1 = 'Good Morning SantOsh'
print(str1.find('o')) # 1
print(str1.find('ing')) # 9
print(str1.find('w')) # -1

# str.replace method
print("_" * 80)
str1 = 'Good Morning Santosh'
print(str1.replace('Morning','Evening'))


# str.split method
print("_" * 80)
str1 = 'Today India is playing good cricket'
print(str1.split())


# str.strip method - removes blank space at the beginning and end
print("_" * 80)
str1 = '         Today India is playing good cricket        '
print(str1.strip())

# str.lstrip method - removes blank space at the beginning only
print("_" * 80)
str1 = '         Today India is playing good cricket        '
print(str1.lstrip())

# str.rstrip method - removes blank space at the end only
print("_" * 80)
str1 = '         Today India is playing good cricket        '
print(str1.rstrip())

''''
# Exercise 1
#   program to get a string made of the first and the last 2 chars
#   from a given string. If the string length is
#   less than 2, return instead of the empty string
print("_" * 50)

str1 = 'santosh'
leng = len(str1)
if leng<= 2:
    print("Invalid string")
else:
    result1 = str1[0:2]
    result2 = str1[leng-2:leng+1]
    print(result1, result2)

# Exercise 2
#   List of strings as input and returns the length of the longest string
print("_" * 50)

list1 = ['Santosh', 'Santosh Rach', 'Santosh Rachoti', 'Santosh Rachotimath']
temp = 0
for word in list1:
    leng = len(word)
    if leng > temp:
        temp = leng
        temp_word = word
print(temp_word)


# Exercise 3
#   string program to get a string made of 4 copies of the last two characters
#   of a specified string (length must be at least 2)
print("_" * 50)

str1 = 'Santosh'
leng = len(str1)
if leng <= 2:
    print("Invalid string")
else:
    last_char = str1[-2:]
    print(last_char*4)

# Exercise 4
#   string program to reverse a string if it’s length is a multiple of 4.
print("_" * 50)

str1 = 'Santosh1'
leng = len(str1)
if leng % 4 == 0:
    print(str1[::-1])
else:
    print("Invalid string")

# Exercise 5
#   Count occurrences of a substring in a string.
print("_" * 50)

str1 = 'Santosh Santosh Santosh Santosh'
sub_str1 = 'San'

count = str1.count(sub_str1)
print(count)

# Exercise 7
#   program to test whether a passed letter is a vowel or consonant
print("_" * 50)

str1 = 'Santosh Rachotimath'
vowels = ['a','e','i','o','u']

for char in str1:
    if char in vowels:
        print(f"{char} is vowel")
    else:
        print(f"{char} is consonant")



# Exercise 8
# longest and smallest word in the input string
print("_" * 50)

str1 = 'I am Santosh Rachotimath'
vowels = ['a','e','i','o','u']

for char in str1:
    if char in vowels:
        print(f"{char} is vowel")
    else:
        print(f"{char} is consonant")
'''