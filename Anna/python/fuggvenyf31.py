lista = []
szam = int(input("Adj meg egy pozitív számot!"))
while szam >= 0:
    lista.append(szam)
    szam = int(input("Adj meg egy pozitív számot!"))
print(lista)
def harommal_oszthatok(lista):
    darab = 0
    for elem in lista:
        if elem % 3 == 0:
            darab += 1
    return darab

print(harommal_oszthatok(lista))    