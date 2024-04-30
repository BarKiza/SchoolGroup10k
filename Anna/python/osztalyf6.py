
class Auto:
    def __init__(self, tipus, ar, db):
        self.tipus = tipus
        self.ar = ar
        self.db = db

autok = [
    Auto("Suzuki Swift", 3490000, 5),
    Auto("Opel Corsa", 3790000, 3),
    Auto("Toyota Yaris", 4190000, 2),
]

vasarlas = input("Kérem a vásárolni kívánt autó típusát: ")

for auto in autok:
    if auto.tipus.lower() == vasarlas.lower():
        if auto.db > 0:
            db = int(input("Kérem a vásárolni kívánt darabszámot: "))
            if db <= auto.db:
                osszeg = db * auto.ar
                auto.db -= db
                print(f"A vásárlás összege: {osszeg}")
            else:
                print("Nincs elegendő készlet.")
        else:
            print("Nincs készleten.")
        break
else:
    print("Nem található ilyen autó típus.")

darabszamok_fajlba = []
for auto in autok:
    darabszamok_fajlba.append(f"{auto.tipus}: {auto.db} db")

with open("darabszamok.txt", "w") as f:
    f.write("\n".join(darabszamok_fajlba))
