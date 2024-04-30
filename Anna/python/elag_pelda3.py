import random
gondolt_szam = random.randint(1,5)
szam = int(input("Adj meg egy számot"))
if szam == gondolt_szam:
    print("Eltaláltad")
elif szam > gondolt_szam:
    print("Nagyobb mint gondoltam")
else:
    print("Kisebb mint gondoltam")
    print("Erre a számra gondoltam: ",  gondolt_szam)