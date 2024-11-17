# IF / Else conditions are used to decided to do something based on something being true or
# false
x = 10
y = 10



# Comparison Operators(== , !=, <, >, <=, >=) - Used to compare values

if x > y:
    print(f"{x} is bigger than {y}")

elif x == y:
    print(f"{y} is equal to {x}")

else:
    print(f"{y} is bigger than {x}")

# Logical Operators (and, or, not) - Used to combine conditional statements


# Membership Operators (not, not in) - Membership operators are used to test if a sequence
# is presented in an object

numbers = [1,2,3,4,5]
x = 40
if x in numbers:
    print(x in numbers)

if x not in numbers:
    print(x not in numbers)

# Identity Operators (is, is not) -  Compare the objects, not if they are equal, but if they
# are actually the same object, with same memory location

# is
#x = y
if x is y:
    print("They have same memory location")

x = 10
if x == y:
    print("They have the  same value")

