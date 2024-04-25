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