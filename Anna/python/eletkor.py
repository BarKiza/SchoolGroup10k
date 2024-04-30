kor = int(input("Kérem adja meg az életkorát!"))
if kor < 0:
    print("Sajnálom, de nem lehet minusz")
elif kor < 18:
    print("Ön még kiskorú")
elif kor < 65 and kor > 18:
    print("Ön már felnőtt")
elif kor > 65:
    print("Ön már időskorú")
