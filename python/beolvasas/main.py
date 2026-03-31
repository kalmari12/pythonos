from class1 import szemely


szemelyek = []

with open("python/beolvasas/szemelyek_bov.csv","r",encoding="utf-8")as adat:
    next(adat)
    for sor in adat.read().strip().split(","):
        nev = 

