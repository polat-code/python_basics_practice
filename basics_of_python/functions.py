# A function is a block of code which only runs when it is called.In python, we do not use
# curly brackets, we use indentation with tabs or spaces

def sayHello(name="default"):
    print(f"Hello {name}")

sayHello("Özgürhan")
sayHello()


# return values

def getSum(num1, num2):
    total = num1 + num2
    return total

print(getSum(1.5,2))


# A lambda function is a small anonymous function
# A lambda function can take any number of arguments, but can only have one expression. Very
# similar to JS arrow function
# 
# variable = lambda parameter1 , parameter2,.. :(arrow) return value
getSum = lambda num1,num2: num1 + num2

print(getSum(10,72))