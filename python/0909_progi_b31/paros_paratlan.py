szam = int(input("kérek egy számot: "))

if szam % 2 == 0:
 print(f"Az eredmény: {szam / 2}")
 print("A szám páros!")

else:
 print(f"Az eredmény: {szam / 2:.2f}")
 print(f"A maradék: {szam % 2}")
 print("A szám páratlan!")



