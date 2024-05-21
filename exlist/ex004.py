# Escreva um programa que receba uma palavra e retorne em que índice da lista (pré-estabelecida) de palavras a que foi recebida está, ou se não estiver contida na lista, printe uma mensagem de erro.

lista = ['pelo', 'goiaba', 'unha', 'professor', 'grama', 'papel', 'oceano', 'desenho', 'vento', 'jogo']
palavra = input('Digite uma palavra: ')
dentro = False

for i in lista:
    if palavra == i:
        print('Está dentro da lista.')
        dentro = True
        break

if not dentro:
    print('Não está dentro da lista.')

