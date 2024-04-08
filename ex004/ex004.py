numero_usuario = int(input('Digite um número.'))

termos_total = [0, 1]
serie_termos = ""

for i in range(0, numero_usuario + 1):
    termo_seguinte = termos_total[i] + termos_total[i+1]
    termos_total.append(termo_seguinte)

print(termos_total)