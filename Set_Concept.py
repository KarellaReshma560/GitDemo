"""
#***Sets are collection of items***
1.Sets are non-sequential collection of items
2.Sets are mutable
3.Comma "," separated elements enclosed with in {}
4. Sets do not allow "duplicate elements" but lists and tuples allow duplicates
5. Use Case - we can use SET to store "passport numbers" because it should be unique
6.Concatenation not supported in SET
7.Type cast is possible in SET
8.Use "discard" function to avoid errors instead of "remove" function in a set
9.Operations in sets - Intersection(&), union(|) and difference(-)
10. Frozen sets are Immutable. we cant modify the frozen set but we can perform the Intersection(&), union(|) and difference(-) on frozen sets
"""
"""
set1 = {10, "Python", 2.5, 10}
print(set1)
print(type(set1))

#Cannot have indexing/slicing with sets
#print(set1[0]) #error - 'set' object is not subscriptable

#length of a SET
print(len(set1))

#**Operators in SET**
#Membership operator -- in, not in
nums1 = {1,2,3,4,-1}
print(1 in nums1)
print(0 in nums1)
print(2 not in nums1)

#Concatenation not supported in SET
nums2 = {10,20}
#print(nums1 + nums2) #error- it is like mathematical sets
#print(nums2 * 2) # error  - repeating is also not supported
"""
"""
#Tuples to SET typecast
weekdays = ("Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun")
print(weekdays)
print(type(weekdays))

weekdays = set(weekdays) #typecasted -  but sequence is changed
print(weekdays)
print(type(weekdays))
"""
"""
#Sets are mutable
set1 = {2, 0, -1}
print(set1)
#add() - it is ike a bag, just add the value in a bag
set1.add(5)
print(set1)

#remove() - permanent deletion from a set1
#set1.remove(0)
#print(set1)

#set1.remove(4) #error - becoz the value is not present in a set

#add() - adding same number in a set, no error and also not adding same value to a set
set1.add(5)
print(set1)
"""
"""
#discard function
set1 = {2, 0, -1}
print(set1)
set1.discard(2)
print(set1)

set1.discard(4) #discard do not give any errors if element is not present in a set
print(set1)
"""

"""****OPerations in sets*****


student1 = {"English","Maths", "CS","Chemistry", "Physics"}
student2 = {"English","Biology", "Chemistry", "Physics"}
student3 = {"Sanskrit", "Maths", "CS"}
#print(student1, type(student1))
#print(student2, type(student2))

#find common subjects of student1 and student2 - Intersection
common_subjects = student1.intersection(student2, student3) #output: set() - empty set --> because, it should be common in all 3 students
print(common_subjects, type(common_subjects))

# "&" is also used instead of Intersection
#common_subjects = student1 & student2 & student3
#print(common_subjects, type(common_subjects))

#Find all the subjects for all students - union
All_subjects = student1.union(student2, student3)
print(All_subjects, type(All_subjects))

# "|" instead of union keyword. | is not concatenation here, it is union in sets
All_subjects = student1 | student2 | student3
print(All_subjects, type(All_subjects))


#need to find the difference days : "-" or "difference" keyword
days = {"Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"}
weekends = {"Sat", "Sun"}

#weekdays = days - weekends
#print(weekdays, type(weekdays))

# or "difference" keyword
weekdays = days.difference(weekends)
print(weekdays)

#******Frozen set - Immutable **********
#General set
s1 = {1,2,3}
print(s1)
s1.add(-8)
print(s1, type(s1))

#Frozenset
fs1 = frozenset({10,20,30})
fs2 = frozenset({40,10,60})
print(fs1, type(fs1))
print(fs2, type(fs2))
#fs1.add(40)
#print(fs1, type(fs1)) #Error: 'frozenset' object has no attribute 'add'

# &, | , -  are ale to perform on sets
common_value = fs1 & fs2
print(common_value, type(common_value))

all_value = fs1 | fs2
print(all_value, type(all_value))

difference_value = fs1 - fs2
print(difference_value, type(difference_value))
"""