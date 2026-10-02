"""
#args -  variable length positional args (0 to n)
# "*" takes all the values into arg
#args stores all the values in "tuple"
#We can use this args function when we dont know how many args need to pass into that function

def add(*args):
    #print(args,type(args))
    return sum(args)

result = add(10,20,30,4,1,2,3,6) #we can pass "N" no.of values
result1 = add(0)
print(result)
print(result1) #still it gives results as "0"


#passing no.of args in strings
def print_name(*name):
    return name
result = print_name("John", "Doe", "Mike")
#result = str(input("What is your name? "))
print(result)
"""
"""
def student_details(sid, sname, *marks):
    if len(marks) == 0:
        print(f"{sname} with stud_id  {sid} is absent for exams")
    else:
        percentage = sum(marks) / len(marks)
        print(f"{sname} with stud_id {sid} is secured {percentage}%")

student_details(101, "Doe", 87.5, 70, 60.7, 89)
student_details(106, "John", 90.2, 89, 75.3, 68)
student_details(109, "Mike", 84.5, 65, 80.7, 96)
student_details(110, "Carol")

"""
"""
# **Keyword args(**kwargs) - variable length keyword args
#kwargs is a dictionary <class 'dict'>

def func(**kwargs):
    print(kwargs, type(kwargs))

func(a=1, b=2, c=3)
func() #empty dict
"""
#Example with **kwargs
#We can not specify other args after "**kwargs"
def student_details(sid, sname, *extras, **marks): #marks is dict we need give values for each key(subject)
    if len(marks) == 0:
        print(f"{sname} is absent for exams")
    else:
        percentage = sum(marks.values()) / len(marks)
        print(f"{sname} is secured {percentage}%")
    print(f"{sname} does {extras}")
student_details(101, "Doe","tennis", math=87.5, phy=70, chem=60.7, soc=89)
student_details(101, "Mike", "cricket",math=77, phy=74, chem=66.4)
student_details(101, "Carol","dance")


