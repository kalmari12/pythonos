import random
import csv
import datetime

def tisztit(szoveg:str)-> str:
    jelek = [",",".","-","_","(",")","[","]"]

    for jel in jelek:
        szoveg = szoveg.replace(jel, " ")
    return(szoveg)

def elemeklen(lista:list) -> int:
    db = 0
    for elem in lista:
        if elem != " ":
            db += 1
    return db

def torolt(lista:list) -> list:
    for elem in lista:
        if elem.isdigit():
            lista.remove(elem)
    return lista

def evzsamok(listaegy:list) -> list:
    ret = []
    for elem in listaegy:
        if len(elem) == 4 and elem.isdigit():
            ret.append(elem)
    return ret

def mghk(szavas):
    ret2 = []
    maganok = ["a",'á',"e","é","o","ó","ö","ő","u","ú","ü","ű","í"]
    for szo in szavas:
        if szo[0] in maganok and szo not in ret2:
            ret2.append(szo)
    return ret2

with open("stringekketto/forras.txt", "r", encoding="utf-8") as adatok:
    tartalom = adatok.read()

tartalom = tartalom.lower()
tartalom = tisztit(tartalom)
szavak = tartalom.split()
esz = evzsamok(szavak)
szavak = torolt(szavak)
mghkk = mghk(szavak)

print(esz)
print(mghkk)