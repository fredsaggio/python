# Demorei pra pegar um pouco a lógica dessa, relendo a questão com calma deu pra clarear a mente.

n = int(input('Digite um número.'))
n1 = 0
n2 = 1
texto = "0, 1, "

for i in range(1, n+1):
    n3 = n1 + n2
    n1 = n2
    n2 = n3
    texto += str(n3)
    if i < n:
        texto += ", "

print(texto)



# Esse aqui eu fiz primeiro porém foi feito utilizando Arrays, logo eu decidi fazer do primeiro jeito com coisas que foram ensinadas em sala de aula.

numero_usuario = int(input('Digite um número.'))

termos_total = [0, 1]
serie_termos = ""

for i in range(0, numero_usuario + 1):
    termo_seguinte = termos_total[i] + termos_total[i+1]
    termos_total.append(termo_seguinte)

print(termos_total)