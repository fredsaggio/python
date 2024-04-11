soma = 0
media = 0 
i = 0 # Adicionado pra contar a quantidade de valores recebidos


while True:

    num_usuario = int(input('Digite um número, para parar digite -1: '))

    if num_usuario == -1:
        print('Finalizado.')
        break

    soma += num_usuario
    i+=1 # Colocado apenas no final para não dar conflito com o 'if', caso fosse adicionado antes do if, entraria na contagem da media e daria erro no cálculo.

media = soma / i

print(f'A soma total dos números digitados foi de: {soma}')
print(f'A média da soma dos números é de: {media:.2f}') # Poderia ter feito 'soma/i' também que daria na mesma.