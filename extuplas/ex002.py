tupla = ['amor', 'abraço', 'prato', 'tomada', 'rosa', 'bolsa']
dado = input('Digite uma palavra: ')
incluso = False

for i in tupla:
    if dado == i:
        tupla.remove(dado)
        print(f'Dado removido! Sua nova tupla é: {tupla}')
        incluso = True
        break

if not incluso:
    print('Não está dentro da tupla.')