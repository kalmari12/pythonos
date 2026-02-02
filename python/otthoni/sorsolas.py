import random

emberek = ["Levi","Kasa","En","Ray","Peti","Monke","Borka","Lovag","Felix"]

hianyoznak = []
kihianyzik = []

#kik hianyoznak bekerese
while kihianyzik != "nem":
    kihianyzik = str(input("Ki nincs most: "))
    hianyoznak.append(kihianyzik)

igazi = []

#hianyzok kivevese
for ember in emberek:
    if ember not in hianyoznak:
        igazi.append(ember)

hanyember = int(input("Hany ember legyen egy csapatban? "))

while if x in egycsapat != x:
    # elso csapat
    egycsapat = []

    for x in range(hanyember):
            egycsapat.append(igazi[random.randint(1,len(igazi))])

    # masodik csapat
    mcsapat = []

    for x in range(hanyember):
        mcsapat.append(igazi[random.randint(1,len(igazi))])

