# Questão 1:

while True:

    palavra = str(input('Digite uma string com letras e números.'))
    letras = ''
    numeros = ''

    if ' ' in palavra:
        print('Não pode haver espaços na string.')
        continue # Coloquei o 'continue' pra fazer a função de reiniciar o loop caso o valor do if seja 'true'.

    for i in range(len(palavra)):
        if palavra[i].isnumeric():
            numeros += palavra[i]
        if not palavra[i].isnumeric():
            letras += palavra[i]

    if len(numeros) < 1 or len(letras) < 1:
        print('Sua string deve conter ao menos uma letra e um número.')
        continue

    print(f'Letras: {letras}, números: {numeros}')
    break

