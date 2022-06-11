# A Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.

# Simple Dictionary
person = {
    'firstName': 'John',
    'lastName': 'Doe',
    'age': 30
}

# Using a constructor instead of the simple dictionary
person = dict(
    firstName='John',
    lastName= 'Doe',
    age=30
)

# Access a single value
print(person['firstName'])
print(person.get('lastName'))

# Add to a dictionary
person['phone'] = '555-555-5555'

# Get just the keys of a dictionary
print(person.keys())

# Get values
print(person.values())

# Get items
print(person.items())

# Make copy of a dictionary(object)
person2 = person.copy()
person2['city'] = 'Austin'
print(person2)

# Remove item
del(person['age'])
person.pop('phone')

# Clear dictionary
person.clear()

# Get length
print(len(person2))

print(person)

# List of dictionaries
people = [
  {
    'name': 'Martha',
    'age': 30
  },
  {
    'name': 'Kevin',
    'age': 25
  }
]

# Get the Object Kevin index 1 in the list with name
print(people[1]['name'])


