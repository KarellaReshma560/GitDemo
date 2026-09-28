'''
s1 = "Hello Reshma"
print(s1[0:10:1])
s1_sllice = s1[0:10:2]
print(s1_sllice)
print(type(s1_sllice))

#---------------------
#f-string
name = "Reshma"
age = 20
language = "English"
hours = 3
mid_1 = 20
mid_2 = 25
print(name, "is", age, "years old")
#instaed of above format we can print the output in below format with f-string
print(f"{name} is {age} years old. She studies {language} {hours} hours a day and secured total {mid_1+mid_2}")


#Escape sequences
#\n - new/nxt line
#\t - tab
#\\- backslash
# \' - inserts a single quote inside a single-quoted string

print("Hello.\nHow are you?")

print("John\t20")

print("old address\\new address")

print("Reshma is so \"beautiful\"")

print("This is Python\'s class")


#String functions

s1= "Python is fun"
print(len(s1))
print(s1*3)  #In strings * is repeatative operation

#Membership operation
# in --> it checks whether the string is present or not
print("Python" in s1) # It returns TRUE or FALSE
print("i" in s1)
print("z" in s1) #it returns FALSE becoz it is not present

#not in
print("Java" not in s1) # returns TRUE becoz it is "not in" in s1
print("Python" not in s1)


# Comparision of strings
print("Python" == "Python") #TRUE
print("Python " == "Python") #FALSE becoz we have space

#Removing spaces from a string - strip()

s1 = "Python "
s2 = s1.strip()
print(s1 , s2)
print(len(s1), len(s2))


#Replace function
a1 = "We are learning Python"
print(a1)
print(a1.replace("Python","Java"))
print(a1.replace("e","E",))
print(a1.replace("e","E",1)) #It only changes at first occurence
print(a1.replace("e","E",2))


#How to convert string into count, cases,start, end

#Count the substring - string.count(sub-string)
s1 = "We are learning Python. Python is fun"
s2 = "Python"
s3 = " "
print(s1.count(s2))
print(f"Occurences of {s2} is {s1.count(s2)}")
print(f"Occurences of space {s3} is {s1.count(s3)}")
'''

#Changing case of a string
#upper(). lower(), title(), capitalize()

s1 = "Python3.13"  #it ignores numeric
print(s1.upper())
print(s1.lower())
print(s1.title())
#startswith(), endswith()
s2= "We are learning Python"
print(s2.startswith("we")) #Case sensitive
print(s2.startswith("We"))
print(s2.endswith("We"))
print(s2.endswith("Python"))

print(s1.replace("Python", "Java"))

print(s2.replace("e","E"))
print(s2.replace("e","E",1)) #only replace function performs on first occurance from left to right of the string
print(s2.replace("e","E",2))