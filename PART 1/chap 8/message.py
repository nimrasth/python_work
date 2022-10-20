# message
def display_message():
    print("We are learning about functions.")
display_message()


# favouite book
def fav_book(title):
    print(f"\nOne of my favourite book is {title.title()}")
fav_book('The Alchemist')


# t-shirt
def make_shirt(size, text):
    print(f"\nThe T-shirt of size {size} has a message '{text}'.")
make_shirt('large', 'Life is good')
make_shirt(size='small', text='YOLO')


#large shirts
def make_shirt( text, size='large',):
    print(f"\nThe T-shirt of size {size} has a message '{text}'.")
make_shirt(text='I love python')
def make_shirt( size, text="YOLO"):
    print(f"\nThe T-shirt of size {size} has a message '{text}'.")
make_shirt('large')
make_shirt('medium')


# cities
def describe_city(city, country='Nepal'):
    print(f"\n{city} is in {country}.")
describe_city('Patan')
describe_city('Kathmandu')
describe_city('Santorini')
