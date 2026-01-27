szöveglista = []

# forrás beolvasása

with open('egricsillagok.txt', 'r', encoding="utf-8") as szöveg:
    bevitel = szöveg.read()

darabokban = bevitel.strip().split()

'''for szó in darabokban:
    print(szó)'''

vizsgal = str(input("kérem a keresett szót: "))
index = 0

for szó in darabokban:
    szó = szó.replace(",", "").replace('.', '').replace(':', '').replace('-', '')
    if szó == vizsgal:
        index += 1
    print(szó)

print(f"A szó ennyiszer  szerepel a listában {index}!")
    
