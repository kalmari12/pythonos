#modulok meghívása

import random



# lista letrehozasa

szamlista = []

lista2 = [3,5,12,4]

szlista = ["alma","korte","szilva"]

#lista feltöltése véletlenszámokkal

for x in range(100): #hany darab elemet sorsolok
    szamlista.append(random.randint(0, 1000)) #0 és 1000 között 

szamlista.sort()


# 1 elem vagy interbvallum lekerese
'''
print(f"{szamlista}") #komplett lista kiirasa
print(f"{szamlista[23]}") #23. indexű elem kiirasa, ha nincs akkor overflow
print(f"{szamlista[5:12]}") # 5 és 12 elem kozotti elemek kiirasa
print(f"{szamlista[:5]}") #elso ot elem kiirasa
print(f"{szamlista[5:]}") #elso ot elem utani resz kiirasa
print(f"{szamlista[-1]}") #mindenkori utolso elemet irja ki
print(f"{szamlista[0]}") #mindenkori elso elemet irja ki
#ez barmilyen muveletben felhasznalhato
#itt nem tortenik bejaras


#lista metodusai (szintén bejárás nelküliek)
szamlista.append() # lista vegere szur be egy elemet
szamlista.insert() # lista megadott indexszére szúr be elemet, a lista utána lévő elemeinek az indexe novekszik egyel
szamlista.pop() # alapértelmezés szerint a lista végéről eltünteti a mindenkori utolsó elemet
szamlista.remove()  # a megadott elemet tunteti el (csak az elsö talalatot)
szamlista.clear() # a lista megmarad de a tartalmat uriti
szamlista.sort() # novekvo rendezes
szamlista.reverse() # csokkeno rrendezes (szamlista.sort(reverse=True))<- ez ugyanazt csinalja 
szamlista.copy() # egy új listába masolja a lista tartalmát
#ezek mindegyike a kiindulo listat modositja


#lista bejarasa
# A megoldas: (for) - kézenfekvőbb
#minden elemen elvegzi ugyanazt a muveletet(indexszel nem kell foglalkozni)

for x in szamlista: #pontosan annyiszor fut le, mint amennyi elem van
    print(x, end='\n\t') #kiirja az indexszen lévő elemet 

#B megoldas: (while) - itt az indexszet nekd kell kezelni, ha nem emled az index értékét és a feltétel igaz, akkor végtelen ciklust kapsz
# ez egy elöltesztelő ciklus, azaz rossz feltétel megadása esetén egyszer sem fut le

index = 0
while  index < len(szamlista):
    print(szamlista[index])
    index += 1 # ha ez nincs itt akkor végtelen ciklus
'''
# # # # #
#feladat: szétválogatás
tizzel = []
nemtizzel = []

for x in szamlista:
    if x % 10 == 0:
        tizzel.append(x)
    else:
        nemtizzel.append(x)

print(f"{tizzel}")





















