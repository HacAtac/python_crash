# A module is basically a file containing a set of functions to include in your application. There are core python modules, modules you can install using the pip package manager (including Django) as well as custom modules

# Core modules

'''
We can import the whole module by using the import keyword.
Or we can import specific functions by using the from keyword.
'''
#import datetime
#today = datetime.date.today() 
# import time
# timestamp = time.time()
# Pip modules
import camelcase

# Custom modules
import validator
from validator import validate_email

# import certain function from a module with from
from datetime import date 
today = date.today() 

from time import time
timestamp = time()

camel = camelcase.CamelCase()
text = 'hello there world'
print(camel.hump(text))   #hump is a method in the CamelCase module that converts a string to camel case

email = 'test@test.com'
if validate_email(email):
    print('The email is valid')
else:
    print('The email is invalid')
