import datetime

class termek:
    def __init__(self, nev, kategoria):
        self.nev = nev
        self.kategoria = kategoria
        self.bruttoar = 0
        self.suly = 0
        self.nettoar = 0

    def __str__(self):
        return f"{self.nev}, kategória: {self.kategoria}, jelenlegi darabára: {self.bruttoar}, súlya: {self.suly}, nettóára: {self.nettoar}"

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