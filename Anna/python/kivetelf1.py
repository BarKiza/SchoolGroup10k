szamok = []
try:
    szam = int(input("Adj meg egy számot!"))
except ValueError as e:
    print('Hiba: ', e)
    print('Nem számot adtál meg!')