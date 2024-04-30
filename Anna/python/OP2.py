import random

class Kutya:
    nem = ['kan', 'nosteny']

    def __init__(self, nev):
        self.nev = nev
        self.eletkor = random.randint(1, 15)
        self.nem = random.choice(self.nem)

    def info(self):
        return f"Név: {self.nev}, Életkor: {self.eletkor}, Neme: {self.nem}"


kutyak_szama = int(input('Kérem adja meg a kutyák számát: '))
kutyak = []
for i in range(kutyak_szama):
    nev = input(f"Kérem adja meg a(z) {i+1}. kutya nevét!")
    kutyak.append(Kutya(nev))

print("A megadott kutyák adatai:")
for kutya in kutyak:
    print(kutya.info())