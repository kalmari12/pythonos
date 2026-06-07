import random

for x in range(100):
    if x % 3 == 0 and x % 5 ==0:
        print("FizzBuzz")
    elif x % 3 == 0 and x % 7 == 0:
        print("FizzBuzz")
    elif x % 3 == 0 and x % 5 == 0 and x % 7 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 ==0:
        print("Buzz")
    elif x % 7 == 0:
        print("Bazz")
    else:
        print(x)



tanulo = []
print("--- Jegynapló ---\n"
      "1. Jegy hozzáadása\n"
      "2. Átlag megjelenítése\n"
      "3. Statisztika\n"
      "4. Kilépés\n")
mitcsinal = int(input("Adja meg mit szeretne csinalni: "))

while i mitcsinal != 4:
    print("--- Jegynapló ---\n"
      "1. Jegy hozzáadása\n"
      "2. Átlag megjelenítése\n"
      "3. Statisztika\n"
      "4. Kilépés\n")
    if mitcsinal == 1:
        jegybekeres = int(input("Adja meg a jegyet: "))
        if jegybekeres <= 5 or jegybekeres >= 1:
            tanulo.append(jegybekeres)
        else:
            print("A jegy nem elfogadható!")
    elif mitcsinal == 2:
        print(f"A tanuló átlaga: {sum(tanulo)/len(tanulo)}")
    elif mitcsinal == 3:
        print(f"A tanuló legjobb jegye: {max(tanulo)}\n"
              f"A tanuló leggyengébb jegye: {min(tanulo)}")
            






