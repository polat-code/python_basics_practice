# A List is a collection which is ordered and changeable. Allows duplicate members.

# Create list.

numbers = [1,2,3,4,5]
for number in numbers:
    print(number)

# Use a constructor
#numbers = list((1,2,3,4,5))

fruits = ["apple","oranges","pears"]

# Get a value
print(fruits[1])

# Get length of list
print(len(fruits))

fruits.append("banana")

fruits.insert(2,"ananas")


print(fruits.index("oranges"))
fruits.reverse()

print(fruits)

fruits_string = list(map(lambda fruit : print("fruit : " + fruit) ,fruits))
