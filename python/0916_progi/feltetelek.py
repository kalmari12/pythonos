import random

veletlen = random.randint(-300, 300)
print(f"A sorsolt szam: {veletlen}")

if veletlen % 3 == 0:
    print(f"A szam osztahto 3-mal!\n"
          f"Eredmény: {veletlen / 3}")