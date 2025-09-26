szam = int(input("Adj meg egy szémot 5 és 10 között:"))

while not 5 <= szam <= 10:
    szam = int(input("Helytelen érték: kérek egy másikat:"))

print("rendben")