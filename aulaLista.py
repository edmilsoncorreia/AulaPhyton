lista = [0, 1, 2, 3, 4, 5, 6, 7, 8]
print(lista)

lista4 = lista[0:4]
print(lista4)

listaSlicelen = lista[4:len(lista)]
print(listaSlicelen)

listaPares = lista[0:len(lista):2]
print(listaPares)

listaCopiada = lista[0:len(lista)]
print(listaCopiada)

listaCopy = lista.copy()
print(listaCopy)