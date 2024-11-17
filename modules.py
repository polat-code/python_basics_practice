# A module is basically a file containing a set of functions to include in your application.
# There are core python modules (individual python file is a module), modules you can install
# using the pip package manager (including Django) as well as custom modules.

import datetime
#today = datetime.date.today()

from datetime import date
print(date.today())

from validator import validate_email

email = "ozgurhan.45@gmail.com"

if validate_email(email):
    print("Valid Email")
else:
    print("Invalid Email")


    
