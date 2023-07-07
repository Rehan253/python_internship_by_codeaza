import json

# JSON Serialization
data = {
    'name': 'Rehan',
    'age': 24,
    'city': 'Lahore'
}

json_str = json.dumps(data)
print(json_str)

# JSON Deserialization
json_str = '{"name": "Rehan", "age": 24, "city": "Lahore"}'

data = json.loads(json_str)
print(data['name'])
print(data['age'])
print(data['city'])

# Reading and Writing JSON Files
data = {
    'name': 'John Doe',
    'age': 30,
    'city': 'New York'
}

# Writing JSON to a file
with open('output.json', 'w') as json_file:
    json.dump(data, json_file)

# Reading JSON from a file
with open('output.json') as json_file:
    data = json.load(json_file)
    print(data)
