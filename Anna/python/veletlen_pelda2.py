import random

szam=random.randint(1,2)
if szam == 1:
   erme = "fej"
else:
   erme = "írás"

bekert = input("Fej vagy írás?")
if bekert == erme:
    print("Talált")
else:
    print("Nem talált")
