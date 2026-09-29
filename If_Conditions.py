#marks = float(input("Enter your marks: "))
'''
if marks >= 90:
    print("Grade is A")
elif  80 <= marks <= 90:
    print("Grade is B")
elif 70 <= marks <= 80:
    print("Grade is C")

else:
    print("Fail")
'''
#Nested IF
'''
if marks >= 60:
    print("Congrats you have passed the course")
    if marks >= 90:
        print("Grade is A")
    elif 80 <= marks <= 90:
        print("Grade is B")
    elif 70 <= marks <= 80:
        print("Grade is C")
    else:
        print("Grade is D")
else:
    print("Fail, better luck next time")
'''

#Ternary operators

num = int(input("Enter the number: "))
# if num % 2 == 0:
#     print("Even")
# else:
#     print("Odd")

#Syntax every condition in same line
#true-expression "if" condtion "else" false-expression

print("Even") if num % 2 == 0 else print("Odd")