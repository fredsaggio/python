lista1 = [1, 2, 3, 4, 5]
lista2 = ["1", "7", "2", "4", "8"]
igualdade = []

for i in range(len(lista1)):
    igual = False
    for x in range(len(lista2)):
        lista2[x] = int(lista2[x])
        if lista1[i] == lista2[x]:
            igual = True
    if igual:
        igualdade.append(lista1[i])

print(igualdade)  