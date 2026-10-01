# 25. Dada a lista [3, 7, 1, 9, 4], exiba os itens na ordem inversa.

lista = [3, 7, 1, 9, 4]

# para i de 5 ate 1 passo -1 faca
for i in range(len(lista) - 1, -1, -1):
    print(lista[i])