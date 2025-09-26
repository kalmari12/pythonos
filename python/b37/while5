import random

szamlista = []

ujertek =  True

while ujertek:
    sorsolt_szam = random.randint(1,9999)
    szamlista.append(sorsolt_szam)
    print(f"Sorsolt szam: {sorsolt_szam}\n"
          f"A lista hossza {len(szamlista)}")
    kerdes = str(input("Sorsoljak még?(i/n)"))
    if kerdes == "n":
        ujertek = False

print(f"lista elemei {szamlista}")

print(f"A legkisebb elem: {min(szamlista)}\n"
      f"A legnagyobb elem: {max(szamlista)}"
      f"\nAz elemek összege: {sum(szamlista)}"
      f"\nA legelső elem {szamlista[0]}"
      f"\nAz utolso elem: {szamlista[len(szamlista)-1]}")

