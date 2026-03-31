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
        return f"Név: {self.nev}\nSzülhely: {self.szulhely}\nSzüldatum: {self.szuldatum}\nemail: {self.email}\nTelefonszam: {self.telefonszam}\nIranyitoszam: {self.iranyitoszam}\nVaros: {self.varos}\nUtca: {self.utca}\nHazsszam: {self.hazszam}\nnem: {self.nem}\ballampolgarsag: {self.allampolgarsag}\nszemelyi: {self.szemelyi_azonosito}\nAnyja neve: {self.anyja_neve}"