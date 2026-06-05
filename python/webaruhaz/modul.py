class termek:
    def __init__(self, sor):
        adat = sor.strip().split(',')
        self.Termek_ID = adat[0]
        self.Termeknev = adat[1]
        self.kategoria = adat[2]
        self.AR_HUF = adat[3]
        self.Keszlet_db = adat[4]
        self.Ertekeles = adat[5]

    def __str__(self):
        return f"Termek ID: {self.Termek_ID}\nTermeknev: {self.Termeknev}\nkategoria: {self.kategoria}\nAr: {self.AR_HUF}\nKeszlet: {self.Keszlet_db}\nertekeles: {self.Ertekeles}"