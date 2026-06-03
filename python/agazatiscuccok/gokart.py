class Gokartpalya:
    def __init__(self, nev, telepules, palya_hossz, jegyar):
        self.nev = nev
        self.telepules = telepules
        self.palya_hossz = int(palya_hossz)
        self.jegyar = int(jegyar)

    def __str__(self):
        return f"Nev: {self.nev}\nTelepules: {self.telepules}\nPalya_hossz: {self.palya_hossz}\nJegyar: {self.jegyar}"
    
    def aremeles(nev, lista):
        aremelt = []

        for x in lista:
            if x.nev == nev:
                x.jegyar +=  x.jegyar*0.15
                return x