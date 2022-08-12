from marvel import Marvel
from keys import public_key, private_key

marvel = Marvel(PUBLIC_KEY=public_key,
                PRIVATE_KEY=private_key)

characters = marvel.characters

my_char = characters.all(nameStartsWith="Captain")["data"]["results"]

for char in my_char:
    print(char["id"], char["name"])
    for comic in char["comics"]["items"]:
        print(comic["name"])
    print("---------------------")