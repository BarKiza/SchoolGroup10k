class Negyzet:
    def __init__(self, hossz):
       self.hossz = hossz

    def terulet(self):
        return self.hossz * self.hossz

    def kerulet(self):
        return self.hossz * 4

    def info(self):
        print(f'A(z) {self.hossz} egység oldalhosszúságú négyzet területe {self.terulet():.2f} egység, kerülete {self.kerulet():.2f} egység.') 

negyzet_01 = Negyzet(10)
print(negyzet_01.terulet())
print(negyzet_01.kerulet())
print(negyzet_01.info())
