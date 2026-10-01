#loops are used to print the list or any values multiple times
"""
#Lists in loops
l = ["Mike", 20.5, 1995]
for i in l:
    print(i)

#String in loops
a = "Apple"
for x in a:  #here it is printing each word one by one
    print(x)

#range function
for j in range(1_5):
    #print(j)
    print("Apple")


#Nested Loops
for i in range(4):
    for j in range(3):
        print(f"i = {i}, j = {j}")
"""

#STAR Pattern LOOPS

for i in range(6): #Outer loop tells us how many "rows" to print
    for j in range(1, i+1): #Inner loop tells uos how many "*" to print
        print("* ", end=" ") # need to give empty string "end" with empty spaces, this is becoz i dont want to print continous "*" in the same line thats why we are ending it with "end ="
    print()   # it comes out of inner loop and go to next line

