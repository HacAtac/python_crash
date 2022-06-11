# A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string).

# List or (array)
people = ['John', 'Paul', 'Sara', 'Susan']

#Simple for loop
for person in people:
    print('Current person:', person)

# Break out of loop
for person in people:
    if person == 'Sara':
        break
    print('Current person:', person)

#Continue will skip the current iteration of the loop in this case the person Paul will be skipped
for person in people:
    if person == 'Paul':
        continue
    print('Current person:', person)

#Range, used to loop through something a specific number of times
#Using len method to get the length of the list
for i in range(len(people)):
    print('Current person:', people[i])

for i in range(0, 10):
    print('Number', i)


# While loops execute a set of statements as long as a condition is true.
count = 0
while count <= 10:
    print('The count is:', count)
    count += 1   #same as count = count + 1