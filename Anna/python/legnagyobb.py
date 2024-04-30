def legnagyobb_elem(lista):
    legnagyobb = lista[0]
    for elem in lista:
        if elem > legnagyobb:
            legnagyobb = elem
        return legnagyobb

lista = [1, 5, 3, 7, 2]
max_elem = legnagyobb_elem(lista)
print("A lista legngaobb eleme:", max_elem)