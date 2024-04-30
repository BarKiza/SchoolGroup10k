import random

lista = []
lista_paros = []
for i in range(5):
    szam = random.randint(1,10)
    lista.append(szam)
    if szam % 2 == 0:
        lista_paros.append(szam)

print(lista)
print(lista_paros)
