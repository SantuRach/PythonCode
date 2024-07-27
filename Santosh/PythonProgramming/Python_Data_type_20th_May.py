
########### list ##############
# print("_" * 100)
list1 = [1,2,3,4,[5,6,7],(7,8,9)]
print(list1)
print(list1[4])
print(list1[4][0])


########### Tuple ##############
print("_" * 100)

s1 = [5,6,7]
s2 = (7,8,9)
tup1 = [1,2,3,4,s1,s2]

# here the list is modified not tuple. tuple is immutable
print(s1)
s1.append(10)
print(s1)
print(tup1)


########### Dictionary ##############
print("_" * 100)

dict1 = {
            'Name'  : 'Santosh is a boy',
            'Age'   : 36,
            (1,2,3) : [4,5,6],
            'Hello' : {'a': 987, 345 : "Hello hi"}
}
print(dict1)
print(dict1['Age'])
print(dict1[(1,2,3)])
print(dict1['Hello'])
print(dict1[(1,2,3)][-1])
print(dict1['Hello']['a'])
print(dict1['Hello'][345])
print(dict1['Hello'][345][-2])
print(dict1['Hello'])
