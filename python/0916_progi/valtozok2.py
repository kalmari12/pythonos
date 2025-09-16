valtozo = int(input("Kérek egy adatot: "))
print(f"A változó típusa: {type(valtozo)}")

if type(valtozo) == int:
    print(f"Ez egy egész szám")
    print(f"hatványra emelve: {valtozo**2} ")
elif type(valtozo) == str:
    print(f"A művelet nem végezhető el!")



