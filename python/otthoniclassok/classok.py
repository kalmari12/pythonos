class szemely:
    def __init__(self, nev, szulhely, szuldatum, email, telefonszam, iranyitoszam, varos, utca, hazszam, nem, allampolgarsag, szemelyi_azonosito, anyja_neve):
        self.nev = nev
        self.szulhely = szulhely
        self.szuldatum = szuldatum
        self.email = email
        self.telefonszam = telefonszam
        self.iranyitoszam = iranyitoszam
        self.varos = varos
        self.utca = utca
        self.hazszam = hazszam
        self.nem = nem
        self.allampolgarsag = allampolgarsag
        self.szemelyi_azonosito = szemelyi_azonosito
        self.anyja_neve = anyja_neve

    def __str__(self):
        return f"Neve: {self.nev}\nSzulhely: {self.szulhely}\nSzuldatum: {self.szuldatum}\n Email: {self.email}\nTelefonszam: {self.telefonszam}\nIranyitoszam: {self.iranyitoszam}\nVaros: {self.varos}\nHazszam: {self.hazszam}\nNem: {self.nem}\nAllampolgarsag: {self.allampolgarsag}\nSzemelyi: {self.szemelyi_azonosito}\nAnyja: {self.anyja_neve}"