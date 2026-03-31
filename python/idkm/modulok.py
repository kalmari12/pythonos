class termek:
    def __init__(self, nev, kategoria, ar):
        self.nev = nev
        self.kategoria = kategoria
        self.ar = ar

    def __str__(self):
        return f"A termék neve: {self.nev}\nA termek kategoriaja: {self.kategoria}\nA termek netto ara: {self.ar}"