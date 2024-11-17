# Tuple is a collection which is ordered and unchangeable. Allows duplicate members.

# Create Tuple

fruits = ("Apple","Pears","Oranges")
#fruitsTup = tuple(("Apple","Pears","Oranges"))

# Confusion for str and tuple

fruits2 = ("Apple",) # fruits2 is a tuple

print(type(fruits2))

fruits2 = ("Apple") # Fruits2 is a str

print(type(fruits2))

print(fruits[1])

# A Set is a collection which is unordered and unindexed. No duplicate members.

# Create a set

fruits_set = {"Apples","Oranges","Mango"}
print(fruits_set)
fruits_set.add("Pears")
print(fruits_set)

# deleting variable
#del fruits_set

print("Apples" in fruits_set)