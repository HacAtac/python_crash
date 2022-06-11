# A List is a collection which is ordered and changeable. Allows duplicate members.  Basically an array like javascript.

# Create list 
numbers = [1,2,3,4,5] # Best practice to use square brackets
print(type(numbers))
# Using a constructor
numbers = list((1,2,3,4,5)) # Same as above but using a constructor
fruits = ['Apples', 'Oranges', 'Grapes', 'Pears'] # can add other types

# Get value
print(fruits[1])

# Get len method of list
print(len(fruits))

# Append to list list method
fruits.append('Mangos')

# Remove from list list method
fruits.remove('Grapes')

# Insert into position list method
fruits.insert(2, 'Strawberries')

# Remove from position list method
fruits.pop(3)

# Reverse list method
fruits.reverse()

# Sort list method
fruits.sort()

# Reverse sort list method
fruits.sort(reverse=True)

print(fruits)