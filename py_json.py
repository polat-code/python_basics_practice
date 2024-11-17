
import json

data = '{"first_name":"Özgürhan","last_name":"Polat","age":25}'

user = json.loads(data)

print(user)
print(type(user))
print(user["first_name"])


