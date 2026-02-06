import random

emberek = ["Levi","Kasa","En","Ray","Peti","Monke","Borka","Lovag","Felix"]

hianyoznak = []
kihianyzik = []

#kik hianyoznak bekerese
while kihianyzik != "nem":
    kihianyzik = str(input("Ki nincs most: "))
    if kihianyzik != "nem":
        hianyoznak.append(kihianyzik)

igazi = []

#hianyzok kivevese
for ember in emberek:
    if ember not in hianyoznak:
        if ember == "Felix":
            if random.random() < 0.1:
                igazi.append(ember)
        else:
            igazi.append(ember)

random.shuffle(igazi)

hanyember = int(input("Hany ember legyen egy csapatban? "))

# elso csapat
egycsapat = igazi[:hanyember]

# masodik csapat
kettocsapat = igazi[hanyember : hanyember*2] 

print(f"------- 1. Csapat -------\n"
      f"{egycsapat}")


print(egycsapat)
print(kettocsapat)
