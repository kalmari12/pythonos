import random
'''print(f"a lista elemei: {lista}")'''
lista = []

index = 0

for x in range(200):
    lista.append(random.randint(1,20))

lista.sort()
print(f"kezdeti lista: {lista}")

'''lista.pop()''' #mindenkori utolsó elemet tünteti el
eltavolitando = lista[0]
lista.remove(eltavolitando) # az első találatnál eltávolítja az elemet, ismétlésnél nem csinál semmit

print(f"átalakított: {lista}")

'''
print(lista[:5])
print(lista[150])
print(lista[123:130])
print(lista[10:20],  end= ' - \n')
print(f"Elemek összege: {sum(lista[1:30])}")'''

lista.clear() #törli a lista tartalmat
lista.insert() # a megadott index helyere rakja be az elemet a többit hatra tolja 
lista.count() # egy szam hanyszor fordul elő




