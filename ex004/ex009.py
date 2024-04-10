# Essa eu achei a mais fácil das 9 mesmo sendo a mais verbosa, kkkkkkkkkkkkkkkkk (Isso se eu entendi a questão, né)

valor_voto = None
candidato_1 = 0
candidato_2 = 0
candidato_3 = 0
candidato_4 = 0
branco = 0
nulo = 0

while valor_voto != 0:

    valor_voto = int(input('Digite o número do voto.'))

    if valor_voto == 1: 
        candidato_1 += 1
    if valor_voto == 2: 
        candidato_2 += 1
    if valor_voto == 3: 
        candidato_3 += 1
    if valor_voto == 4: 
        candidato_4 += 1
    if valor_voto == 5: 
        nulo += 1
    if valor_voto == 6: 
        branco += 1
    if valor_voto > 6:
        print('Digite um valor de 1 a 6.')

total_votos = candidato_1 + candidato_2 + candidato_3 + candidato_4 + nulo + branco

print('----------------------------------------',
      f'Votos para o candidato 1: {candidato_1}',
      f'Votos para o candidato 2: {candidato_2}',
      f'Votos para o candidato 3: {candidato_3}',
      f'Votos para o candidato 4: {candidato_4}',
      f'Votos nulos: {nulo}',
      f'Votos em branco:{branco}',
      f'Porcentagem de votos nulos sobre o total de votos: {(nulo/total_votos * 100):.2f}%', 
      f'Porcentagem dos votos em branco sobre o total de votos: {(branco/total_votos * 100):.2f}%',
      '----------------------------------------', sep="\n")


