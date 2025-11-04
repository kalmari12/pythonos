import random
'''
lista1 = []
lista2 = []

for x in range(5):
    lista1.append(random.randint(1,10))

for x in lista1:
    if x % 2 == 0:
        lista2.append(x)

print(f"a lista elemei: {lista1}\n\n"
      f"A lista eleminek összege: {sum(lista2)}")
'''

'''lista1 = []

szam1 = int(input("kérek egy egész számot -5;5-ös intervallumon: "))

while szam1 < 5 and szam1 > -5:
    if szam1 > 5 or szam1 < -5:
        print("A szám kisebb vagy nagyobb mint a megadható számok")

    '''
lista1 = []

muvelet = True

while muvelet:
    szam = input("adj egy szamot: ")

    if szam <= 5 and szam >= -5:
        lista1.append(szam)
    else:
        print("rossz a szam")
        muvelet = False

print(f"a megadott szamok: {lista1}")