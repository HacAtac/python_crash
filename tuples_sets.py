# A Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Simple tuple
fruitTuple = ('Apples', 'Oranges', 'Grapes')
# Using constructor tuple
fruitTuple = tuple(('Apples', 'Oranges', 'Grapes'))

# Get single value 
#print(fruitTuple[1])

# Can not change value
# fruitTuple[1] = 'Grape'  # This will throw an error because tuples are unchangeable

# Tuples with one value should have trailing comma
fruitTuple2 = ('Apples',)

del fruitTuple2 # Delete tuple

# Get length of tuple
#print(len(fruitTuple2))


# A Set is a collection which is unordered and unindexed. No duplicate members.
'''
 SETS
'''
# Create set
fruitSet = {'Apples', 'Oranges', 'Mango'}

# Check if in set
print('Apples' in fruitSet)

# Add to set
fruitSet.add('Grape')

# Remove from set
fruitSet.remove('Grape')

# Clear set
fruitSet.clear()

# Delete set (not recommended) (completely deletes the set)
del fruitSet

print(fruitSet)
