from os.path import exists

while True:
    num = int(input('Digite um número de 1 a 6: '))

    if 1 > num > 6:
        print('Número inválido, apenas número entre 1 e 6.')
        continue

    if not num.isnumeric():
        print('Apenas número!')
        continue

    with open('text.txt', 'r', encoding='utf-8') as arquivo:
        ler = arquivo.read()

    print(ler)

    while True:
        if num == 1: 
            nomeArquivo = input('Digite o nome do arquivo que quer criar: ')
            parametro = criarArquivo(nomeArquivo + ".txt")
            def criarArquivo(arquivo):
                with open(arquivo, 'r', encoding='utf-8') as arquivoo:
                    lerr = arquivoo.read()

                if exists(arquivoo):
                    print('Este arquivo já existe.')
                return print(lerr)
        