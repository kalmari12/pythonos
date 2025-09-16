#szukseges modulok meghivasa

import random

#szereplok eletereje konstansként eltárolva változóban 
hos_hp = 100

ellenseg_hp = 75

# ki mekkorát ut az adott korben, es ehhez sorsolunk random szamot
hos_hit = random.randint(0, 200)
ellenseg_hit = random.randint(0, 120)

utes = random.randint(1, 6)

if utes == 1 or utes == 3 or utes == 5  or utes == 6:
    print(f"hős üt!\n"
          f"Sebzés: {hos_hit}\n"
          f"ellenség eletereje: {ellenseg_hp - hos_hit}")
    
else :
    print(f"Ellenség ut!\n"
          f"sebzes: {ellenseg_hit}\n"
          f"Hős életereje: {hos_hp - ellenseg_hit}\n")

if (hos_hp -ellenseg_hit) > 0 and (ellenseg_hp - hos_hit) <= 0:
    print(f"\nA hős még él!"
          f"\nAz ellenség halott")

elif (hos_hp -ellenseg_hit) < 0 and (ellenseg_hp - hos_hit) >= 0:
    print(f"\nA hős halott!"
          f"\nAz ellenség még él")