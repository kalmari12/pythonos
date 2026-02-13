import datetime
import random

'''datum = datetime.date(2026, 2, 23)
szuldatum = datetime.date(2009, 5,5)

kor = datum-szuldatum
print(kor/365)

print(datum.strftime("%A"))
'''
# while 1582.10.04-nél előbbi dátumot ne lehessen megadni
# datum bevitele utan irja ki hogy az milyen nap


# allapitsd meg a megadott szabalyok meneten egy randomizalt datum  milyen napra esett 100 db-o

datumok = []

for x in range(100):
    datum = datetime.date(random.randint(1583, 2026),random.randint(1,12),random.randint(1,28))
    datumok.append(datum)

for x in datumok:
    print(x,x.strftime("%A"))
    
igaze = False
datumok2 = 0
###################################################
while not igaze:
    try:
        datumok2 = datetime.date(int(input("Adja meg az evet: ")),int(input("Adja meg a honapot: ")),int(input("Adja meg a napot: ")))
        if datumok2.year <= 1582 and datumok2.month <= 10 and datumok2.day <= 4:
            print(f"NIGa")
        else:
            igaze = True
    except:
        print("fuck you")
        continue

print(f"A megadott datum: {datumok2.strftime('%c'), datumok2.strftime('%A')}")
        

'''            if datumok2.year >= 1582 and datumok2.month >= 10 and datumok2.day >= 4:
         print(f"A megadott dátumra esett nap: {datumok2,datumok2.strftime('%A')}")
     else:
         while datumok2.year < 1582 and datumok2.month < 10 and datumok2.day < 4:
             datumok2 = datetime.date(int(input("Adja meg az evet(Az előző nem volt jó): ")),int(input("Adja meg a honapot(Az előző nem volt jó): ")),int(input("Adja meg a napot(Az előző nem volt jó): ")))
         print(f"A megadott dátumra esett nap: {datumok2,datumok2.strftime('%A')}")'''