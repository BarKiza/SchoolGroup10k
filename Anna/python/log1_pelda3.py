szam = int(input("Adj meg egy számot!"))
if szam % 3 == 0:
    print("A szám osztható 3-mal")
if szam % 4 == 0:
    print("A szám osztható 4-gyel")
if szam % 3 == 0 and szam % 4 == 0:
    print("A szám osztható 3-mal és 4-gyel")
if szam % 3 == 1 or szam % 4 == 1:
    print("A szám nem osztható sem 3-mal sem 4-gyel")