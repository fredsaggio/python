import os 
import time

def clear():
    return os.system('cls')

while True:
    clear()

    with open('extext/text.txt', 'r', encoding='utf-8') as arquivo:
        ler = arquivo.read()

    print(ler)

    num = input('Digite um número de 1 a 6: ')

    if not num.isnumeric():
        clear()
        print('-'*50)
        print('Apenas números são válidos, digite novamente.')
        print('-'*50)
        time.sleep(2)
        continue

    numInt = int(num)
    if numInt < 1 or numInt > 6:
        print('Número inválido, apenas número entre 1 e 6, digite novamente.')
        time.sleep(2)
        continue

    clear() 

    if numInt == 1:
        while True:
            nomeArquivo = 'extext/' + input('Digite o nome do arquivo que quer criar: ') + '.txt'

            if not os.path.exists(nomeArquivo):   
                with open(nomeArquivo, 'w', encoding='utf-8') as arquivoo:
                    escrever = arquivoo.write('Arquivo criado!')
                    print('Arquivo criado!')
                    criarMais = input('Deseja criar mais um arquivo? Digite "sim" ou "nao": ')
                    if criarMais == 'sim':
                        clear()
                        continue
                    elif criarMais == 'nao':
                        print('Voltando para o menu inicial...')
                        time.sleep(1)
                        break
                    else:
                        print('Valor inválido.')

            else:
                print('Este arquivo já existe.')
                continue
    elif numInt == 2:
        while True:
            clear()
            nomeArquivo = 'extext/' + input('Digite o nome do arquivo que quer adicionar uma frase: ') + '.txt'

            if nomeArquivo == 'extext/text.txt':
                print('Este arquivo não pode ser modificado.')
                time.sleep(1)
                continue

            if os.path.exists(nomeArquivo):

                queFrase = input('Que frase quer adicionar?')

                with open(nomeArquivo, 'a', encoding='utf-8') as arquivoo:
                    adicionar = arquivoo.write('\n' + queFrase)

                print('Conteúdo adicionado.')

                criarMais = input('Deseja adicionar conteúdo em mais algum arquivo? Digite "sim" ou "nao": ')

                if criarMais == 'sim':
                    continue
                elif criarMais == 'nao':
                    print('Voltando para o menu inicial...')
                    time.sleep(1)
                    break
                else:
                    print('Valor inválido.')
                
            else: 
                print('Este arquivo não existe, digite o nome de um arquivo existente. ')
                time.sleep(1.5)
                continue
    elif numInt == 3:
        while True: 
            clear()
            nomeArquivo = 'extext/' + input('Qual o arquivo deve ser lido: ') + '.txt' 

            if os.path.exists(nomeArquivo):
                with open(nomeArquivo, 'r', encoding='utf-8') as arquivoo:
                    lerArquivo = arquivoo.read()
                print('-' * 30)
                print(lerArquivo)
                print('-' * 30)
                time.sleep(1.5)

                lerMais = input('Deseja ler mais algum arquivo? Digite "sim" ou "nao": ')

                if lerMais == 'sim':
                    continue
                elif lerMais == 'nao':
                    print('Voltando para o menu inicial...')
                    time.sleep(1)
                    break
                else:
                    print('Valor inválido.')
            else:
                print('Esse arquivo não existe.') 
                time.sleep(1.5)
                continue
    elif numInt == 4:
        while True:
            clear()
            nomeArquivo = 'extext/' + input('Qual arquivo deve ter o conteúdo zerado: ') + '.txt' 

            if nomeArquivo == 'extext/text.txt':
                print('Valor não permitido.')
                time.sleep(1.5)
                continue

            if os.path.exists(nomeArquivo):
                with open(nomeArquivo, 'w', encoding='utf-8') as arquivoo:
                    zerarArquivo = arquivoo.write('')
                print('Arquivo limpo.')
                zerarMais = input('Deseja zerar mais um arquivo? Digite "sim" ou "nao": ')
                if zerarMais == 'sim':
                    continue
                elif zerarMais == 'nao':
                    print('Voltando para a página inicial...')
                    time.sleep(1)
                    break
                else:
                    print('Valor inválido.')
            else:
                print('Esse arquivo não existe.')
                time.sleep(1.5)
                continue
    elif numInt == 5:
        while True:
            clear()
            conteudoArquivo = 'extext/' + input('Copiar conteúdo de qual arquivo: ') + '.txt'
            nomeArquivo = 'extext/' + input('Qual o nome do novo arquivo: ') + '.txt'

            if os.path.exists(conteudoArquivo):
                with open(conteudoArquivo, 'r', encoding='utf-8') as arquivoo:
                    copiarArquivo = arquivoo.read()

                with open(nomeArquivo, 'w', encoding='utf-8') as arquivooo:
                    copiandoArquivo = arquivooo.write(copiarArquivo)

                with open(nomeArquivo, 'r', encoding='utf-8') as arquivoooo:
                    lerArquivo = arquivoooo.read()
                
                print('Conteúdo do arquivo:')
                print(lerArquivo)
                print('-'*30)
                copiarMais = input('Deseja copiar mais algum arquivo? Digite "sim" ou "nao": ')
                if copiarMais == 'sim':
                    continue
                elif copiarMais == 'nao':
                    print('Voltando para a página inicial...')
                    time.sleep(1)
                    break
                else:
                    print('Valor inválido.')
            else:
                print('Este arquivo não existe.')
                time.sleep(1.5)
                continue
    elif numInt == 6:
        print('Programa finalizado.')
        break
    