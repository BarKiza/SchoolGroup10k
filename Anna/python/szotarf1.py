nev = input("Add meg a kutya nevét!")
fajta = input("Add meg a kutya fajtáját!")
eletkor = input("Add meg a kutya életkorát!")
oltas = input("Rendelkezik oltással? [true,false]")
kutya = {
    'nev': nev,
    'fajta': fajta,
    'eletkor': eletkor,
    'oltas': oltas,
}
print(kutya)

for kulcs in kutya:
    print(kulcs, kutya[kulcs])