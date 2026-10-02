"""
1. lambda function is a small, anonymous function
that can be defined in a single line of code
2. Filter fun() will keep the values of sequence list/tuples which returns TRUE,
and discard(filtered out) the values which returns FALSE
3. Map()  stores the output(TRUE/FALSE) of all the elements in a map object
It create a map object which it returns TRUE, and also stores False in map object
"""
#filter(function, sequence)

seq = [1,2,3,4,5,6]
#odd = lambda x: True if x % 2 != 0 else False
#Instead of writing lambda function and assigned to variable "odd" will directly write in "filter function"
filtered_output = filter(lambda x: True if x % 2 != 0 else False, seq)
print(filtered_output)
print(f"Odd numbers in above seq are : {list(filtered_output)}")

#map() example
seq1 = [1,2,3]
mapped_output = map(lambda x: x ** 2, seq1)
#from above map object stores all the output from lambda function.
print(mapped_output)
print(f"Map output : {list(mapped_output)}")