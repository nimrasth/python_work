# city country
def city_country(city,country):
    return f"{city}, {country}"

def main():
    print(city_country("Patan", "Nepal"))
main()

# if __name__ == '__main__':
#     main()


# make album
def make_album(name, title, no_songs=None):
    
    artist= {
        'name': name,
        'title': title,
        'no_songs': no_songs,
    }
    return artist

while True:
        print("\nEnter q to quit")
        a_name=input("Enter artist name: ")
        if a_name=='q':
            break
        a_title= input("Enter artist title: ")
        if a_title=='q':
            break
        a_songs= input("enter no of songs: ")
        if a_songs=='q':
            break


aartist=make_album(a_name,a_title,a_songs)
print(aartist)


