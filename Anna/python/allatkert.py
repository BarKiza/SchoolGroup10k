class Allatkert:
    def __init__(self, novenyek, allatok):
       self.novenyek = novenyek
       self.allatok = allatok

    def kiir(self):
        print("Növények: ", self.novenyek)
        print("Állatok: ", self.allatok)

    def kiiras_fajlba(self):
        with open('allatkert.txt', 'w', encoding='utf-8') as f:
            f.write(f"Növények: {self.novenyek}/n")
            f.write(f"Állatok: {self.allatok}/n")

allatkert = Allatkert(45, 67)
allatkert.kiir()
allatkert.kiiras_fajlba()