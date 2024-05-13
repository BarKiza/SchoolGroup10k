def tavolsagok(menetido, sebesseg):
    return (menetido / 60) * sebesseg

menetido_perc = int(input("Írja be a hajónak a hajózási idejét percekben: "))
sebesseg_km_h = int(input("Írja be a hajóna ka sebességét km/h-ban: "))

tavolsag_km = tavolsagok(menetido_perc, sebesseg_km_h)
print(f"A megtett távolság {tavolsag_km} km.")


def szerviz(gyartas):
    hajoev = 2024 - gyartas
    if hajoev >= 10:
        print("A hajót évente kell szervizelni.")
    elif hajoev >= 3:
        print("A hajót két évente kell szervizelni.")
    else: 
        print("A hajót minden 3 évente kell szervizelni.")
    
gyartas = int(input("Írja be a hajónak a gyártási évét: "))
szerviz(gyartas)