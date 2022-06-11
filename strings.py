# Strings in python are surrounded by either single or double quotation marks. Let's look at string formatting and some string methods

name = 'Jordan'
age = 32 

# Concatenate strings
print('Hello, my name is' + name + 'and I am ' + str(age) + 'years old.')

'''

    String Formatting

'''
# Arguments by position
print('{}, {}, {}'.format('a', 'b', 'c')) 
print('{2}, {1}, {0}'.format('a', 'b', 'c'))

# Arguments by name
print('My name is {name} and I am {age} years old.'.format(name=name, age=age))

# F-Strings (only in Python 3.6+)
print(f'My name is {name} and I am {age} years old.')   # this is the preferred way to format strings in Python 3.6+

'''
 String Methods
'''
s = 'hello there world'

# Capitalize first letter 
print(s.capitalize())  

# Capitalize all letters 
print(s.upper()) 

# Count the number of characters in a string # String Method
print(s.lower()) 

# Swap case
print(s.swapcase())

# Get length
print(len(s))

# Replace
print(s.replace('world', 'everyone'))

# Count
sub = 'h'
print(s.count(sub))

# Starts With
print(s.startswith('hello'))

# Ends With
print(s.endswith('d'))

# Split into a list
print(s.split()) # splits into an array of strings

# Find position
print(s.find('r'))

# Is all alphanumeric
print(s.isalnum())

# Is all alphabetic
print(s.isalpha())

# Is all numeric
print(s.isnumeric())



