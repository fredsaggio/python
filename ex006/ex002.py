lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
sub_lista = []
num = int(input("Digite um número: "))

for i in range(0, len(lista), num):
    sub_lista.append(lista[i:i+num])

print("Sub-listas:", end=" ")

for i in range(len(sub_lista)):

    if i == len(sub_lista) - 1:
        print(sub_lista[i], end="")
        break

    print(sub_lista[i], end=", ")
