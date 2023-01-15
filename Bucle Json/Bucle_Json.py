import json

data = {}
data['clients'] = []

data['clients'].append({
    'first_name': 'Wilher',
    'last_name': 'Polanco',
    'age': 27})

data['clients'].append({
    'first_name': 'Joe',
    'last_name': 'Hinners',
    'age': 31})

data['clients'].append({
    'first_name': 'Theodoric',
    'last_name': 'Rivers',
    'age': 36})

with open('data.json', 'w') as file:
    json.dump(data, file, indent=4)

with open('data.json') as file:
    data = json.load(file)

    for client in data['clients']:
        print('First name:', client['first_name'])
        print('Last name:', client['last_name'])
        print('Age:', client['age'])
        print('')
