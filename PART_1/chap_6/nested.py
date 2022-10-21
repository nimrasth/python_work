# person
people={
    'person_1':{
    'first_name':'Ram',
    'last_name' : 'Shrestha',
    'age': 50,
    'city':'Kathmandu'
    },
    'person_2':{
        'first_name':'Shyam',
        'last_name' : 'Pradhan',
        'age': 40,
        'city':'Lalitpur'
    },
    'person_3':{
        'first_name':'Hari',
        'last_name' : 'Kayastha',
        'age': 30,
        'city':'Bhaktapur'
    }
}
for person,information in people.items():
    print(f"\n{person}: {information['first_name']} {information['last_name']} of {information['age']} lives in {information['city']}.")


# pets
pets={
    'dog':{
        'German Shephard': 'Alex',
        'Bulldog': 'Barbara',
        'Husky': 'Crimson',
    },
    'cat':{
        'british shorthair': 'Diana',
        'maine coon': 'Elisa',
    },
    'fish':{
        'Goldfish': 'Finn',
        'Catfish': 'Hardy',
    },
}
for animal, info in pets.items():
    for breed, owner in info.items():
        print(f"\n{owner} owns {breed.title()} {animal.title()}.")