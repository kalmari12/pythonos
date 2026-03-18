import datetime
'''class termek:
    def __init__(self, nev, cikkszam, kategoria, egysegar):
        self.nev = nev
        self.cikkszam = cikkszam
        self.kategoria = kategoria
        self.egysegar = egysegar
        self.raktaron = 200
        self.telephely = 1

    def __str__(self):
        return f"Termék neve: {self.nev}\nCikkszáma: {self.cikkszam}\nKategória: {self.kategoria}\nEgységára: {self.egysegar}\nRaktáron: {self.raktaron}\nTelephelye: {self.telephely}"

    '''
global idcount; idcount = 0


class termek:
    def __init__(self, id, nev, kategoria, ar, mennyiseg, leiras):
        self.id = id
        self.nev = nev
        self.kategoria = kategoria
        self.ar = ar
        self.mennyiseg = mennyiseg
        self.leiras = leiras

    def __str__(self):
        return f"id: {self.id}\nTermék neve: {self.nev}\nKategória: {self.kategoria}\nEgységára: {self.ar}\nMennyiség: {self.mennyiseg}\nLeirása: {self.leiras}"

class rendeles:
    def __init__(self, nev, mibol, gramms):
        self.id = idcount + 1
        self.id = nev
        self.mibol = mibol
        self.gramms = gramms
        
    def __str__(self):
        return f"A rendelés ideje: {datetime.datetime.now}\nA rendelő neve: {self.nev}\nId: {self.id}"

