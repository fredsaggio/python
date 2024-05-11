lista1 = [1, 2, 3, 4]
lista2 = [2, 4, 5, 6, 7, 8]
diferenca = []

for i in range(len(lista1)):
    semelhante = False
    for j in range(len(lista2)):
        if lista1[i] == lista2[j]:
            semelhante = True
            break
    if not semelhante:
        diferenca.append(lista1[i])


for i in range(len(lista2)):
    semelhante = False
    for j in range(len(lista1)):
        if lista2[i] == lista1[j]:
            semelhante = True
            break
    if not semelhante:
        diferenca.append(lista2[i])

print(diferenca)