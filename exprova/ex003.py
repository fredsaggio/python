numero = int(input('Digite um número: '))

for i in range(numero-1, 1, -1):
    numero *= i

print(f'Fatorial: {numero}')