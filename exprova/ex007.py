numero = int(input('Digite um número: '))
serie = ""
soma = 0

for i in range(1, numero+1):
    termo = (i/(i-1+(i*1)))
    termo2 = f'{i}/{(i-1+(i*1))}'
    soma += termo
    serie += termo2
    if i < numero:
        serie += " + "

print(f'{serie} = {soma:.3f}')