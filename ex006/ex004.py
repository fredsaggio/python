# Método com a função "sort()":

lista = []

for i in range(6):
    num = int(input(f'Digite o {i}° número: '))
    lista.append(num)

lista.sort()

print(lista)



# Método sem funções:

lista2 = []

for j in range(6):
    num = int(input(f'Digite o {j}° número: '))
    lista2.append(num)

for x in range(len(lista2)):
    for y in range(x + 1, len(lista2)):
        if lista2[x] > lista2[y]:
           lista2[x], lista2[y] = lista2[y], lista2[x] # Não sabia que dava pra fazer isso

print(lista2)
