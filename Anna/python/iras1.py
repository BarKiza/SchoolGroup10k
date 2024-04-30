
with open('nyelvek.txt', 'r', encoding='utf-8') as forrasfajl, \
    open('nyelvek_masolat.txt', 'w', encoding='utf-8') as celfajl:
        for sor in forrasfajl:
            szavak = sor.strip().split(';')
            print(szavak[0], szavak[1], file=celfajl)