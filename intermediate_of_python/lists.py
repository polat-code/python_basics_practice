my_list = ["banana","apple","orange"]

for item in my_list:
    print(item)


my_list[1] = "mango"
my_list.append("apple")
my_list.insert(2,"pears")
print(my_list)

my_list.remove("banana")
print(my_list)
last_element = my_list.pop()
print(last_element)
print(my_list)

print("apple" in my_list)
print(len(my_list))
my_list_copy =  my_list.copy()
my_list_copy.append("apple")

print(my_list)
print(my_list_copy)

print(my_list.clear())


