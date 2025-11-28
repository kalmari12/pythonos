# MEgnyitási módok:
# r: olvasas
# w: ítrás, fájlt hoz létre; ha létezik ilyen nevű fájl már, felülírja az eredetit 
# x: írás, fájlt hoz létre; ha létezik ilyen nevű fájl már, hibát ads
# a: a létező fájl végére hozzáfűz, ha még nem létezik ilyen nevű, akkor létrehozza
# a+: hozzáfűzést és olvasást is lehetővé teszi

with open('kimenet.txt', 'w', encoding="utf=8") as datafolyam:
    print("Lorem ipsum", file=datafolyam) # tényleges fájlba iras

    print("\nLorem ipsum dolor sit amet, consectetur adipiscing elit. Aenean at imperdiet felis. Nulla efficitur lacus odio, in accumsan ipsum volutpat vitae. Ut eget interdum quam. Mauris suscipit maximus bibendum. Aliquam erat volutpat. Morbi sit amet massa ac diam ullamcorper scelerisque vel sed nulla. Cras nisi magna, viverra non erat quis, dignissim viverra sapien. Nam luctus semper lorem at porta. Nam quis mollis arcu, eget luctus quam.", file=datafolyam)

    print("\nVestibulum a turpis erat. Morbi pellentesque massa a felis tempor tempus. Duis sollicitudin pharetra ligula, a iaculis tortor ornare a. Maecenas sed leo viverra, ultrices sapien non, tristique metus. Integer vestibulum odio eros, ut vulputate tortor mollis ultricies. Nulla facilisi. Fusce tempus condimentum lacinia. Mauris at lorem eget tellus sodales consequat.", file=datafolyam)
    
    print("A fájlba iras megtortent")

import random

for _ in range(100):
    with open('kimenet2.txt', 'a', encoding="utf-8") as datafolyam:
        szam = random.randint(1, 100)
        print(f"{szam}")
        print(f"{szam}", file=datafolyam)





