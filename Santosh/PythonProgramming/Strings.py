
''''
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

# str.rstrip method - removes blank space at the end only2
print("_" * 80)
str1 = '         Today India is playing good cricket        '
print(str1.rstrip())

# str.join method - removes blank space at the end only2
print("_" * 80)
str1 = 'Today India is playing good cricket'
output1 = '-'.join(str1)
print(output1) # T-o-d-a-y- -I-n-d-i-a- -i-s- -p-l-a-y-i-n-g- -g-o-o-d- -c-r-i-c-k-e-t

# isalpha - method checks only string contains alphabet or not
print("_" * 80)
str1 = 'SantoshRachotimath'
print(str1, str1.isalpha()) # true

# isalpha - method checks only string contains alphabet or not
print("_" * 80)
str1 = 'Santosh Rachotimath'
print(str1, str1.isalpha()) # False, since space is there

# isalpha - method checks only string contains alphabet or not
print("_" * 80)
str1 = 'Santosh123'
print(str1, str1.isalpha()) # False, since number is there

# isnumeric - method checks only string contains alphabet or not
print("_" * 80)
str1 = '123456789'
print(str1, str1.isnumeric()) # True

# isnumeric - method checks only string contains alphabet or not
print("_" * 80)
str1 = '123 456'
print(str1, str1.isalpha()) # False, since space is there

# isnumeric - method checks only string contains alphabet or not
print("_" * 80)
str1 = '123san'
print(str1, str1.isalpha()) # False, since alphabet is there


# is alpha numeric - method checks only string or numeric contains alphabet or not
print("_" * 80)
str1 = '123san'
print(str1, str1.isalnum()) # True

# is alpha numeric - method checks only string or numeric contains alphabet or not
print("_" * 80)
str1 = '123'
print(str1, str1.isalnum()) # True

# is alpha numeric - method checks only string or numeric contains alphabet or not
print("_" * 80)
str1 = 'san'
print(str1, str1.isalnum()) # True

# is space - method checks presence of space
print("_" * 80)
str1 = '123 san'
#print(str1, str1.isspace())
for char in str1:
    print(char, char.isspace()) # True

# isascii - method checks presence of space
print("_" * 80)
str1 = '123 san'
print(str1, str1.isascii()) # True

# isascii - method checks presence of space
print("_" * 80)
for char in range(65,90):
    print(char, chr(char))


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
output1 = str1.split(' ')
print(output1)
leng = temp = 0
for word in output1:
    leng = len(word)
    if leng > temp:
        temp1 = word
    else:
        continue

print(temp1)


# Exercise 9
# Most simultaneously repeated character in string

# Exercise 10
# Python program to replace the second occurrence of any char with the special character $.
print("_" * 50)

str1 = 'Progr'
str2 = '$'
count = 0
for char in str1:
#    print(str1.count(char))
    if str1.count(char) > 1:
        count += 1
        if count == 2:
            output1 = str1.replace(char,str2)
            print(output1)
            count = 0
    else:
        continue


# Exercise 10
# program to get to swap the last character of a given string.
print("_" * 50)

str1 = 'santosh'

print(str1[-1]+str1[1:-1]+str1[0])

# Exercise 11
# program to exchange the first and last character of each word from the given string.
print("_" * 50)

str1 = 'Its Online Learning'
output1 = str1.split(' ')
output2 = output1[0][-1]+output1[0][1:-1]+output1[0][0]+" "
output3 = output1[1][-1]+output1[1][1:-1]+output1[1][0]+" "
output4 = output1[2][-1]+output1[2][1:-1]+output1[2][0]+" "
print(output2 + output3 +output4)

# Exercise 12
# program to exchange the first and last character of each word from the given string.
print("_" * 50)
count1 = 0

str1 = 'We are learning python programming'
list1 = str1.split(' ')
vowels = 'aeiou'
list2 = []
for word in list1:
    for char in word:
        if char in vowels:
            count1 += 1
    list2.append(count1)
    count1 = 0

output = dict(zip(list1,list2))
print(output)

# Exercise 13
# python to repeat vowels 3 times and consonants 2 times.
print("_" * 50)

str1 = 'SqA Tools Learning'
vowels = 'aeiou'
VOWELS = 'AEIOU'
str2 = ''

for char in str1:
    if char in vowels or VOWELS:
        str2 = str2+char*3
    else:
        str2 = str2+char*2

print(str2)

# Exercise 14
# python program to get all the digits from the given string.
print("_" * 50)

str1 = """
Sinak’s 1112 aim is to 1773 create a new generation of people who
understand 444 that an organization’s 5324 success or failure is
based on 555 leadership excellence and not managerial
acumen 
"""
list1 = str1.split(" ")
list2 = []

for char in list1:
    if char.isnumeric():
        list2.append(char)

print(list2)

# Exercise 15
# python program to replace the words “Java” with “Python” in the given string.
print("_" * 50)

str1 = 'JAVA is the Best Programming Language in the Market'
output = str1.replace('JAVA','Python')

print(output)

# Exercise 16
# Python program to get all the palindrome words from the string.
print("_" * 50)

str1 = 'Python efe language aakaa hellolleh'
list1 = str1.split(' ')
list2 = []

for word in list1:
    if word == word[::-1]:
        list2.append(word)
print(list2)

# Exercise 17
# Python program to create a string with a given list of words.
print("_" * 50)

str1 = 'Python efe language aakaa hellolleh'
list1 = ['There', 'are', 'Many', 'Programming', 'Language']
output = ''

for word in list1:
    output = output + word + ' '
output = output.capitalize()
print(output)

# Exercise 18
# Python program to remove duplicate words from the string.
print("_" * 50)

str1 = 'John jany sabi row john sabi'
list1 = str1.split(" ")
output = ''

for word in list1:
    count = list1.count(word)
    if count == 1:
        output = output + word + " "
print(output)

# Exercise 19
# to remove unwanted characters from the given string.
print("_" * 50)

str1 = 'Py(th)#@&on Pro$*#gram'
output = ''

for char in str1:
#    count = list1.count(word)
    if char.isalpha():
        output = output + char
print(output)

# Exercise 20
# program to find the longest capital letter word from the string.
print("_" * 50)

str1 = 'PROGRAMMING Learning PYTHON is FUN'
list1 = str1.split(" ")
output = ''
leng = temp = 0
for word in list1:
    if word.isupper():
        leng = len(word)
        if leng > temp:
            output = word
            temp = leng
print(output)

'''
























