szavak = []
szo = input("Adj meg egy szót!")
while szo != '':
    szavak.append(szo)
    szo = input("Adj meg egy szót!")
print(szavak)
legrovidebb = szavak[0]
leghosszabb = szavak[0]

for szo in szavak:
    if len(szo) < len(legrovidebb):
        legrovidebb = szo
    if len(szo) > len(leghosszabb):
        leghosszabb = szo

print(f'A legrövidebb szó a listában: {legrovidebb}')
print(f'A leghosszabb szó a listában: {leghosszabb}')