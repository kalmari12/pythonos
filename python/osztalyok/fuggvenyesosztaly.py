import datetime

class szemely: #osztálydefiníció
    def __init__(self, vezeteknev, keresztnev, szuleteshely, szuletesdatum):
        self.x = datetime.datetime.now()
        self.vezeteknev = vezeteknev
        self.keresztnev = keresztnev
        self.szuleteshely = szuleteshely
        self.szuletesdatum = szuletesdatum
        self.kor = self.x.year - self.szuletesdatum.year
        self.varos = "Budapest"

    def info(self):
        x = datetime.datetime.now()
        return f"Vezetéknév: {self.vezeteknev}", f"Keresztnév: {self.keresztnev}",f"Születéshely: {self.szuleteshely}",f"Szuletesdatum: {self.szuletesdatum}", f"hanyeves: {self.kor}"






szemely1 = szemely("Szabó", "János", "Debrecen", datetime.date(1999, 11, 5))

print(szemely1.info())