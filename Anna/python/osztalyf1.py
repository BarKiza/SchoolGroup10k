class Kor:
    pi = 3.1415

    def __init__(self,r):
        self.r = r
    
    def terulet(self):
        return self.pi * self.r ** 2

    def kerulet(self):
        return 2 * self.pi * self.r

r = float(input("Kérem a kör sugarát:"))
kor = Kor(r)
print(f"A kör területe:{kor.terulet()}")
print(f"A kör kerülete:{kor.kerulet()}")
