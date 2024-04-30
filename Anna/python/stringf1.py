mondat = input("Adj meg egy mondatot!")

if mondat[-1] == '?':
    print("Ez a mondat kérdő mondat")
elif mondat[-1] == '.':
    print("Ez a mondat kijelentő mondat")
else:
    print("Ez vagy felkiáltó / felszólító / óhajtó mondat")