# Python has functions for creating, reading, updating, and deleting files.

# Open a file
myFile = open('myfile.txt', 'w') # when we open a file, we need to close it because it is a resource

# Get some info from the file
print('Name: ', myFile.name)
print('Is Closed: ', myFile.closed)
print('Opening Mode: ', myFile.mode)

# Write to file
myFile.write('Cool Beans!')
myFile.write('\nI like beans')
myFile.close()

# Append to file
myFile = open('myfile.txt', 'a')
myFile.write('\nI also like ice cream')
myFile.close()

# Read from file
myFile = open('myfile.txt', 'r+')
text = myFile.read(10) # 10 param will read first 10 characters
print(text)
myFile.close()
