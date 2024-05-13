class ShipData:
    def __init__(self, nev, ev, tn, egytank):
        self.nev = nev
        self.ev = int(ev)
        self.tulaj_nev = tn
        self.egytank = int(egytank)

    def __str__(self):
        print(self.nev, self.ev)

with open("ship.txt", "rt", encoding="utf-8") as f:
    adatok = f.readlines()
adatok.pop(0)
adatok.pop(0)
ship= []

for i in adatok:
    s = i.split(";")
    ship_egyen = ShipData(s[0], s[1], s[2], s[3])
    ship.append(ship_egyen)


def legoregebb(lista):
    oldest = lista[0].ev
    for i in lista:
        if i.ev < oldest:
            oldest = i.ev
    return oldest


legoregebb(ship).__str__()

def km_1980_utan(lista):
    ossz_km = 0 
    db = 0
    for i in lista:
        if i.ev > 1980:
            db += 1
            ossz_km += i.egytank

    return round(ossz_km / db, 2)

print(km_1980_utan(ship), "km")