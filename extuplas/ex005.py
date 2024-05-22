dicionario = {}
nome = input('Digite seu nome: ')
senha = input('Digite sua senha: ')
cpf = input('Digite seu cpf: ')

dicionario['nome'] = nome
dicionario['senha'] = senha
dicionario['cpf'] = cpf

print(dicionario)

while True:
    login = input('Digite seu nome de usuário: ')
    senhaa = input('Digite sua senha: ')

    if login != nome or senhaa != senha:
        print('Nome de usuário ou senha incorretos.')
    else: 
        print('Bem-vindo!')
        break