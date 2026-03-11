from modul import termek
from modul import rendeles
import datetime

termek2 = termek("Uborka", "Zöldség")
termek3 = termek("hagyma","Zöldség")
termek4 = termek("répa","Zöldség")
termek5 = termek("barack","gyümölcs")
termek1 = termek("Paradicsom", "Zöldség")
termek1.bruttoar = 1000
termek1.suly = 300
termek1.netto()

termekek = [termek1, termek2, termek3, termek4, termek5]

for term in termekek:
    print(term.kiir())

rendelesek1 = rendeles("Áron")

