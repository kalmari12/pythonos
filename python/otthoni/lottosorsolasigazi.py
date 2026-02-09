import random
lista52 = []
for i in range(52):
    lista7 = []
    for index in range(5):
        talalt = True
        while(talalt):
            i2 = 0
            r = random.randint(1,90)
            while(len(lista7)>0 and i2<len(lista7)  and lista7[i2]!=r):
                i2+=1
            if(i2==len(lista7)):
                lista7.append(r)
                talalt = False
    lista52.append(lista7)

print(lista52)