def osszehasonlit(szam1, szam2):
    if szam1 > szam2:
        print(szam1, "nagyobb mint", szam2)
    elif szam1 < szam2:
        print(szam2, "nagyobb mint", szam1)
    else:
        print("A két szám egyenlő.")

osszehasonlit(1,5)
osszehasonlit(9,6)
osszehasonlit(5,3)