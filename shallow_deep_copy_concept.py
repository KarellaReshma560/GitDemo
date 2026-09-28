"""
1. first take Mutable datatypes - LISTS, SET, DICTIONARY
2. we can use Copy() function to shallow copy,
for that we need to "import copy module" to use copy function
3. We can use shallow and deep copy for lists and dictionaries as well. Below are the example for LISTS for shallow and deep copy
"""

import copy #imported copy module
"""
l1 = [1, 2.5, [10, 20, 30], "Python"]
#Copy above list #SHALLOW COPY
l2 = copy.copy(l1)
print(l2) #copied from l1 to l2

#print(id(l1)) #l1 stored in "1967516787712" location in memory
#print(id(l2)) #l2 stored in "1967519441728" location in memory

#Now change any value in l1 and check  whether l2 copied same or not
l1[0] = 100 # changed from 1 to 100 in l1
print(f"l1 is {l1}", id(l1)) #differnt memory addresses
print(f"l2 is {l2}", id(l2)) #l2 is not changed the updated value from l1

1.l1 is in different location and l2 is in different location
2.But inner list of all values of l1 and l2 shares same memory location(i.e 2.5 values in l1 and l2 sahres same memory locations)
3.From above change, we are directly changing the value fro "1" to "100" means reassigning the value, so not reflected in "l2"
"""
"""
l1[2][0] = 89 # changing 3 value(list) with first index(10 to 89) in l1
print(f"l1 is {l1}", id(l1)) #differnt memory addresses
print(f"l2 is {l2}", id(l2)) #now l2 is reflected the changes from l1


1.From above change, we are not changing or reassigning entire list [10,20,30],
just we are changing one value i.e., 10 --> 89. 
2. SO the memory address remains same both in l1 and l2, because of this change is reflecting in l2 here.
"""
#OUtput: l1 is [100, 2.5, [89, 20, 30], 'Python']
#l2 is [1, 2.5, [89, 20, 30], 'Python']

""" ***DEEP COPY******
1. To AVoid above problem, like shallow copy we use DEEP COPY concept
2. in deep copy, l1 inner list is placed in different location and l2 inner list is placed in different location.
3. Even if changes happen in l1, it is not reflected in l2, because of different locations for inner list as below
"""

l1 = [1, 2.5, [10, 20, 30], "Python"]
#Copy above list #DEEP COPY
l2 = copy.deepcopy(l1)
print(l2) #copied from l1 to l2

l1[0] = 100 # changed from 1 to 100 in l1
l1[2][0] = 89 # changing 3 value(list) with first index(10 to 89) in l1
print(f"l1 is {l1}", id(l1)) #differnt memory addresses
print(f"l2 is {l2}", id(l2)) #now l2 is reflected the changes from l1

#OUtput: l1 is [100, 2.5, [89, 20, 30], 'Python'] 1761449387008
#l2 is [1, 2.5, [10, 20, 30], 'Python'] 1761451582336
