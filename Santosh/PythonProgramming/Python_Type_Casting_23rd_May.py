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
# brackets, space, character every thing is considered as string.
print("_" * 100)
list1 = [4,5,'Santosh',6.2,{1,45,56,34}]
print(list1, type(list1))
print(list1, type(str(list1)))
print(str(list1))
var2 = str(list1)
print(var2, type(var2))
print(var2[4], type(var2))
print(var2[5], type(var2))
print(var2[-1], type(var2)) #}

############## List -> Tuple ##############
# brackets, space, character, number every thing is considered as string.
print("_" * 100)
list1 = [3,5,'Santosh',6.2,{1,45,56,34}]
print(list1, type(list1))
print(list1, type(tuple(list1)))
print(tuple(list1))
var3 = tuple(list1)
print(var3, type(var3))
print(var3[4], type(var3))
print(var3[-2], type(var3))

############## List -> Dict ##############
# Direct conversion to dict is not possible.
# zip function to be used to convert
# two list should be present to map key and Value
# Question 1 raised. Why tuple inside the list is not converting to dict ?
print("_" * 100)
list4 = [4,5,'Santosh',6.2,1]
list5 = ['a',123,'Rachotimath','Santosh',2]
print(list4, type(list4))
print(list5, type(list5))
output1 = dict(zip(list4, list5))
print(output1, type(output1))
print(output1[4], type(output1))
print(output1[6.2], type(output1))
print(output1['Santosh'], type(output1))

############## List -> Set ##############
# Set dont have indexing
print("_" * 100)
list4 = [4,5,'Santosh',6.2,1]
print(list4, type(list4))
output1 = set(list4)
print(output1, type(output1))

############## List -> Boolean ##############
print("_" * 100)
list4 = []
print(list4, type(list4))
print(list4, type(bool(list4))) #1
var2 = bool(list4)
print(var2, type(list4)) #2

print("_" * 100)
list4 = [4,5,'Santosh',6.2,1]
print(list4, type(list4))
print(list4, type(bool(list4))) #1
var2 = bool(list4)
print(var2, type(list4)) #2


########################### Tuple Type casting ###########################

############## Tuple -> Int ##############
# Conversion is not possible

############## Tuple -> Float ##############
# Conversion is not possible

############## Tuple -> String ##############
# brackets, space, character every thing is considered as string.
print("_" * 100)
tup1 = (4,5,'Santosh',6.2,{1,45,56,34})
print(tup1, type(tup1))
print(tup1, type(str(tup1)))
print(str(tup1))
var2 = str(tup1)
print(var2, type(var2))
print(var2[4],var2[-1],var2[-5], type(var2))

############## Tuple -> List ##############
# brackets, space, character every thing is considered as string.
print("_" * 100)
tup1 = (4,5,'Santosh',6.2,{1,45,56,34})
print(tup1, type(tup1))
print(tup1, type(list(tup1)))
print(list(tup1))
var2 = list(tup1)
print(var2, type(var2))
print(var2[4],var2[-1],var2[-5], type(var2))

############## Tuple -> Dict ##############
# Direct conversion to dict is not possible.
# zip function to be used to convert
# two list should be present to map key and Value
# Question 1 raised. Why tuple inside the list is not converting to dict ?
print("_" * 100)
list4 = (4,5,'Santosh',6.2,1)
list5 = ('a',123,'Rachotimath','Santosh',2)
print(list4, type(list4))
print(list5, type(list5))
output1 = dict(zip(list4, list5))
print(output1, type(output1))
print(output1[4], type(output1))
print(output1[6.2], type(output1))
print(output1['Santosh'], type(output1))

############## Tuple -> Set ##############
# Set dont have indexing
print("_" * 100)
list4 = (4,5,'Santosh',6.2,1)
print(list4, type(list4))
output1 = set(list4)
print(output1, type(output1))

############## Tuple -> Boolean ##############
print("_" * 100)
list4 = ()
print(list4, type(list4))
print(list4, type(bool(list4))) #1
var2 = bool(list4)
print(var2, type(var2)) #2

print("_" * 100)
list4 = (4,5,'Santosh',6.2,1)
print(list4, type(list4))
print(list4, type(bool(list4))) #1
var2 = bool(list4)
print(var2, type(var2)) #2

########################### Dict Type casting ###########################

############## Dict -> Int ##############
# Conversion is not possible

############## Dict -> Float ##############
# Conversion is not possible

############## Dict -> String ##############
# Direct Conversion is not possible
# Key and Value mapping should be present same as Dict
# Single quote to be used for string declaration
# import json to covert string to Dict
# json.loads method to be used to convert

print("_" * 100)

dict1 = {"Name" : 552, "Surname" : "Rachotimath", "DOB" : "28Aug1989"}
print(dict1, type(dict1))
str1 = str(dict1)
print(str1, type(str1))
print(str1[2])

############## Dict -> List ##############
# Only list of keys will be printed not values
print("_" * 100)

dict1 = {"Name" : 552, "Surname" : "Rachotimath", "DOB" : "28Aug1989"}
print(dict1, type(dict1))
print(dict1, type(list(dict1)))
print(list(dict1))
var2 = list(dict1)
print(var2, type(var2))

############## Dict -> Tuple ##############
# Only list of keys will be printed not values
print("_" * 100)

dict1 = {"Name" : 552, "Surname" : "Rachotimath", "DOB" : "28Aug1989"}
print(dict1, type(dict1))
print(dict1, type(tuple(dict1)))
print(tuple(dict1))
var2 = tuple(dict1)
print(var2, type(var2))
print(dict1.values()) #prints values only
print(dict1.keys()) #prints keys only

############## Dict -> Set ##############
# Only list of keys will be printed not values
print("_" * 100)

dict1 = {"Name" : 552, "Surname" : "Rachotimath", "DOB" : "28Aug1989"}
print(dict1, type(dict1))
print(dict1, type(set(dict1)))
print(set(dict1))
var2 = set(dict1)
print(var2, type(var2)) #keys will be printed not values


############## Dict -> Boolean ##############
print("_" * 100)
dict1 = {"Name" : 552, "Surname" : "Rachotimath", "DOB" : "28Aug1989"}
print(dict1, type(dict1))
print(dict1, type(bool(dict1))) #1
var2 = bool(dict1)
print(var2, type(var2)) #2

print("_" * 100)
dict1 = {}
print(dict1, type(dict1))
print(dict1, type(bool(dict1))) #1
var2 = bool(dict1)
print(var2, type(var2)) #2


########################### SET Type casting ###########################

############## SET -> Int ##############
# Conversion is not possible

############## SET -> Float ##############
# Conversion is not possible

############## SET -> String ##############
# brackets, space, character every thing is considered as string.
print("_" * 100)
set1 = {4,5,'Santosh',6.2}
print(set1, type(set1))
print(set1, type(str(set1)))
print(str(set1))
var2 = str(set1)
print(var2, type(var2))
print(var2[4],var2[-2],var2[-5], type(var2))

############## SET -> list ##############
# brackets, space, character every thing is considered as string.
print("_" * 100)
set1 = {4,5,'Santosh',6.2}
print(set1, type(set1))
print(set1, type(list(set1)))
print(list(set1))
var2 = list(set1)
print(var2, type(var2))
print(var2[3], type(var2))

############## SET -> tuple ##############
# brackets, space, character every thing is considered as string.
print("_" * 100)
set1 = {4,5,'Santosh',6.2}
print(set1, type(set1))
print(set1, type(tuple(set1)))
print(tuple(set1))
var2 = tuple(set1)
print(var2, type(var2))
print(var2[3], type(var2))

############## SET -> dict ##############
# Conversion not possible

############## SET -> Boolean ##############
print("_" * 100)
set1 = set() # if you give set1 = {} then it considers as dict
print(set1, type(set1))
print(set1, type(bool(set1))) #1
var2 = bool(set1)
print(var2, type(var2)) #2

print("_" * 100)
set1 = {4,5,'Santosh',6.2}
print(set1, type(set1))
print(set1, type(bool(set1))) #1
var2 = bool(set1)
print(var2, type(var2)) #2

########################### Boolean Type casting ###########################

############## Boolean -> Int ##############
print("_" * 100)
bool1 = True
print(bool1, type(bool1))
print(bool1, type(int(bool1)))
var2 = int(bool1)
print(var2, type(var2)) #2

print("_" * 100)
bool1 = False
print(bool1, type(bool1))
print(bool1, type(int(bool1)))
var2 = int(bool1)
print(var2, type(var2)) #2
############## Boolean -> Float ##############
print("_" * 100)
bool1 = True
print(bool1, type(bool1))
print(bool1, type(float(bool1)))
var2 = float(bool1)
print(var2, type(var2)) #2

print("_" * 100)
bool1 = False
print(bool1, type(bool1))
print(bool1, type(float(bool1)))
var2 = float(bool1)
print(var2, type(var2)) #2

############## Boolean -> String ##############
print("_" * 100)
bool1 = True
print(bool1, type(bool1))
print(bool1, type(str(bool1)))
var2 = str(bool1)
print(var2, type(var2)) #2
print(var2[0], type(var2)) #2

print("_" * 100)
bool1 = False
print(bool1, type(bool1))
print(bool1, type(str(bool1)))
var2 = str(bool1)
print(var2, type(var2)) #2
print(var2[0], type(var2)) #2

############## Boolean -> List ##############
# Conversion is not possible

############## Boolean -> tuple ##############
# Conversion is not possible

############## Boolean -> Dict ##############
# Conversion is not possible

############## Boolean -> Set ##############
# Conversion is not possible