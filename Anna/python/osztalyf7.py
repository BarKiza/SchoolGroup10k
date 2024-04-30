class Osztok:
    def __init__(self, szam):
        self.szam = szam

    def osztok(self):
        osztok = []
        for i in range(1, self.szam + 1):
            if self.szam % i == 0:
                osztok.append(i)
        return osztok

    def prim(self):
        if self.szam < 2:
            return False
        for i in range(2, int(self.szam ** 0.5) + 1):
            if self.szam % i == 0:
                return False
        return True

szam = int(input("Kérem adjon meg egy egész számot: "))

osztok = Osztok(szam).osztok()
if Osztok(szam).prim():
    print(f"A(z) {szam} prímszám.")
else:
    print(f"A(z) {szam} nem prímszám.")
print(f"A(z) {szam} osztói: {osztok}")
