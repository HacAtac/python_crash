# JSON is commonly used with data APIS. Here how we can parse JSON into a Python dictionary

import json

# Sample JSON
userJSON = '{"firstName": "John", "lastName": "Doe", "age": 30}'

# Parse JSON to dictionary or (Object)
user = json.loads(userJSON) # in JS its JSON.parse

print(user)
print(type(user))
print(user['firstName'])

# Parse Dictionary to JSON
car = {'make': 'Ford', 'model': 'Mustang', 'year': 1970}
carJSON = json.dumps(car)

print(carJSON)
print(type(carJSON))
print(car["make"])
