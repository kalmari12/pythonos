import datetime
import random

idcount = 0

class termek:
    def __init__(self, nev, kategoria):
        global idcount; idcount += 1
        self.id = idcount
        self.nev = nev
        self.kategoria = kategoria
        self.bruttoar = random.randint(200,800)
        self.suly = random.randint(100,500)
        self.nettoar = 0

    def __str__(self):
        return f"Id:{self.id},{self.nev}, kategória: {self.kategoria}, jelenlegi darabára: {self.bruttoar}, súlya: {self.suly}, nettóára: {self.nettoar}"

    def netto(self):
        netto =self.bruttoar*0.73
        self.nettoar = netto
        return self.nettoar

    
    
class rendeles:
    def __init__(self, nev):
        self.nev = nev
        self.ido = datetime.datetime.today()

    def __str__(self):
        return f"Rendelő neve: {self.nev}\nRendelés ideje: {self.ido}"