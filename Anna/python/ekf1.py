import random

lista = []
for i in range(5):
    szam = random.randint(1,7)
    lista.append(szam)

szam2 = int(input("Adj meg egy számot!"))

talalat = False
index = 0
while index < len(lista) and not talalat:
    if lista[index]  == szam2:
        talalat = True
    index = index + 1
print(lista)
if talalat:
    print('Van a listában a felhasználó által megadott szám.')
else:
     print('Nincs a listában a felhasználó által megadott szám.')
