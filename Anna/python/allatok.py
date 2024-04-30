allat1 = input("Kérem az első állat nevét: ")
allat2 = input("Kérem az második állat nevét: ")
allat3 = input("Kérem az harmadik állat nevét: ")

allatok = [allat1, allat2, allat3]
allatok.sort()

print("Az állaok ábécé sorrendben: ")
for allat in allatok:
    print(allat)