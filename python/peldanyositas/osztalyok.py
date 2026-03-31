class szemely:
    def __init__(self, nev, kereszt):
        self.nev = nev
        self.kereszt = kereszt

    def __str__(self):
        return f"Teljes Neve: {self.nev} {self.kereszt}" 