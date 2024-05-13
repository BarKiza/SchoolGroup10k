while True:
    hajonev = input("Írja be a hajó nevét: ")
    gyartas = int(input("Írja be a hajó gyártási évét: "))

    if gyartas < 1950 or 2024 - gyartas < 10:
        print("A gyártási évnek 1950 vagy későbbnek kell lennie, és "
        "a hajónak legalább 10 évesnek kell lennie.")

    else:
        break

hajoev = 2024 - gyartas
print(f"Ezt írtad be: {hajonev}")
print(f"A hajó {hajoev} éves.")
print(f"A hajó nevében {len(hajonev)} betű van.")