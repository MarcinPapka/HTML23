# animals = [
#     {'name':'Burek', 'kind':'Dog', 'age': 7},
#     {'name':'Bonifacy', 'kind':'Cat', 'age': None},
#     {'name':'Misio', 'kind':'hamster', 'age': None},
# ]
# print(animals[-1]['name'])
# animals[1]['age'] = 2
# print(animals[1])
# animals.insert({0'name': 'Reksio', 'kind': 'dog', 'age': 9})
# print(animals)

address = [
    {'city': 'Kraków', 'street': 'Reduta', 'house_number': '2', 'post_code': '31-421'},
    {'city': 'Warszawa', 'street': 'Rzemieślnicza', 'house_number': '20E', 'post_code': '30-363'},
    {'city': 'Toruń', 'street': 'Wrocławska', 'house_number': '9', 'post_code': '31-354'},
]

if __name__ == '__main__':

print(address[-1]["post_code"])
print(address[1]["city"])
address[0]["street"] = 'Zielona'
print(address)
