# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
"""

x = 1            # int
y = 2.5          # float
name = 'Jordan'  # string
isCool = True    # bool (boolean)

# Multiple assignment
x, y, name, isCool = (1, 2.5, 'Jordan', True) 
print('data types', x, y, name, isCool)  # Same as console.log() in JS

# Basic math
a = x + y # Addition
s = x - y # Subtraction
m = x * y # Multiplication
d = x / y # Division
r = x % y # Modulus
e = x ** y # Exponent

# Casting (converting) variables to different types
x = str(x)
y = int(y)
z = float(y)

# Check type
print(type(z))
print(z)




