import random

player1_dsz = random.randint(1,6)
player2_dsz = random.randint(1,6)

print(f"Az első játékos által dobott szám: {player1_dsz}")
print(f"A második játékos által dobott szám: {player2_dsz}")

if player1_dsz > player2_dsz:
  print(f"Az első játékos nyert!")
elif player1_dsz < player2_dsz:
  print(f"A második játékos nyert!")

elif player1_dsz == player2_dsz:
    print(f"Döntetlen!")



