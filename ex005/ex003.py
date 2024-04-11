# Nas primeiras tentativas eu tentei aninhar 2 "while", mas deu erro porque o while rodava tudo de uma vez, já esse for vai de passo em passo (explicação do chatGPT).

# Demorei horas pra fazer esse código aí funcionar perfeitamente, sempre dava algum erro com a lógica dos if's.

while True:
  i = 0          
  numeros = ""
  letras = ""
  senha = str(input('Digite uma senha: '))

  for caractere in senha:        
    if caractere.isnumeric():
      numeros += caractere
    else: 
      letras += caractere

  if len(numeros) < 1 or len(letras) < 1:
    print('Deve haver no mínimo 1 letra e um número.')

  if len(senha) < 8 or len(senha) > 16:
    print('Senha inválida, no mínimo 8 e no máximo 16 caracteres.')

  if 8 <= len(senha) <= 16 and len(numeros) >= 1 and len(letras) >= 1:
    print('Senha válida!')
    break