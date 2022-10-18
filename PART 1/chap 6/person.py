
# person
person={
    'first_name':'Ram',
    'last_name' : 'Shrestha',
    'age': 50,
    'city':'Kathmandu'
}
print(person)


# favourite number
fav_num={
    'ram': 7,
    'shyam': 11,
    'hari': 3,
    'gopal': 1,
    'krishna': 10_00_000
}
print(fav_num)


# glossary
glossary={
    'Exodus': 'A circumstance when a huge number of people leave a particular place.',
    'Indigenous': 'occurring, living, or existing naturally in a particular place.',
    'leap': 'a sudden increase and spring or jump in air quickly.',
    'snatch': 'forcefully seize something in a rude manner.',
    'norm': 'a pattern or standard.'
}
for word,meaning in glossary.items():
    print(f"\n{word.title()} : {meaning}")


# river
river_name={
    'Nile River': 'North East Africa',
    'Amazon River': 'South America',
    'Yangtze River': 'China',
    'Mississippi – Missouri River': 'USA',
    'Yellow River': 'China'
}
for river, country in river_name.items():
    print(f"\n The {river.title()} runs through {country}")
print("\n")
for river in river_name.keys():
    print (river)
print("\n")
for country in river_name.values():
    print(country)


# favourite languages
favorite_languages = {
 'jen': 'python',
 'sarah': 'c',
 'edward': 'ruby',
 'phil': 'python',
 }
people=['ram', 'shyam', 'sarah', 'phil']
for person in people:
    if  person in favorite_languages.keys(): 
        print(f"\n{person.title()}, Thank u for responding.")
    elif person  not in favorite_languages.keys():
        print(f"\n{person.title()}, You are invited to take the poll.")

