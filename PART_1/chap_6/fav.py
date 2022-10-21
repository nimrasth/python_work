# favourite_places
favourite_places={
    'Alex': ['Mustang','Lomanthang', 'Manang'],
    'ram': ['basantapur', 'patan', 'bhakatapur'],
    'Harry': ['rara', 'paanch pokhari', 'shey phoksundo']
}
for person, place in favourite_places.items():
    print(f"\n{person} likes to visit :")
    for place in place:        
        print(place.title())

# favorite Numbers
fav_num={
    'ram': [7,14],
    'shyam': [11,22],
    'hari': [2,4,6,8],
    'gopal': [1,3,5,7],
    'krishna': [10_00_000],
}
for people, num in fav_num.items():
    print(f"\nFavourite numbers of {people}:")
    for num in num:
        print(num)
