'''
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

'''

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