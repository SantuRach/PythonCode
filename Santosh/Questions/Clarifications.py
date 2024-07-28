
############## List -> Dict ##############
# Direct conversion to dict is not possible.
# zip function to be used to convert
# two list should be present to map key and Value
print("_" * 100)
list4 = [4,5,'Santosh',6.2,{1,2,3,4}]
list5 = ['a',123,'Rachotimath','Santosh',{4,5,6,7}]
print(list4, type(list4))
print(list5, type(list5))
output1 = dict(zip(list4, list5))
print(output1, type(output1))
print(output1[4], type(output1))
print(output1[6.2], type(output1))
print(output1['Santosh'], type(output1))

# From Santosh 28-07-1989
# 1. Why tuple inside the list is not converting to dict ?
# Note: If I replace {1,2,3,4} with float/int/string and {4,5,6,7} with float/int/string, program is working fine
