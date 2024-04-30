import random
def atlag_es_indexek(lista):
    osszeg = sum(lista)
    atlag =  osszeg / len(lista)
    nagyobbbak = [i for i in range(len(lista)) if lista[i] > atlag]
    return atlag, nagyobbbak

szamok = []
szam = input("Adja meg az első számot: ")
while szam != "":
    szamok.append(int(szam))
    szam = input("Adja meg a következő számot (Enterrel kilép): ")
    
atlag, nagyobbak = atlag_es_indexek(szamok)
print("Az átlag: ", atlag)
print("Az átlagnál nagyobb elemek indexei: ", nagyobbak)