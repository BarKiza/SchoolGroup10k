class Diak:
    def __init__(self, nev, osztaly):
        self.nev = nev
        self.osztaly = osztaly

    def info(self):
        print(f'Szia, a nevem {self.nev}, és a(z) {self.osztaly}ba járok.')


class Tanar:
    def __init__(self, nev, szakok):
        super().__init__(nev)
        self.szakok = szakok

    def info(self):
        print(f'Hello a nevem {self.nev}, {self.szakok} szakos tanár vagyok.'
        )


diak01 = Diak('Kiss Péter', '10.A')
diak02 = Diak('Aranyás Anna' '10.K')
tanar01 = Tanar()