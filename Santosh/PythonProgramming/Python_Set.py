"""
################################# Python Set #################################
"""
set1 = {1, 4, 6, 7, 'a', 'b', 'c', 4, 6}

print(set1, type(set1))

'''
1. Set is mutable data typre
2. set has only uniques data values, duplicate values are npt allowed
3. Only immutable data  type can be member of set 
4. Set store data in random, it does not follow any sequencing.

'''

# Apply loop on set

set1 = {1, 4, 6, 7, 'a', 'b', 'c', 4, 6}
for val in set1:
    print(val)

print(dir(set))
# ['__and__', '__class__', '__class_getitem__', '__contains__', '__delattr__', '__dir__', '__doc__',
# '__eq__', '__format__', '__ge__', '__getattribute__', '__getstate__', '__gt__', '__hash__',
# '__iand__', '__init__', '__init_subclass__', '__ior__', '__isub__', '__iter__', '__ixor__',
# '__le__', '__len__', '__lt__', '__ne__', '__new__', '__or__', '__rand__', '__reduce__',
# '__reduce_ex__', '__repr__', '__ror__', '__rsub__', '__rxor__', '__setattr__', '__sizeof__',
# '__str__', '__sub__', '__subclasshook__', '__xor__', 'add', 'clear', 'copy', 'difference',
# 'difference_update', 'discard', 'intersection', 'intersection_update', 'isdisjoint', 'issubset',
# 'issuperset', 'pop', 'remove', 'symmetric_difference', 'symmetric_difference_update', 'union',
# 'update']

################################# Set methods #################################

#####################   Add method  #####################
# Add method - THis method helps to ass datat to set
print('-' * 50)
set1 = {1, 2, 3}

set1.add(4)
print(set1)

set1.add('Hello')
print(set1)

#####################   Union method  #####################
# Union method - THis method helps to combuine to sets and create new set
print('-' * 50)
set1 = {1, 2, 3}
set2 = {1, 2, 4, 5, 6, 'Hello'}

set3 = set1.union(set2)
print(set3)

#####################   Update method  #####################
# Update method - THis method helps to one set data to another set
print('-' * 50)
set1 = {1, 2, 3, 'San'}
set2 = {1, 2, 4, 5, 6, 'Hello'}

set1.update(set2)
print(set1)

#####################   Remove method  #####################
# remove method - THis method helps to one data to another set
print('-' * 50)
set1 = {1, 2, 3, 'San'}

set1.remove(1)
print(set1)

#####################   discard method  #####################
# remove method - his method remove data from set if it is available, if not then does not throw any error.
print('-' * 50)
set1 = {1, 2, 3, 'San'}

set1.discard(2)
print(set1)

set1.discard(100)  # does not throw any error
print(set1)

#####################   pop method  #####################
# pop method - This method remove any random data from set and return it.
print('-' * 50)
set1 = {1, 2, 4, 5, 6, 'Hello'}

res = set1.pop()
print(res)

#####################   Clear method  #####################
# Clear method - This method to clears all the data from set.
print('-' * 50)
set1 = {1, 2, 4, 5, 6, 'Hello'}

set1.clear()
print(set1)  # set()




#####################   Difference method  #####################
# Difference method - This method return difference between two sets.
print('-' * 50)

set1 = {1, 2, 4, 5, 6, 'Hello'}
set2 = {1, 4, 6, 7, 'a', 'b', 'c', 4, 6}

diff_val_1_to_2 = set1.difference(set2)
diff_val_2_to_1 = set2.difference(set1)

print('Difference between set1 to set2 : ', diff_val_1_to_2)
print('Difference between set2 to set1 : ', diff_val_2_to_1)

#####################   Difference Update method  #####################
# Difference Update method - This method updates the difference between two sets and does not return any value
print('-' * 50)

set1 = {1, 2, 4, 5, 6, 'Hello'}
set2 = {1, 4, 6, 7, 'a', 'b', 'c', 4, 6}

set1.difference_update(set2)
set2.difference_update(set1)

print('Difference between set1 to set2 : ', set1)
print('Difference between set2 to set1 : ', set2)


#####################   Intersection method  #####################
# Difference Update method - This method this method will return common values between two sets.
print('-' * 50)

set1 = {1, 2, 4, 5, 6, 'Hello'}
set2 = {1, 4, 6, 7, 'a', 'b', 'c', 4, 6}

intersect_output1 = set1.intersection(set2)
intersect_output2 = set2.intersection(set1)

print(intersect_output1)
print(intersect_output2)

#####################   Intersection Update method  #####################
# Difference Update method - This method this method will return common values between two sets.
print('-' * 50)

set1 = {1, 2, 4, 5, 6, 'Hello'}
set2 = {1, 4, 6, 7, 'a', 'b', 'c', 4, 6}

set1.intersection_update(set2)
set2.intersection_update(set1)

print(set1)
print(set2)


#####################   Symmetric Difference  method  #####################
# Symmetric Difference method - This method gives common values between two sets and create a new set.
print('-' * 50)

set1 = {1, 2, 3, 4, 5, 6, 'Hello'}
set2 = {4, 5, 6, 7, 'a', 'b', 'c'}

intersect_output1 = set1.symmetric_difference(set2)
print('symmetric_difference: ', intersect_output1)



#####################   Symmetric Difference  Update method  #####################
# Symmetric Difference Update method - This method returns common values between two sets and create a new set.
print('-' * 50)

set1 = {1, 2, 3, 4, 5, 6, 'Hello'}
set2 = {4, 5, 6, 7, 'a', 'b', 'c'}

set1.symmetric_difference_update(set2)
print('symmetric_difference update:  ', set1)


#####################   subset and super set  #####################
# subset and super set method -
print('-' * 50)

set1 = {1, 2, 3, 4, 5, 6, 'Hello'}
set2 = {4, 5, 6}
set3 = {4, 5, 6, 9}

print('Is super set : ', set1.issuperset(set2))
print('Is sub set : ', set2.issubset(set1))

print('Is super set : ', set1.issuperset(set3))
print('Is sub set : ', set3.issubset(set1))


#####################   Deep copy  #####################
# Shallow copy
print('-' * 50)

set1 = {1, 2, 3, 4, 5, 6, 'Hello'}
set2 = set1
set1.add(100)
print('Shallow copy: ',set1)
print('Shallow copy: ',set2)


# Deep copy
print('-' * 50)
set1 = {1, 2, 3, 4, 5, 6, 'Hello'}
set2 = set1.copy()
set2.add(99)
print('Deep copy: ',set1)
print('Deep copy: ',set2)

