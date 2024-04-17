'''
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
'''

'''
#FILA
from collections import deque
lista = deque([0, 1, 2, 3, 4])
lista.append(5)
print(lista)
lista.pop()
print(lista)
lista.popleft()
print(lista)
'''

'''
#CRIANDO UMA LISTA DA DOS MÚLTIPLOS DE 2
lista = []
for i in range(11):
    lista.append(i*2)
    print(lista)

#OUTRA MANEIRA DE TER O MESMO RESULTADO
lista2 = [i*2 for i in range(11)]
print(lista2)
'''

#CRIANDO UMA LISTA TRANSPOSTA
matriz = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
transposta = [[linha[i] for linha in matriz] for i in range(4)]
print(matriz)
print(transposta)
