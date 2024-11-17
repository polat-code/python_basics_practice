# A for loop is used for iterating over a sequence (that is either a list, a tuple, 
# a dictionary, a set, or a string)

people = ["john","paul","sara","susan"]

for person in people:
    if person == "sara":
        #continue
        #break
        pass
    print(f"Current person : {person}")


# range

for i in range(len(people)):
    print(people[i])

# While loops execute a set of statements as long as a condition is true.
count = 0
while(count <= 10):
    print(f"count : {count}")
    count += 1


