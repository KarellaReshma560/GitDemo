"""
It is an iterator based loop which steps through the items of a collection
(lists, tuples, sets, dict, str) and executes a block of code repeatedly
for a no. of times equal to items/elements of that collections


percents = [85.5, 70, 69.8, 80, 91.4] #each repeation is called iteration
for i in percents:   #automatic incrementation and overrides i value every time from above list
    print(i)


s1 = "Hello Reshma"
for i in s1:
    print(i)
"""
"""

s2 = {'emp_id': 101, 'name': "Reshma", 'city': "Ottawa", 'dept': "HR"}
print(s2.items())
# for j in s2:
#     #print(j) # only returns the key not value
#     print(j, s2[j])

#2 different types
for j in s2.items():
    print(j)


#Range() --> It is built-in function used to generate the sequence of integers in a given int list
#for var in range(start, stop, step)

# for i in range(1,11,2):
#     print(i)

#generate even numbers from the given numbers
# for j in range(2,11,2):
#     print(j)

#reverse order from 20 to 10(excluding 10)
# for k in range(20, 10, -2):
#     print(k)
# print("Good")


#Second syntax without "STEP" and "START"
for j in range(5): #"step" default is "1" and "Start" default is "1"
    print(j)

#print the index of list items using range()
groceries = ['salt', 'sugar', 'milk', 'bread']
print(groceries)
for i in range(0, len(groceries), 1):
    print(i)


#Below are the profits in Q1, Q2, Q3 and Q4
profits = [9, 12, 7, 14]

for index in range(len(profits)):
    #print(index) # gives the index values(0,1,2,3)
    q = index + 1
    print(f"Quarter{q} is ", profits[index]) # gives the values of profits(9, 12, 7, 14)

"""

"""
scores = [2,17, 100, 5, 8, 4.5, 6 , 2 , 90]
#total = 0
# for i in scores:
#     total = total + i
#INSTEAD of "for loop" we can use Sum()

# total = sum(scores)
# print(total)

#find highest value

#highest = scores[0]
# for i in scores:
#     if highest < i:
#         highest = i

#Instead of "for loop" we can use max() and min()
highest = max(scores)
print(f"Highest values from scores is {highest}")

lowest = min(scores)
print(f"Highest values from scores is {lowest}")



#CONTINUE and BREAK concept

# for i in range(1, 20):
#     if i % 3 == 0:
#         continue # continues to print the values which satisfies above condition
#     print(i)

for i in range(1, 20):
    if i % 3 == 0:
        break
    print(i) #op: 1,2--> becoz 3%3 == 0, it terminates the for loop becoz it is break
"""

#WHILE LOOP

# num = 1
# while num < 5:
#     print(num)
#     num = num + 1

#INFINITE WHILE LOOP
# while True:
#     print("Hello")

#Ex: if we want to run continuously, but after certain condition come out of the loop
correct_password = "Python"
attempt = 0
max_attempt = 3
while True: #infinite loop
    user_password = str(input("Enter your password: "))
    if user_password == correct_password:
        print("Correct Password")
        break
    else:
        attempt = attempt + 1
        print("Incorrect Password")
        if attempt > max_attempt:
            print("No. of attempts done, Try again after some time")
            break

print("Logged in")

