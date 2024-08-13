

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

leng = len(str2)
result = str2[0:leng+1] #Python programming
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
legth = len(str1)
if legth <= 2:
    print("Invalid string")
else:
    result1 = str1[0:2]
    result2 = str1[legth-2:legth+1]
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
print("_Santosh" * 50)

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

# Exercise 21
# Python program to get common words from strings.
print("_" * 50)

str1 = 'Very Good Morning, How are You'
str2 = 'You are a Good student, keep it up'
list1 = str1.split(" ")
list2 = str2.split(" ")
list3 = []
for word in list1:
    if word in list2:
        list3.append(word)
print(list3)

# Exercise 22
# Python program to get common words from strings.
print("_" * 50)

str1 = 'sqqs'
if str1 == str1[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

# Exercise 23
# program to calculate the frequency of each character in a string.
print("_" * 50)
dictionary = dict()

str1 = 'sqatools'
for char in str1:
    dictionary[char] = str1.count(char)
print(dictionary)


# Exercise 24
# program to combine two strings into one.
print("_" * 50)
str1 = 'abc'
str2 = 'def'

print(str1+str2)

# Exercise 25
# Write a program to check if a string has a number or not.
print("_" * 50)
str1 = 'sqatools'
output = 'String dont have a number'
for char in str1:
    if char.isnumeric():
        output = 'String have a number'
print(output)

# Exercise 26
# program to count the number of vowels in a string.
print("_" * 50)
str1 = 'I am learning python'
vowels = 'aeiouAEIOU'

output = 0

for char in str1:
    if char in vowels:
        output += 1
print("Vowels count in str1: ", output)

# Exercise 28
# program to count the number of consonants in a string.
print("_" * 50)
str1 = 'I am learning python'
vowels = 'aeiouAEIOU'

output = 0

for char in str1:
    if char not in vowels:
        output += 1
print("consonants count in str1: ", output)

# Exercise 29
# program to remove all duplicate characters from a given string in python.
print("_" * 50)
str1 = 'sqatools'

# Exercise 30
# program to check if a string has a special character or not
print("_" * 50)
str1 = 'pythonsqatools'
if str1.isalnum():
    print("NO special character")
else:
    print("Has special character")

# Exercise 31
# program to exchange the first and last letters of the string
print("_" * 50)
str1 = 'We are learning python'

print(str1[-1]+str1[1:-1:]+str1[0])

# Exercise 32
# program to convert all the characters in a string to Upper Case
print("_" * 50)
str1 = 'I live in pune'

print(str1.upper())

# Exercise 33
# Write a program to remove a new line from a string using python
print("_" * 50)
str1 = 'objectorientedprogramming\n'

print(str1.replace("\n", ""))

# Exercise 34
# python program to split and join a string
print("_" * 50)
str1 = 'Hello world'
list1 = str1.split(" ")

output = "-".join(list1)
print(output)

# Exercise 35
# program to print floating numbers up to 3 decimal places and convert it to string
print("_" * 50)
str1 = 2.14652

output = str(round(str1, 3))

print(output, type(output))

# Exercise 36
# python program to find the location of a word in a string
print("_" * 50)
str1_inp = 'I am solving based on strings problems'
str1 = 'problems'
list1 = str1_inp.split(" ")
print(list1)
for word in list1:
    if word == str1:
        index = list1.index(word)
        index += 1

print(index)

# below function can also be used directly
print(list1.index(str1))


# Exercise 37
# python program to find the location of a word in a string
print("_" * 50)
str1_inp = 'I want to eat fast food @ food center food food food food food food'
str1 = 'food'
list1 = str1_inp.split(" ")
print(list1)
count = list1.count(str1)

print(count)

# Exercise 38
# words greater than the given length
print("_" * 50)
str1_inp = 'We are learning python food'
str1 = 3
list1 = str1_inp.split(" ")
print(list1)
for word in list1:
    leng = len(word)
    if leng > str1:
        print(word, end=" ")

# Exercise 39
# words greater than the given length
print("_" * 50)
str1_inp = 'Sqatools'

print(str1_inp[0:4])

# Exercise 40
# Python program to get a string made of the first 2 and the last 2 chars from a given
print("_" * 50)
str1_inp = 'Sqatools'

print(str1_inp[0:2]+str1_inp[-2:])

# Exercise 41
# program to print the mirror image of the string.
print("_" * 50)
str1_inp = 'Sqatools'

print("Mirror image of", str1_inp, " is : ", str1_inp[::-1])

# Exercise 42
# python program to split strings on vowels
print("_" * 50)
str1_inp = 'qwertay'
vowels = 'aeiouAEIOU'
str1 = output = ''
for char in str1_inp:
    if char in vowels:
        str1 = str1 + " "
    else:
        str1 += char
print(str1)

# Exercise 43
# python program to replace multiple words with certain words. Replace python with SQA  and sqatools with TOOLS
print("_" * 50)
str1_inp = 'I’m learning python at Sqatools, python, Sqatools'

str1 = str1_inp.replace('python', 'SQA')
str1 = str1.replace('Sqatools', 'TOOLS')
print(str1)

# Exercise 44
# python program to replace multiple words with certain words. Replace python with SQA  and sqatools with TOOLS
print("_" * 50)
str1_inp = 'I’m learning python at Sqatools, python, Sqatools'

str1 = str1_inp.replace('python', 'SQA')
str1 = str1.replace('Sqatools', 'TOOLS')
print(str1)

# Exercise 45
# program to remove empty spaces from a list of strings.
print("_" * 50)
list1 = ['Python','','','Programming']

list2 = []
for word in list1:
    if len(word) == 0:
        continue
    else:
        list2.append(word)
print(list2)

# Exercise 46
# python program to find duplicate characters in a string
print("_" * 50)
str1 = 'hello world'
str2 = ''
for char in str1:
    count = str1.count(char)
    #print(char, count)
    if count >= 2 and char not in str2:
        #print(char, end="")
        str2 = str2 + char
    else:
        continue
    count = 0
print(str2)

# Exercise 47
# Write a python program to sort a string
print("_" * 50)
str1 = 'xyabkmp'
str2 = sorted(str1)

print(str2, type(str2))
print("".join(sorted(str1)))

import random

# Exercise 48
# program to generate a random binary string of a given length.
print("_" * 50)

str1 = ''
for i in range(0,8):
    val = str(random.randint(0,1))
    str1 += val
print(str1)


# Exercise 49
# program to check if the substring is present in the string or not
print("_" * 50)

str1 = 'I live in Pune'
str2 = 'I live'
if str2 in str1:
    print('Yes')
else:
    print('No')

# Exercise 50
# program to print the index of the character in a string.
print("_" * 50)

str1 = 'I live in Pune'
print('Index of e is: ', str1.index('e'))

# Exercise 51
# Write a program to strip spaces from a string
print("_" * 50)

str1 = '                         I live in Pune      '
print('Strip is: ', str1.strip())
print('Strip is: ', str1.rstrip())
print('Strip is: ', str1.lstrip())

# Exercise 52
# program to check whether a string contains all letters of the alphabet or not.
print("_" * 50)

# Exercise 53
# program to check whether a string contains all letters of the alphabet or not.
print("_" * 50)

str1 = 'program to convert a string into a list of words.'
list1 = list(str1.split(" "))
print(list1)

# Exercise 54
# program to check whether a string contains all letters of the alphabet or not.
print("_" * 50)

str1 = 'sqa,to.,ols.'
str2 = ''
for char in str1:
    if char == ',':
        char = char.replace(char,'.')
    elif char == '.':
        char = char.replace('.', ',')
    else:
        char = char
    str2 += char
print(str2)

# Exercise 55
# program to split a string on the last occurrence of the delimiter.
print("_" * 50)

str1 = 'l,e,a,r,n,I,n,g,p,y,t,h,o,n'
str2 = str1.rsplit(",",1)
print(str2)

# Exercise 56
# program to find the first repeated word in a given string.
print("_" * 50)

str1 = 'ab bc ca ca bd'
list1 = str1.split(" ")
list2 = []
for word in list1:
    if word in list2:
        print("Repeated word is : ", word)
    else:
        list2.append(word)


# Exercise 57
# program to find the second most repeated word in a given string
print("_" * 50)

# Exercise 58
# Remove spaces from a given string
print("_" * 50)
str1 = "python at sqatools"
str2 = str1.replace(' ','')
print(str2)

# Exercise 59
#  program to capitalize the first and last letters of each word of a given string.
print("_" * 50)
str1 = "this is my first program"
list1 = str1.split()
str2 = ''

for word in list1:
    new_word = word[0].capitalize() + word[1:len(word)-1] + word[-1].capitalize() + ' '
    str2 = str2 + new_word

print(str2)

# Exercise 60
#  program to calculate the sum of digits of a given string.
print("_" * 50)
str1 = "12hrjk5sd7893"
sum = 0

for char in str1:
    if char.isnumeric():
        sum += int(char)

print(sum)

# Exercise 61
#  program to remove zeros from an IP address.
print("_" * 50)
str1 = "289.03.02.054"
str2 = ''
for char in str1:
    if char != '0':
        str2 += char

print(str2)

# Exercise 62
#  program to remove zeros from an IP address.
print("_" * 50)
str1 = "289.03.02.054"
str2 = ''
for char in str1:
    if char != '0':
        str2 += char

print(str2)

# Exercise 63
#  program to find the maximum length of consecutive 0’s
#  in a given binary string
print("_" * 50)
str1 = "10001100000111"
count = 0

for char in str1:
    if char == '0':
        count += 1
        temp = count
    else:
        count = 0

print(temp)


# Exercise 64
#  program to remove all consecutive duplicates of a given string
print("_" * 50)
str1 = "xxxxyyzzzzz"
str2 = ''

for char in str1:
    if char not in str2:
        str2 += char

print(str2)

# Exercise 65
# Write a program to create strings from a given string.
# Create a string that consists of multi-time occurring characters
# in the said string using python.
print("_" * 50)
str1 = "aabbcceffgh"
str2 = ''

for char in str1:
    count_char = str1.count(char)
    if count_char > 1:
        if char not in str2:
            str2 += char

print(str2)

# Exercise 66
# Write a program to count all the Uppercase, Lowercase, special character
# and numeric values in a given string
print("_" * 50)
str1 = "@SqaTo3ols.lin&"
upper = lower = digit = special = 0

for char in str1:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        digit += 1
    else:
        special += 1

print("Upper count is : ", upper)
print("lower count is : ", lower)
print("digit count is : ", digit)
print("special count is : ", special)

# Exercise 67
# program to uppercase half string using python.
print("_" * 50)
str1 = "Santosh"
middle = len(str1)//2

print(str1[0:middle]+str1[middle:].upper())

# Exercise 68
# program to remove the kth element from the string K =2
print("_" * 50)
str1 = "sqatools"
k = 2

print(str1[0:k]+str1[k+1:])

# Exercise 69
# program to reverse words in a string
print("_" * 50)
str1 = "string problems"
list1 = str1.split(" ")

print(" ".join(list1[::-1]))

# Exercise 70
# program to find the first repeated character in a string and its index.
print("_" * 50)
str1 = "sqatools"
for char in str1:
    count = str1.count(char)
    if count > 1:
        print(char, count)
        break

# Exercise 71
# program to find the first repeated character in a string and its index.
print("_" * 50)
str1 = "sqaTOOls"
for char in str1:
    count = str1.count(char)
    if count > 1:
        print(char, count)
        break

# Exercise 72 Swap case
str1 = str1.swapcase()
print(str1)

# Exercise 73
# program to get all the email id’s from given string using python.
print("_" * 50)
str1 = """We have some employee whos john@gmail.com email id’s are
randomly distributed jay@lic.com we want to get hari@facebook.com
all the email mery@hotmail.com id’s from this given string."""

str2 = '@'
list1 = str1.split(" ")

for word in list1:
    if str2 in word:
        print(word[0:word.index(str2)])

# Exercise 74
# program to get a list of all the mobile numbers from the given string
print("_" * 50)
str1 = """ We have 2233 some employee 8988858683 whos 3455 mobile numbers 
are randomly distributed 2312245566 we want 453452 to get 4532892234 all 
the mobile numbers 9999234355  from this given string. """

list1 = str1.split(" ")

for word in list1:
    if len(word) == 10:
        print(word, end =" ")

