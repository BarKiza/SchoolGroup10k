bekert_szam = int(input("Adj meg egy páros számot!"))
sor = 1
darab_karakter = 1
while sor <= bekert_szam/2:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('0', end='')
        oszlop = oszlop + 1
        print('')
    darab_karakter = darab_karakter + 1
    sor = sor + 1

darab_karakter = bekert_szam/2
sor = 1
while sor <= bekert_szam/2:
    oszlop = 1
    while oszlop <= darab_karakter:
        print('0', end='')
        oszlop = oszlop + 1
        print('')
    darab_karakter = darab_karakter - 1
    sor = sor - 1
