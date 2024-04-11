while True:
    try:
        n = int(input('Digite um número: '))
        break
    except ValueError:
        print('Valor inválido, digite um número inteiro.')

soma = 0

for i in range(1, n+1):
    while True:
        try:
            valor = int(input(f'Digite o {i}º valor'))
            soma += valor
            break
        except ValueError:
            print('Digite um número inteiro.')

media = soma / n

print(f'A média dos valores recebidos é de: {media:.2f}')