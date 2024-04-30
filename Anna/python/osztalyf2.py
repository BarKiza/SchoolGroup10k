class Haromszog:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
	    self.c = c

    def terulet(self):
        s = (self.a + self.b + self.c) / 2
        return (s * (s - self.a) * (s - self.b) * (s - self.c)) ** 0.5
    
    def kerulet(self):
       return self.a + self.b + self.c


a = float(input("Kérem a háromszög 'a' oldalát: "))
b = float(input("Kérem a háromszög 'b' oldalát: "))
c = float(input("Kérem a háromszög 'c' oldalát: "))

h = Haromszog()
print(f"A háromszög területe: {h.terulet()}")
print(f"A háromszög kerülete: {h.kerulet()}")
