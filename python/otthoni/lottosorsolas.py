import random




def sorsol(hany, mine, maxe):
    szamlista = []
    for i in range(52):
        hetiszamok = []
        if(len(szamlista)==0):
            for index_szam in range(hany):
                talalt = True
                while(talalt):
                    nyeroszam = random.randint(mine,maxe)                    
                    index2 = 0
                    while(len(hetiszamok)>0 and index2<len(hetiszamok) and hetiszamok[index2]!=nyeroszam):
                         index2+=1
                    if(index2==len(hetiszamok)):
                       talalt = False     
                       hetiszamok.append(nyeroszam)
            szamlista.append(hetiszamok)
        else:
            for index_szam in range(hany):
                talalt = True
                while(talalt):
                    nyeroszam = random.randint(mine,maxe)
                    index = 0
                    elem = 0
                    while index < len(szamlista) and szamlista[index][elem] != nyeroszam:
                            if(elem==hany-1):
                                 elem = 0
                                 index += 1
                            else:
                                 elem += 1
                    if(index==len(szamlista)):
                         index2 = 0
                         while(len(hetiszamok)>0 and index2<len(hetiszamok) and hetiszamok[index2]!=nyeroszam):
                              index2+=1
                         if(index2==len(hetiszamok)):
                            talalt = False     
                            hetiszamok.append(nyeroszam)
            szamlista.append(hetiszamok)
                     
                     
    return szamlista

hatoslista = sorsol(6,1,500)
otoslista = sorsol(5,1,700)
print(otoslista)   
                                   
            
                    
                





