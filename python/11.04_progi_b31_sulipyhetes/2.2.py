import random
"""szo = str("alma")
szo2 = str(input("kerek egy betut: "))
index = 0
talalat = False

while index < len(szo) and not talalat:
    if szo[index] == szo2:
            talalat == True
    index = index + 1

if talalat == True:
    print("A betu nincs van a szoban")
else:
    print("a betu benne van a szoban")
"""
szolista = ["levego", "alma", "papir", "negyzet", "kenyer"]
szo2 = szolista[random.randint(0,4)]
state = True
index = 0

while state:
    betu = str(input("kerek egy betut"))   
    for y in betu:
        if betu == y:
            print("a betu szerepel a listaban")
    if len(betu) == 0:
        state == False

print(f"A megadott szo a {szo2} ")





