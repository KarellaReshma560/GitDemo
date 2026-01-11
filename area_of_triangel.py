"""
a = int(input("Enter first side: "))
b = int(input("Enter second side: "))
c = int(input("Enter the third side: "))
s = (a+b+c)/2
print("Semi_Perimeter = ",s)
Area = (s*(s-a)*(s-b)*(s-c)) * 0.5
print("Area = ",Area)

"""
"""
#Simple Interset = (P * R * T)/100
#P = Principal Amount
# Rate of Interest
# Time Duration

p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter  time duration: "))
s = (p*r*t)/100
print("Simple Interest: ",s)

"""

#Compund Interest

#Amount = P(1+r/100) ^ t
#Compund = A-P
p = float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter  time duration: "))
A = p * pow((1 + r/100),t)
print("Amount: ",round(A))
C = A-p
print("Compound Interest: ",round(C))


