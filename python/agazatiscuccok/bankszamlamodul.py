import random

class bankszamla:
    def __init__(self, tulajdonos_neve):
        self.tulajdonos_neve = tulajdonos_neve
        self.egyenleg = 0
        self.szamlaszam = random.randint(100000,999999)

    def __str__(self):
        return f"Bankszámla | {self.tulajdonos_neve} | Egyenleg: {self.egyenleg} Ft"

    def befizet(self, mennyi: int):
        self.egyenleg += mennyi
    
    def kivesz(self, mennyi: int):
        self.egyenleg -= mennyi

        