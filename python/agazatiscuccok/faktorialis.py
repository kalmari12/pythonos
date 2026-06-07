#Írj rekurzív függvényt, amely kiszámolja egy nemnegatív egész szám faktoriálisát! Kezelje le azt az esetet is, ha a felhasználó negatív számot ad meg (kivételkezeléssel)!

# def faktor(szam):
#     faktor = szam-1 
#     ossz =0
#     if faktor != 0:
#         szam*faktor += ossz  
#     return faktor(szam)

# def faktor(sz, mivel):
#     eredmeny = sz*(sz-1)
#     for i in range(sz-2,1,-1):
#         eredmeny += eredmeny*(i-1)
#     return eredmeny


def faktor(sz, mivel):
    if mivel>1:
        eredmeny = sz*mivel
        return faktor(eredmeny, mivel-1)
    else:
        eredmeny = sz        
        return eredmeny

print(faktor(5,4))


