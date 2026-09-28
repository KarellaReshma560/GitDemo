"""
1.comma separated key-value pairs enclosed within {}
2. syntax: {key1:value1, key2:value2, ..........}
3. we can find the length of key-value pairs in dictionaries
4. INDEXES function is not used for dictionaries, will get error, because is not stored as LISTS in dictionaries
5. But we can fetch the "value" by the "key" in dictionaries
6. Dictionaries are Mutable, we can add, update,... the values in dictionaries
7. finding value not in the list, getting "error"
8. We can add "NEW" key-value in the dictionaries, because it is mutable
9. We can use get() function to retrieve the values, even if want to retrieve the values which are not present in the list, it wont generate error instead it give "None" in the output
10. Membership operator (IN) returns true or false as output
11. Update function, tries to concatenate 2 dictionaries into 1 dictionary
12. pop() , deletes the key-value pair in dictionary
13. working with Key-values
    a. not allowed keys - LISTS, SETS, DICTIONARIES (mutable, so we cannot use as KEYS)
    b. allowed keys - STR, INT, FLOAT, BOOLEAN, TUPLES (Immutable, so it allowed as keys)
    c. VALUES allow all datatypes
14. We can fetch only KEYS from the dictionaries with "key()" function
15. We can fetch only VALUES from the dictionaries with "values()" function
16. We can fetch both KEYS and VALUES combinedly in one list with "items()" function
#Price of groceries

grocery_list = {'milk':60, 'biscuits': 20, 'rice': 50, 'bread': 30}
print(grocery_list, type(grocery_list))

#print(len(grocery_list)) #length

#print(grocery_list[0]) #KeyError: 0 , because dictionary does not have indexes concept

#we can fetch the "value" by the "key"
#print(grocery_list['milk'])
#print(grocery_list['rice'])

#Dictionaries are Mutable
#grocery_list['milk'] = 70
#print(grocery_list)

#finding value not in the list
#print(grocery_list['eggs']) #KeyError: 'eggs'

#adding new key value in the dictionaries
grocery_list['butter'] = 100 # adds the new values
grocery_list['bread'] = 200 # updates the new value for existing list
print(grocery_list)

students1 = {"maths": 80.5, "eng":76.0, "phy": 89.0}

#fetch the marks for "phy"
print(students1["phy"])

#get()
print(students1.get("phy"))

#print(students1["chem"]) #KeyError: 'chem'
print(students1.get("chem")) #output is "None", not generating error

print(students1.get("chem", 40.0)) #just giving "40.0" instead of "None" , but not adding into original list
print(students1)


emp1 = {"id": 1001, "name": "John", "Salary": 10000}
print(emp1.get("phone")) #output : None
print(emp1.get("phone", 9672659084))

print(emp1.get("id", 9672659084)) #even if gave default value for current Key, it will return only mentioned value while we created in the dictionary

#membership operator --> in
print("name" in emp1)  #output : TRUE
print("phone" in emp1) #output : FALSE


#Semester marks for same student
sem1_marks = {"maths": 78.5, "eng": 71.0, "phy": 89.0}
print(sem1_marks)
sem2_marks = {"chem" : 81.5, "biol": 90.5, "eng": 100.0, "chem": 90.0} #if we have same key-value pair, after updating it is overriding with new key-value pair
print(sem2_marks)

#update function in dictionaries
sem1_marks.update(sem2_marks)  #we are updating sem2_marks(concatenating) with sem1_marks
print(sem1_marks)

#pop() removes the value from list
sem1_marks.pop("chem")
print(sem1_marks)

sem2_marks = {"chem" : 81.5, "biol": 90.5, "eng": 100.0, "chem": 90.5}
print(sem2_marks) #No error, just updated new for for "chem"
#from above, dictionaries will read from right --> left, so it gives updated values for that key


#Keys and Values of dictionaries

#d1 = {[1,3,5]: 9, [1,2,1]: 4}
#print(d1) #TypeError: unhashable type: 'list'
#we have used Keys as LISTS, so we get error. Keys cannot be lists

#STrings as keys
d2 = {"Nine": 9, "four": 4}
print(d2) #allowed keys are STRINGS

#Int as Keys
d3 = {1: True, 2: False}
print(d3)

#float as Keys
d4 = {1.0: True, 0.0: False}
print(d4)

#boolean as Keys
d5 = {True: 1, False: 0}
print(d5)

#Tuples as keys
d6 = {(1,3,5): 9, (1,2,1): 4}
print(d6)

#SETS as keys
#d7 = {{1,3,5}: 9, {1,2,1}: 4}
#print(d7) #TypeError: unhashable type: 'set'

#DICTIONARIES as keys
#d8 = {{'a':1, 'b': 2}: 9}
#print(d8) #TypeError: unhashable type: 'set'

#Because above are mutable, we are getting errors
"""

#Values as lists
student1 = {'id': 1, 'name': 'Reshma', 'marks': [89.5, 71, 81]}
print(student1.get('marks'))
print(student1.get('marks')[1])#it fetches value "71" from marks
print(student1['marks'][1]) #other method to retrieve

#value as dictionaries
student2 = {'id': 2, 'name': 'Manikanta', 'marks': {'eng': 89.5,'maths': 71, 'bio': 81}}
print(student2.get('marks'))
print(student2.get('marks')['bio'])

#fetch the keys from dictionaries key()
print(student2.keys()) #output : dict_keys(['id', 'name', 'marks'])
print(type(student2)) #class : dict

#fetch the VALUES from dictionaries values()
print(student2.values()) #output : dict_values([2, 'Manikanta', {'eng': 89.5, 'maths': 71, 'bio': 81}])
print(type(student2)) #class : dict

#items(), we can pair both keys() and values()\
print(student2.items(), type(student2.items()))
#output: dict_items([('id', 2), ('name', 'Manikanta'), ('marks', {'eng': 89.5, 'maths': 71, 'bio': 81})]) <class 'dict_items'>

