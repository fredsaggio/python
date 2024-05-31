# Gerenciador de Senhas

# Dicionário para armazenar as credenciais do usuário
credenciais = {}

def cadastrar_usuario():
    print("Cadastro de Novo Usuário")
    username = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    credenciais[username] = senha
    print("Usuário cadastrado com sucesso!")

def fazer_login():
    print("Login")
    username = input("Digite o nome de usuário: ")
    senha = input("Digite a senha: ")
    if username in credenciais and credenciais[username] == senha:
        print("Login bem-sucedido!")
        return True
    else:
        print("Nome de usuário ou senha incorretos.")
        return False

def menu_principal():
    print("\nBem-vindo ao Gerenciador de Senhas")
    print("1. Cadastrar Novo Usuário")
    print("2. Fazer Login")
    print("3. Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        cadastrar_usuario()
    elif escolha == "2":
        if fazer_login():
            # Se o login for bem-sucedido, você pode adicionar aqui as funcionalidades adicionais
            print("Você está logado.")
    elif escolha == "3":
        print("Saindo...")
        return False
    else:
        print("Opção inválida. Tente novamente.")

    return True

# Loop principal do programa
executando = True
while executando:
    executando = menu_principal()