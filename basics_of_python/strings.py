#strings in python are surronded by double or single quotation marks. Let's look at string formatting
# and some string methods.

name = "Brand"
age = 36

print("Hello, my name is " + name + " and I am " + str(age) + " years old.")

# String formatting

#Arguments by position
print("Hello, my name is {name} and I am {age} years old".format(name=name,age=age))

# f string 
print(f"Hello, my name is {name} and I am {age} years old")

#String methods 

s = "helloWorld"

print(s.capitalize())
print(s.count("l"))

print(s.upper())
print(s.lower())
print(s.swapcase())
print(len(s))
print(s.replace("World","place"))
print(s.find("r"))
print(s.isalnum())
print(s.isalpha())
print(s.isnumeric())
