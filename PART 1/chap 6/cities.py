cities={
    'Shanghai':{
        'country': 'China',
        'population': 14_250_000 ,
        'fact':'It covers an area of 6,340 square kilometers.',
    },
    'Karachi':{
        'country': 'Pakistan',
        'population': 14_500_000 ,
        'fact':'It covers an area of 3,780 square kilometers.',
    },
    'Tokyo':{
        'country': 'Japan',
        'population': 13_189_000,
        'fact':'It covers an area of 2,194 square kilometers.',
    },
}
for city,info in cities.items():
    print("\n")
    print(city)
    for fact,detail in info.items():
        print(f"{fact} : {detail}")
        