numero = int(input('Digite um número: '))
n1 = 0
n2 = 1
serie = "0, 1, "

for i in range(1, numero+1):
    termo = n1 + n2 
    n1 = n2 
    n2 = termo
    serie += str(termo)

    if i < numero:
        serie += ", "

print(serie)