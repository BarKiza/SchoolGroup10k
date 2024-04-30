
class Diak:
    def __init__(self, nev, jegyek):
        self.nev = nev
        self.jegyek = jegyek
    
    def atlag(self):
        return sum(self.jegyek) / len(self.jegyek)
    
    def jegyek_fajlba(self, fajlnev):
        with open(fajlnev, "w") as f:
            f.write(f"{self.nev} jegyei:\n")
            for jegy in self.jegyek:
                f.write(str(jegy) + "\n")
                
nev = input("Kérem a diák nevét: ")
jegyek = []
while True:
    jegy = input("Kérem a jegyet (vagy írja be a 'q'-t a kilépéshez): ")
    if jegy == "q":
        break
    jegyek.append(int(jegy))

diak = Diak(nev, jegyek)
print(f"{diak.nev} átlaga: {diak.atlag()}")
diak.jegyek_fajlba("jegyek.txt")