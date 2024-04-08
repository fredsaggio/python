numero_usuario = int(input('Digite um número.'))

soma_total = 0
frase_serie = ""

for i in range(1, numero_usuario + 1):
    valor = int('2' * i)
    soma_total += valor
    frase_serie += str(valor)
    if i < numero_usuario:
        frase_serie += "+"

print(f'{frase_serie} = {soma_total}')