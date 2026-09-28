"""
1. =, !=, <, >, ==
2.If condition is true, it returns the result or FALSE it returns other result
3.Indentation(4 spaces) is main thing for the conditional statements

Syntax: IF
if condition:
    statement1
    statement2
    ..........
    statementN
statement end #(end block)
#whatever in the end block statement,
it will automatically print in the output

age = float(input("What is your age?: "))
if age >= 18:
    print("You are Major, you can cast vote")
print("Proceed next")
"""
"""
Syntax: IF-ELSE
if condition: #if condition is TRUE, it goes "if" block
    statement1
    statement2
    ..........
    statementN
else:   #if condition is FALSE, it goes "else" block
    statement1
statement end #(end block)

age = float(input("What is your age?: "))
if age >= 18:
    print("You are Major, you can cast vote")
else:
    print("You are Minor, you can't cast the vote")
    print("Please contact 'X' person to guide")
print("Proceed next")

#Write a program to int odd or even
num = int(input("Enter a number: "))
if num%2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")
print("Good job")
"""
"""
Syntax: IF-ELIF-ELSE
if condition: #if condition is TRUE, it goes "if" block
    statement1
    statement2
    ..........
    statementN
elif:
    statement1
else:   #if condition is FALSE, it goes "else" block
    statement1
statement end #(end block)
"""
"""
If marks is 90, Grade A
80 and 89, Grade B
70 and 79, Grade C
60 and 69, Grade D
< 60, Grade F
"""
marks = int(input("Enter marks: "))
if marks >= 90:
    print("Grade A")
elif marks >= 80 and marks <= 89:
    print("Grade B")
elif marks >= 70 and marks <= 79:
    print("Grade C")
elif marks >= 60 and marks <= 69:
    print("Grade D")
else:
    print("Grade F")