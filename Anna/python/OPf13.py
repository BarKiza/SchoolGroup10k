class Negyzet:
    def __init__(self, hossz):
       self.hossz = hossz

    def terulet(self):
        return self.hossz * self.hossz

    def kerulet(self):
        return self.hossz * 4

    def info(self):
        print(f'A(z) {self.hossz} egység oldalhosszúságú négyzet területe {self.terulet():.2f} egység, kerülete {self.kerulet():.2f} egység.') 


negyzet_lista = []
hossz = int(input("Add meg a négyzet oldalhosszát!"))
while hossz != 0:
    negyzet = Negyzet(hossz)
    negyzet_lista.append(negyzet)
    hossz = int(input("Add meg a négyzet oldalhosszát!"))

for negyzet in negyzet_lista:
    print(negyzet.info())
