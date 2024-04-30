def szamok_atlaga(lista):
    osszeg = 0
    for szam in lista:
        osszge += szam
    return osszeg / len(lista)

szamok = [1,2,3,4,5,6,7,8,9,10]
atlaga = szamok_atlaga(szamok)
print(atlaga)
