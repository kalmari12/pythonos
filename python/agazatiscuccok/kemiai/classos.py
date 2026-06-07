class auto:
    def __init__(self,Auto_ID,Marka,Modell,Gyartasi_Ev,Uzemanyag,Ar_HUF,Futott_KM):
        self.autoid = Auto_ID
        self.marka = Marka
        self.modell = Modell
        self.gyartasiev = int(Gyartasi_Ev)
        self.uzemanyag = Uzemanyag
        self.ar = int(Ar_HUF)
        self.futott = int(Futott_KM)

    def __str__(self):
        return f"Auto Id: {self.autoid}\nMarka: {self.marka}\nModell: {self.modell}\nEv: {self.gyartasiev}\nUzemanyag: {self.uzemanyag}\nAr: {self.ar}\nFutott: {self.futott}"
    
    def atlag(lista: list) -> int:
        ossz = 0
        index = 0
        for x in lista:
            index +=1
            ossz += x.ar
        return ossz / index
    
    def legkevesebb(lista: list) -> int:
        legkev = lista[0].futott
        for x in lista:
            if x.futott < legkev:
                legkev = x.futott
        return legkev
    
    def uzemanyag2(lista: list, gas: str):
        megkeresett = []
        for x in lista:
            if x.uzemanyag == gas:
                megkeresett.append(x)
        return megkeresett
