def legrovidebb_szo():
    szavak = [input("Adj meg egy szót!")
    for i in range(3)]
    legrovidebb = min(szavak, key=len)
    print("A legrövidebb szó:", legrovidebb)

legrovidebb_szo()