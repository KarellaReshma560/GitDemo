"""
#docstring -  1) It explains what a function, class, or module does,
detailing parameters, return values, and
expected behaviors without forcing someone to
read through the source code.
2) It is placed as the very first statement inside
the code block and is typically enclosed in
triple double quotes.
"""

# #Example1:
# def func():
#     """
#     #docstring - We can write the function does here
#     """
#     return None
# print(help(func)) # It is printing everything which is mentioned inside the "func"

#Ex 2:
def divide(num1, num2):
    """
        num1: A num to be divided (numerator)
        num2: A num to be divided (denominator)
        :return - float value
    """
    if num2 == 0:
        return "Cannot divide as denominator is 0!"
    else:
        result = num1 / num2
        return result
print(divide(13,4))