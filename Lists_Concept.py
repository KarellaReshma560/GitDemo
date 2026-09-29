'''
#Lists Concept
name = "Reshma"
age = 20
percent = 85

student = [name, age, percent] # we can store any kind of data type in lists(int,float,string)
# print(student)
# print(type(student))

days_of_week = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
print(days_of_week[1:6])
print(days_of_week[-5:-2])
print(days_of_week[:6])
# print(days_of_week[8]) #generate error becoz of out of range


#Slicing of Lists

l1 = [3, 8, 1, 0, 4, 9, 7, 3, 6]
print(l1[1:6:1])
print(l1[1:6:2]) #[start:stop:step] for slicing


#Concatenation of string
l1 = [1, 7,2]
l2 = [0, 5]
print(l1 + l2)
print(l2 + l1)
print(l2 + l2)

print(l1*2) # repeatative of list

#Append()

fruits = ["apple", "banana", "cherry"]
print(fruits)
fruits.append("Kiwi")
print(fruits)

# print(fruits.append("orange"))
# we are getting output as "none", becoz append function can not create new list like "replace function did".
#This is called Mutability. Becoz we can use replace function for strings and give new string from previous functions
#for append function first to append and later print the list than will see the result.

#insert function
#adds an element before the specified index
#syntax : list.insert(index, item)

fruits.insert(2, "orange")
print(fruits)
# fruits.remove("orange")



#extend, remove, pop functions
#extend adds elements in list

fruits = ["apple", "banana", "cherry"]
print(fruits)
# fruits.append(["Kiwi", "Grapes"])
# print(fruits)# append only adds 1 element at a time
# print(len(fruits))

#Comapre the diffreneces for append and extend by commenting
#Append only adds 1 argument but extend adds more than 1 argument(but need to give in list format)
fruits.extend(["orange", "kiwi", "orange"])
print(fruits)# extend adds more than 1 element in the lists and adds in the ending of the list
print(len(fruits))

fruits.remove("orange") #if we have multiple varaibles, and try to delete it always delete the 1 occurance in the list
print(fruits)

#pop() function is also used to delete the variables with index
print(fruits)
# fruits.pop(2) # it deletes with the index value
# print(fruits)
# fruits.pop(-1)
# print(fruits)
fruits.pop() # by default if we didnt gave anything it can delete the last element
print(fruits)


#reverse, sort, count, membership functions

days_of_week = ["Mon", "Tue", "Wed", "Thur", "Fri", "Sat", "Sun"]
print(days_of_week)

days_of_week.reverse()
print(days_of_week) #it is permanent change in the list

days_of_week.sort() # it is sorting based on alphabetical order A to Z (By default Ascending order)
print(days_of_week)

nums = [4,1,8,3,0,4,8,9,8,3] #Default sort is Ascending order
nums.sort(reverse=True) # Descending order or reverse order
print(nums)

#count()
print(nums.count(4)) # it gives how many times 4 is present in the list

#dynamic count for numbers
print("Enter the number from above list to see the count: {nums}")
item_to_count = int(input("Enter the number to count: "))
c = nums.count(item_to_count)
print(f"Occurence of number is : {c}")


#dynamic count for strings
language = ["Python", "Java", "Perl", "Python", "Perl", "C", "C++", "C", "Java"]
print("Enter the language from above list to see the count: {language}")
item_to_count = input("Enter the string to count: ")
c = language.count(item_to_count)
print(f"Occurence of string is : {c}")

#membership operator means "in" returns TRUE if item is present
language = ["Python", "Java", "Perl", "Python", "Perl", "C", "C++", "C", "Java"]
print("Python" in language)
print("Unix" in language)
print("Python" not in language) #reverse operation for "in"


#Numerical functions
nums = [4,1.1,8,3,10,4,8,9,8,3,2.5]
#min()
print(f"minimum number from list : {min(nums)}")
print(f"maximum number from list : {max(nums)}")
print(f"Total number from list : {sum(nums)}")


#List inside a list (nested list)

l1 = [5, 1.5, "Python", True, None, [1,2,3,[4,5,6]], 10]
print(f"Length of the list : {len(l1)}")
print(l1)
print(l1[2:])
print(l1[-2])
#fetch the numbers from above list [1,2,3]
print(l1[-2][0])
print(l1[-2][-1])
print(l1[-2][-1][0]) #lists inside list inside list
'''

#for loop
thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
    print(thislist[i])

#While loop for lists
list1 = ["apple", "banana", "cherry"]
i = 0
while i < len(list1):
    print(list1[i])
    i = i + 1

