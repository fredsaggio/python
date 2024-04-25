# Nas primeiras tentativas eu tentei aninhar 2 "while", mas deu erro porque o while rodava tudo de uma vez, já esse for vai de passo em passo (explicação do chatGPT).

# Demorei horas pra fazer esse código aí funcionar perfeitamente, sempre dava algum erro com a lógica dos if's.

while True:
    i = 0          
    flag_num = False
    flag_str = False
    senha = str(input('Digite uma senha: '))

    if 8 <= len(senha) <= 16:
        for i in range(len(senha)):

            if senha[i].isnumeric():
                flag_num = True
            else:
                flag_str = True

        if flag_num and flag_str:
            print('Senha válida!')
            break
        else: 
            print('Senha inválida! Pelo menos uma letra e um número!')
    else:
        print('No mínimo 8 caracteres e no máximo 16!')