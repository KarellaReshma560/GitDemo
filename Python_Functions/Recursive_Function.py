"""
#Recursive Function - It is a function calls itself till a certain condition is not "MET"
#There are 2 parts to any recursive function
1. Base/terminal condition
    Ex: As soon as my number becomes 1, need to stop
2. Recursive condition
    Ex: step 1 -> n * (n-1)!
        step 2 -> n * (n-1) * (n-2)!
        .....

"""
#Ex: Factorial of n ==> n * (n - 1) * (n -2) * ....2 * 1
#4! ==> 4 * 3 * 2 * 1 = 24

def factorial_rec(n):
    if n == 1:
        return 1
    else:  #it calls everytime until it satisfies "if" condition == 1
        factorial = n * factorial_rec(n-1) #function calls itself here (Recursive function)
        return factorial


n = int(input("Enter a number: "))
print(f"Factorial of {n} is {factorial_rec(n)}")

