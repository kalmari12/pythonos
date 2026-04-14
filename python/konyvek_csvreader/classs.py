class konyv:
    def __init__(self, cim, szerzo, ISBN, megjelenes_eve, oldalszam):
        self.cim = cim
        self.szerzo = szerzo
        self.ISBN = ISBN
        self.megjelenes_eve = megjelenes_eve
        self.oldalszam = oldalszam

    def __str__(self):
        return f"A könyv címe: {self.cim}\nSzerző: {self.szerzo}\nISBN: {self.ISBN}\nMegjelenés éve: {self.megjelenes_eve}\nOldalszam: {self.oldalszam}"
    
    def atlagkonyv(lista):
        index = 0
        ossz= 0 
        for konyv in lista:
            index += 1
            ossz += int(konyv.oldalszam)
        return ossz / index
