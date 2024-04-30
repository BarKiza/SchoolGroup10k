import random

class IdojarasAdat:
    def __init__(self, varos, homerseklet, elorejelzes):
        self.varos = varos
        self.homerseklet = homerseklet
        self.elorejelzes = elorejelzes

    def informacio_megjelenites(self):
        print("Város: ", self.varos)
        print("Jelenlegi hőmérséklet: ", self.elorejelzes)

def idojaras_elorejelzes_megszerzese(varos):
    elorejelzesek = ["Napos", "Felhős", "Esős", "Havas", "Ködös"]
    return random.choice(elorejelzesek)

def atlaghomerseklet_megfigyeles(varos):
    return random.randint(10, 25)

#1.feladat
print('1. feladat:')
kivalasztott_varos = input("Válassz egy várost a listából: ")
elorejelzesek = ["Napos", "Felhős", "Esős", "Havas", "Ködös"]
elorejelzes = random.choice(elorejelzesek)
print("Az időjárás előrejelzése ", kivalasztott_varos + "-ra", elorejelzes)

#2.feladat
print('2. feladat:')
varos = input("Add meg a várost amelynek az átlaghőmérsékletet szeretnéd megtudni")
atlaghomerseklet = atlaghomerseklet_megfigyeles(varos)
print("Az átlaghőmérséklet ", varos + "-ban", atlaghomerseklet, "Celsius-fok")

#3.feladat
print('3. feladat:')
varos_nev = input("Add meg a város nevét: ")
jelenlegi_homerseklet = atlaghomerseklet_megfigyeles(varos_nev)
idojaras_elorejelzes = idojaras_elorejelzes_megszerzese(varos_nev)

idojaras_adat = IdojarasAdat(varos_nev, jelenlegi_homerseklet, idojaras_elorejelzes)
idojaras_adat.informacio_megjelenites()