szoveg = str("Lorem, ipsum dolor sit amet consectetur adipisicing elit. Quod in, dolore vero, error excepturi doloribus, eveniet aut dolores enim cupiditate laboriosam vel mollitia voluptatibus dignissimos? Ullam voluptates voluptatum distinctio asperiores.")

print(f"első betű: {szoveg[0]}")
print(f"uccso betű: {szoveg[-1]}")
print(f"szoveg hossza: {len(szoveg)}") # szokozok is beletartoznak


#szavak száma
szavak = 0

for szó in szoveg:
    if szó == " ":
        szavak += 1

print(f"szavak szama: {szavak}")

#bekert betubol hany darab van 
bekert_betu = str(input("melyik betűt keressem? > "))

betu_szama = 0

for betu in szoveg:
    if bekert_betu == betu in szoveg:
        print("talalat")
        betu_szama += 1
    else:
        print("nincs talalat")

print(f"A keresett betű ennyiszer szerepel a szövegben. {betu_szama}")

index = 0 
while index < betu_szama:
    szoveg.remove(bekert_betu)



















