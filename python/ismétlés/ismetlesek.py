a = int(5)
b = float(12)
szöveg = str("alma")
igaz_e = True #vagy false (bool)
egyéb1 = None
print(f"{type(b)}")

c = int(input("kérek egy szamot: "))
c2 = float(input("kérek egy szamot: "))
c = input("kérek egy szot: ") # strel is mukodik

# igaz e vagy hamis
if igaz_e: # igaz_e == True
    print("Ez az állítás igaz: ")
else:
    print("Az állítas hamis")

# inverz

if not igaz_e:
    print("Az állítas hamis")
else:
    print("Ez az állítás igaz: ")

#egyértelmu feltétel(tipusvizsgaLAT)
if type(szöveg) == str:
    print(f"ez egy szoveg")
else:
    print(f"Ez nem egy szöveg")

#egyértelmu feltétel (szám)
if a <= 5: # a == 5 - egyenlo a != - nem egyenlo
    print("igaz")
else:
    print("nem igaz")

#több feltétel megadása
if a < 5 and a > 0: # ha mindketto teljesul
    print("ben ne van az intervallumban az érték")
else:
    print("Nincsen benne az intervallumban az érték")

#több feltétel megadása 2 
if a <5 or a > 0: #ha valamelyik teljesul (vagy)  
    print(f"az allitas igaz")

#tobb feltetel megadasa 3
if a < 5 | a > 0:
    print("az allitas igaz")

#tobb feltetel megadasa 4
if a < 5 and a > 0: # ha mindketto teljesul
    print("ben ne van az intervallumban az érték")
else:
    print("Nincsen benne az intervallumban az érték")

#tobb feltetel megadasa 5 
x = 6
if 12 > x > 17:
    print("az allitas hamis")

#tobb feltetel megadasa 6
if 0 < x < 8:
    print("az allitas igaz!")
















































