#Tuple Concept
#Sequence of items as a collection of list with different datatypes
#In Tuple elements are fixed we cannot modify it permanently(we can't delete or add or modify the tuple)
#Lists can be used where we want to modify the elements
#Tuples are enclosed in parathesis and also store different datatypes like below
"""
t1 = ("Python", 10, 1.5, True, [1, 2, 4], (10, 20))
#print(t1)
#print(len(t1)) #to run the program press SHift+f10

#Accessing items of a tuple - index
#print(t1[0])
#print(t1[-1])
#print(t1[4][0]) #returns 1 from the list [1,2,4]

# t2 = 10, 20, 30  #if we didn't mention round brackets but default it is taking as tuple
# print(t2)
# print(type(t2))
# l1 = [1, 2, 3]
# print(type(l1), type(l1))
# t3 = tuple(l1)  #type casted from list to tuple
# print(t3, type(t3))

fruits = ("Apple", "Orange", "Mango")
print(fruits, type(fruits))
fruits = list(fruits)   #we reassigned the variable from tuple to lists here
print(fruits, type(fruits))
#we cannot do append or any modification on tuple, but if we want to modify the list first will type cast from tuple to list
#and modify the changes and again type cast to tuple from the list.
"""

"""
Operations on tuples

Concatenation, repetition, membership
count, index
min, max, sum
"""

"""
student_details1 = (1001, "John")
student_details2 = (78.5, 91.0, 83.5, 79.5)

# '+' used to concatenate above 2 tuples
student_details = student_details1 + student_details2
#print(student_details)

# '*' used to repeat the tuples
# t1 = ("class 5 fee", 5000)  # same fee for all members in class 5
# print(t1 * 3)

# membership operator "in", "not in"
# print(83.5 in student_details) #correct TRUE
# print(72 in student_details) #Incorrect FALSE
#
# print(83.5 not in student_details)
# print(72 not in student_details)

# Count
t1 = (10,1,3,5,1,8,5,5,1,7)
#syntax - tuple.count(element)
#print(t1.count(1)) #print 3 as '1' has 3 times

#index function used in lists and tuples
#syntax - tuple.count(element)
#print(t1.index(5)) #what is the index of '5' in the tuple t1?
#it returns 3 because '5' is stored in index 3 from above list

#print(t1.index(40)) # not in the list so it gives error

print(t1.index(1)) # here it only provides first occurrence from the tuple

#min, max, sum
print(f"Smallest number : {min(t1)}")

print(f"Biggest number : {max(t1)}")

print(f"Total : {sum(t1)}")

"""

#***Mutable and Immutable***
#Lists are mutable becoz it can change the existing list
#Tuples and strings are immutable becoz they wont change the existing list

#Strings example -- immutable
s1 = "Python is fun"
s2 = s1.replace("Python", "Java")
print(s1) #existing string is not changing until and unless we are assigning replace function to a new variable s2
print(s2)

#Lists example -- mutable
#***One more imp thing that lists should not change their memory address as they are mutable***
l1 = ["Mango", "Apple", "Orange"]
print(l1)
print(id(l1))  #id (2791777084416)-- is to check memory address of the list l1
l1.append("Kiwi")
print(l1)   #id (2791777084416)-- is to check memory address of the list l1 after changes done
print(id(l1))
l1.sort()
print(l1)
print(id(l1))
l1.remove("Orange")
print(l1)

#replace the values in the list with index
print(l1) #['Apple', 'Kiwi', 'Mango']
l1[-1] = "Pear" # replacing Mando with Pear
print(l1)

#Tuples - immutable
fruits = ("Apple", "Orange", "Mango")
fruits[-1] = "Pear"
print(fruits) # error - 'tuple' object does not support item assignment

