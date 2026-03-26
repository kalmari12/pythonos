class termek:
    def __init__(self, id, nev, kategoria,ar,mennyiseg,leiras):
        self.id = id
        self.nev= nev
        self.kategoria = kategoria
        self.ar = ar
        self.mennyiseg = mennyiseg
        self.leiras = leiras

    def __str__(self):
        return f"Id: {self.id}\nNev: {self.nev}\nKategoria: {self.kategoria}\nAr: {self.ar}\nMennyiseg: {self.mennyiseg}\nLeiras: {self.leiras}"