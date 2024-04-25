numero = int(input('Digite um número: '))
serie = ""
soma = 0

for i in range(1, numero+1):
    termo = ("2" * i)
    soma += int(termo)
    serie += termo
    if i < numero:
        serie += " + "

print('Série: {} = {}'.format(serie, soma))

