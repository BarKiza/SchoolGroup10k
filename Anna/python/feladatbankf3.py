def szavak_szama(szoveg):
    szavak = szoveg.split()
    return len(szavak)

mondat = "Ez egy példa mondat."
szavak = szavak_szama(mondat)
print(szavak)