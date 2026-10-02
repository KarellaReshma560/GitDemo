#User defined functions
#We want to re-use a particular code in different projects or programs we can define functions once and can use multiple times
"""SYNTAX
def function_name(arg1, arg2, .........argN):
    statement1
    statement1
    statement1
    .....
    statementN
"""
"""
#Topic 1:
#Greeting function 
def greeting_someone(name):
    print(f"Hello {name}, Good Morning!")
    print("It's a beautiful day!")

#Calling function. Function responds "N" no.of times if we call "N" no.of times
greeting_someone("Reshma")
greeting_someone("Josnikaa")


#Define function whether the number is even or odd
def even_odd(num):
    if num % 2 == 0:
        print(num, "is Even")
    else:
        print(num, "is Odd")

#call the function
even_odd(10)
even_odd(53)
even_odd(45)


#function for adding the numbers
def add(num1, num2):
    result = num1 + num2
    print(f"result: {result}")
add(1,7)
add(53,76)

#Topic 2:
#Now we can see how we can return an argument
def even_odd(num):
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"
        #print(num, "is Odd") #instead of printing it returning the result

#call the function
result = even_odd(3)
print(result)

#Topic 3:
#Returning Multiple values from function
def Arthimetic(num1, num2):
    adds = num1 + num2
    sub = num1 - num2
    mul = num1 * num2
    return adds, sub, mul

val1 = int(input("Enter the first number: "))
val2 = int(input("Enter the second number: "))
res1, res2, res3 = Arthimetic(val1, val2)

print(f"Addition of {val1} and {val2} is {res1}")
print(f"Difference between {val1} and {val2} is {res2}")
print(f"Product of {val1} and {val2} is {res3}")
"""

"""
#Topic 4:
#Types of Arguments

#Positional Arguments - passing the args in order of their position
#Complusory we need to pass both args otherwise will get error - "missing 1 required positional argument: 'b'"
def add(a,b):
    return a+b
res = add(10,5)
print(res)
"""
#Topic 5:
#Default args - the default arg become the optional
#The non-default args should NOT follow the default argument
def sub (a,b=5, c=20):
    #sub(a,b=10, c):
    print(f"{a} , {b} and {c}")
    return a - b - c
res = sub(10,70, 50)
print(res)

#Keyword argument -#we can change the order of passing the argument
res1 = sub(10, c=2, b=1)
print(res1)


