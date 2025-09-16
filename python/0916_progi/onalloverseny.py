import random 

race1 = random.randint(1, 300)
race2 = random.randint(1, 300)

print(f"Az első autó száma: {race1}\n"
      f"A második autó száma: {race2}")

if race1 > race2:
    print(f"Az első autó nyert!")
elif race1 < race2: 
    print(f"A második autó nyert")

else: 
    print(f"A verseny döntetlen lett")