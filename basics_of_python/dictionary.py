# A dictinary is a collection which is unordered, changeable and indexed. No duplicate members.

# Create dict

person = {
    "first_name": "John",
    "last_name":"Doe",
    "age":30
}

# Use constructor
person2 = dict(first_name="Sarah",last_name="Doe",age=30)

print(person, type(person))
print(person2, type(person2))
print(person['first_name'])
print(person.get('last_name'))

# Add key, value

person['phone'] = '555-555-555'
print(person)

# Get keys or values or items
print(person.keys())
print(person.items())
print(person.values())

#person2 = person.copy()
person2 = person
person2["key01"] = "value01"

del(person["age"])

person.clear()
print(person)


# List dict

people = [
    {
        "name":"ali",
        "surname":"durmaz",
        "age":32
    },
    {
        "name":"kadir",
        "surname":"bulur",
        "age":17
    }
]


people.append({
    "name":"fatih",
    "surname":"kadir",
    "age":23
})

print(people)
print(people[0]["name"])
