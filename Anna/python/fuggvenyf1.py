def osszegzo(x, *args):
    osszeg = x
    for szam in args:
        osszeg += szam
    return osszeg

print(osszegzo(1,2,3,10,100))
    