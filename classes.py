# A class is like a blueprint for creating objects. An object has properties and methods(functions) associated with it. Almost everything in Python is an object

# Create class
class User:
    # Constructor
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age

    # Method #1
    def greeting(self):
        return f'My name is {self.name} and I am {self.age}'

    # Method #2
    def hasBirthday(self):
        self.age += 1

# Extend class with another class
class Customer(User):
    def __init__(self, name, email, age):
        self.name = name
        self.email = email
        self.age = age
        self.balance = 0

    # Method
    def setBalance(self, balance):
        self.balance = balance

    # take greeting from parent class
    def greeting(self):
        return f'My name is {self.name} and I am {self.age} and I have a balance of {self.balance}'

# Initialize user object
jordan = User('Jordan Hackworth', 'jhack00@icloud.com', 32)
monique = User('Monique Hackworth', 'm.woodward1411@gmail.com', 30)

# edit property
jordan.name = 'HacAtac'

jordan.hasBirthday()

#Call Method
print(jordan.greeting())

# Init customer 
john = Customer('John Doe', 'john@gmail.com', 40)

john.setBalance(500)

print(john.greeting())


