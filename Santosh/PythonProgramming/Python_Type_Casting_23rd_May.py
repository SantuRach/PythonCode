########################################## Type casting ##########################################
########################### Integer Type casting ###########################

############## int -> Float ##############
print("_" * 100)

var1 = 5
print(var1, type(var1))

print(var1, type(float(var1))) #1

var2 = float(var1)
print(var2, type(var2)) #2

############## int -> String ##############
print("_" * 100)

var1 = 123456789
print(var1, type(var1))
print(var1, type(str(var1))) #1

var2 = str(var1)
print(var2, type(var2)) #2
print(var2[3]) # 4
print(var2[6]) # 7
############## int -> List ##############
# Conversion is not possible


############## int -> tuple ##############
# Conversion is not possible


############## int -> Dict ##############
# Conversion is not possible


############## int -> Set ##############
# Conversion is not possible


############## int -> Boolean ##############
# Conversion is possible only to 0, 1
# 0 -> FALSE , Any int value other than 0 will be TRUE
print("_" * 100)
var1 = 0
print(var1, type(var1))
print(var1, type(bool(var1))) #1
var2 = bool(var1)
print(var2, type(var2)) #2

print("_" * 100)
var1 = 1
print(var1, type(var1))
print(var1, type(bool(var1))) #1
var2 = bool(var1)
print(var2, type(var2)) #2

print("_" * 100)
var1 = 11866864566 # Other than 0,1
print(var1, type(var1))
print(var1, type(bool(var1))) #1
var2 = bool(var1)
print(var2, type(var2)) #2

########################### Float Type casting ###########################

############## Float -> Int ##############
# Any value after . will be ignored while converting to Int
print("_" * 100)

var1 = 5.9
print(var1, type(var1))
print(var1, type(int(var1))) #1
var2 = int(var1)
print(var2, type(var2)) #2

############## Float -> Str ##############

print("_" * 100)

var1 = 556456.9
print(var1, type(var1))
print(var1, type(str(var1))) #1
var2 = str(var1)
print(var2, type(var2)) #2
print(var2[3]) # 4
print(var2[6]) # .

############## Float -> List ##############
# Conversion is not possible


############## Float -> tuple ##############
# Conversion is not possible


############## Float -> Dict ##############
# Conversion is not possible


############## Float -> Set ##############
# Conversion is not possible

############## Float -> Boolean ##############
# Conversion is possible only to 0, 1
# 0 -> FALSE , Any int value other than 0 will be TRUE
print("_" * 100)
var1 = 0.0
print(var1, type(var1))
print(var1, type(bool(var1))) #1
var2 = bool(var1)
print(var2, type(var2)) #2

print("_" * 100)
var1 = 0.2
print(var1, type(var1))
print(var1, type(bool(var1))) #1
var2 = bool(var1)
print(var2, type(var2)) #2

print("_" * 100)
var1 = 2.5 # Other than 0,1
print(var1, type(var1))
print(var1, type(bool(var1))) #1
var2 = bool(var1)
print(var2, type(var2)) #2

########################### String Type casting ###########################

############## String -> Int ##############
# Direct conversion is not possible id character are present
"""
print("_" * 100)
str1 = "Santosh"
print(str1, type(str1))
print(str1, type(int(str1))) #1
var2 = int(str1)
print(var2, type(var2)) #2
print(var2*var2) # 27.040000000000003
"""

# Conversion is possible only if string has number
print("_" * 100)

str1 = "25"
print(str1, type(str1))
print(str1, type(int(str1))) #1
var2 = int(str1)
print(var2, type(var2)) #2
print(var2*var2) #625

############## String -> Float ##############
# Direct conversion is not possible if character are present in string
"""
print("_" * 100)
str1 = "Santosh"
print(str1, type(str1))
print(str1, type(float(str1))) #1
var2 = float(str1)
print(var2, type(var2)) #2
print(var2*var2) # 27.040000000000003
"""

# Conversion is possible only if string has number
print("_" * 100)

str1 = "5.2"
print(str1, type(str1))
print(str1, type(float(str1))) #1
var2 = float(str1)
print(var2, type(var2)) #2
print(var2*var2) # 27.040000000000003

############## String -> List ##############
print("_" * 100)

str1 = "Santosh"
print(str1, type(str1))
print(str1, type(list(str1))) #1
print(list(str1)) #1
var2 = list(str1)
print(var2, type(var2)) # ['S', 'a', 'n', 't', 'o', 's', 'h'] <class 'list'>

############## String -> Tuple ##############
print("_" * 100)

str1 = "Rachotimath"
print(str1, type(str1))
print(str1, type(tuple(str1))) #1
print(tuple(str1)) #1
var2 = tuple(str1)
print(var2, type(var2)) # ('R', 'a', 'c', 'h', 'o', 't', 'i', 'm', 'a', 't', 'h') <class 'tuple'>

############## String -> Dict ##############
# Direct Conversion is not possible
# Key and Value mapping should be present same as Dict
# Single quote to be used for string declaration
# import json to covert string to Dict
# json.loads method to be used to convert

import json
print("_" * 100)

str1 = '{"Name" : 552, "Surname" : "Rachotimath", "DOB" : "28Aug1989"}'
dict2 = json.loads(str1)
print(dict2, type(dict2)) #{'Name': 1, 'Surname': 'Rachotimath', 'DOB': '28Aug1989'} <class 'dict'>

############## String -> Set ##############
# Stores the set in random order
# Duplicte values will be ignored

str1 = "Rachotimath"
print(str1, type(str1))
print(str1, type(set(str1)))
print(set(str1))
var2 = set(str1)
print(var2, type(var2))


############## String -> Boolean ##############
# Conversion is possible only to 0, 1
# 0 -> FALSE , Any int value other than 0 will be TRUE
print("_" * 100)
str1 = ""
print(str1, type(str1))
print(str1, type(bool(str1)))
print(bool(str1))
var2 = bool(str1)
print(var2, type(var2))

print("_" * 100)
str1 = " "
print(str1, type(str1))
print(str1, type(bool(str1)))
print(bool(str1))
var2 = bool(str1)
print(var2, type(var2))

print("_" * 100)
str1 = "Santosh"
print(str1, type(str1))
print(str1, type(bool(str1)))
print(bool(str1))
var2 = bool(str1)
print(var2, type(var2))

########################### List Type casting ###########################

############## List -> Int ##############
# Conversion is not possible

############## List -> Float ##############
# Conversion is not possible

############## List -> String ##############
#
print("_" * 100)
list1 = "4,5,'Santosh',6.2"
print(str1, type(str1))
print(str1, type(bool(str1)))
print(bool(str1))
var2 = bool(str1)
print(var2, type(var2))