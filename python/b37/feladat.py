
'''
-véletlenszamokat sorsolj es tarolj egy oszetett adatszerkezetben
-menj vegig a listan és nezd meg melyik szamok oszthatók: 3, 5, 7
-alkalmazd a szétvalogatas tetelt (tárold el kulon listakban)
-ird ki átlátható formában 
-az alaplista elemeit addig sorsold amig nem kapsz 6667-et
'''
import random

lista1 = []

lista2 = []



while lista1.count(6667) == 0:
    szam1 = random.randint(1,6667)
    lista1.append(szam1)
    if szam1 % 3 == 0 and szam1 % 5 == 0 and szam1 % 7 == 0:
        lista2.append(szam1)

print(f"\n\nAz alaplista számai: {lista1}")
print(f"\n\nA 3-mal 5-el és héttel osztható számok: {lista2}")













