class Termek:
    def __init__(self, nev, ar, keszlet):
        self.nev = nev
        self.ar = ar
        self.keszlet = keszlet

termekek = [
    Termek("Telefon", 49990, 5),
    Termek("Laptop", 149990, 3),
    Termek("Tablet", 79990, 2),
]

rendeles = input("Kérem a rendelni kívánt termék nevét: ")

for termek in termekek:
    if termek.nev.lower() == rendeles.lower():
        if termek.keszlet > 0:
            mennyiseg = int(input("Kérem a rendelt mennyiséget: "))
            if mennyiseg <= termek.keszlet:
                osszeg = mennyiseg * termek.ar
                termek.keszlet -= mennyiseg
                print(f"A rendelés összege: {osszeg}")
            else:
                print("Nincs elegendő készlet.")
        else:
            print("Nincs készleten.")
        break
else:
    print("Nem található ilyen termék.")

keszlet_fajlba = []
for termek in termekek:
    keszlet_fajlba.append(f"{termek.nev}: {termek.keszlet} db")

with open("keszlet.txt", "w") as f:
    f.write("\n".join(keszlet_fajlba))
