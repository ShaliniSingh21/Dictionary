import json

blog = {'URL': 'datacamp.com', 'name': 'Datacamp'}
print(type(blog))
json_data = json.dumps(blog)
print(json_data)
print(type(json_data))