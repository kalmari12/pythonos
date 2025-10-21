import random

lista1 = [0,0]
meddig =random.randint(6,10)
for i in range(meddig):
    player1_dsz = random.randint(1,6)
    player2_dsz = random.randint(1,6)
    print(f"Az első játékos által dobott szám: {player1_dsz}")
    print(f"A második játékos által dobott szám: {player2_dsz}")

    if player1_dsz > player2_dsz:
        lista1[0] += 1
        print(f"Az első játékos nyert!")
    elif player1_dsz < player2_dsz:
        lista1[1] += 1
        print(f"A második játékos nyert!")

    elif player1_dsz == player2_dsz:
        print(f"Döntetlen!")

if lista1[0] > lista1[1]:
    print(f"Az első játékos nyert, a pontszáma: {lista1[0]}")
if lista1[0] < lista1[1]:
    print(f"A második játékos nyert, a pontszáma: {lista1[1]}")