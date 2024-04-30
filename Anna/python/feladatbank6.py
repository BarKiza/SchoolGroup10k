def min_max_kulonbseg(lista):
    min_szam = min(lista)
    max_szam = max(lista)
    kulonbseg = max_szam - min_szam
    return kulonbseg

szamok = []
szam = input("Adja meg az első számot: ")
while szam != "":
    szamok.append(int(szam))
    szam = input("Adja meg a következő számot (Enterrel kilép): ")

kulonbseg = min_max_kulonbseg(szamok)
print(kulonbseg)