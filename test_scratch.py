import json

with open('books.json', 'r') as f:
    data = json.load(f)
    print(data['books'])