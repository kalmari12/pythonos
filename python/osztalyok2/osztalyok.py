class tanulo:
    def __init__(self, keresztnév, eletkor, szuletesh):
        self.keresztnév = keresztnév
        self.eletkor = int(eletkor)
        self.szuletesh = szuletesh

    def bemutatkozas(self):
        return f"A nevem: {self.keresztnév}, {self.eletkor} éves vagyok, születési helyem: {self.szuletesh}."

    def oregedes(self, ev):
        eletkor = self.eletkor = self.eletkor + ev
        return  eletkor

tanulo1 = tanulo("Péter", 15, "Kecskemét")
tanulo2 = tanulo("Dániel", 16, "Kiskunfélegyháza")
print(tanulo1.bemutatkozas())
print(tanulo2.bemutatkozas())
print(40*"-")
tanulo1.oregedes(10)
tanulo2.oregedes(271)
print(tanulo1.bemutatkozas())
print(tanulo2.bemutatkozas())




















        