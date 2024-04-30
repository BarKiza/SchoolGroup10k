class Szoba:
    def __init__(self, azonosito, ferohely):
        self.azonosito = azonosito
        self.ferohely = ferohely
        self.foglalt = False
    
    def foglal(self):
        self.foglalt = True
        
    def szabad(self):
        self.foglalt = False

szobak = [
    Szoba("101", 2),
    Szoba("102", 1),
    Szoba("103", 4),
    Szoba("201", 3),
    Szoba("202", 2),
    Szoba("203", 1),
]

datum = input("Kérem a dátumot (YYYY-MM-DD): ")

szabad_szobak = []
for szoba in szobak:
    if not szoba.foglalt:
        szabad_szobak.append(szoba)

szabad_szobak_fajlba = []
for szoba in szabad_szobak:
    szabad_szobak_fajlba.append(f"{szoba.azonosito} ({szoba.ferohely} fő)")

with open("szabad_szobak.txt", "w") as f:
    f.write(f"Szabad szobák a következő dátumra: {datum}\n\n")
    if szabad_szobak_fajlba:
        f.write("\n".join(szabad_szobak_fajlba))
    else:
        f.write("Nincsenek szabad szobák.")