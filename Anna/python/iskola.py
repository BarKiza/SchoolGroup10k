class Iskola:
    def __init__(self, fiuk, lanyok):
        self.fiuk = fiuk
        self.lanyok = lanyok

    def kiir(self):
        print("Fiúk: ", self.fiuk)
        print("Lányok: ", self.lanyok)
    
    def kiiras_fajlba(self):
        with open('osztaly.txt', 'w', encoding='utf-8') as f:
            f.write(f"Fiúk: {self:fiuk}/n")
            f.write(f"Lányok: {self:lanyok}/n")

osztaly = Iskola(15, 20)
osztaly.kiir()
osztaly.kiiras_fajlba()