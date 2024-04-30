programozasi_nyelvek = []
with open('programozasi_nyelvek.csv', 'r', encoding='utf-8') as forrasfajl:
    for sor in forrasfajl:
        adatok = sor.strip().split(';')
        program_nyelv = {'year': int(adatok[0]), 'programing language': adatok[1], 'first name': adatok[2], 'last name': adatok[3]}
        programozasi_nyelvek.append(program_nyelv)

print(f'{programozasi_nyelvek=}')