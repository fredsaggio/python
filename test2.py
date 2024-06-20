import json

# Função para carregar os dados do arquivo, se existir
def carregar_dados(arquivo):
    try:
        with open(arquivo, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        # Se o arquivo não existir, retorna um dicionário vazio
        return {}

# Função para salvar os dados no arquivo
def salvar_dados(dados, arquivo):
    with open(arquivo, 'w') as file:
        json.dump(dados, file)

# Função para registrar uma visita
def registrar_visita(registro_de_visitas):
    cpf = input("Digite o CPF do visitante: ")
    nome = input("Digite o nome do visitante: ")

    if cpf in registro_de_visitas:
        print("Bem-vindo de volta,", registro_de_visitas[cpf]["nome"], "!")
    else:
        print("Bem-vindo pela primeira vez,", nome, "!")
        familiaridade = input("Qual é a sua relação com o réu? ")
        contato = input("Digite seu número de contato: ")
        endereco = input("Digite seu endereço: ")
        naturalidade = input("Qual é a sua naturalidade? ")
        idade = input("Qual é a sua idade? ")

        # Adicionando os dados do visitante ao registro
        registro_de_visitas[cpf] = {
            "nome": nome,
            "familiaridade": familiaridade,
            "contato": contato,
            "endereco": endereco,
            "naturalidade": naturalidade,
            "idade": idade
        }
        salvar_dados(registro_de_visitas, 'dados_visitas.json')

    print('Seus dados foram salvos :)')

# Função para verificar se um réu pode receber visita
def verificar_pode_receber_visita(nome_reu):
    dados = carregar_dados('dados_reus.json')
    if "reus" in dados:
        if nome_reu in dados["reus"]:
            if dados["reus"][nome_reu]["pode_receber_visita"]:
                return f"O réu {nome_reu} pode receber visita."
            else:
                return f"O réu {nome_reu} não pode receber visita."
        else:
            return f"O nome do réu '{nome_reu}' não foi encontrado na lista."
    else:
        return "Chave 'reus' não encontrada nos dados."

# Função para adicionar um réu que não pode receber visita
def adicionar_reu_sem_visita(nome_reu):
    dados = carregar_dados('dados_reus.json')
    if "reus" in dados:
        if nome_reu in dados["reus"]:
            dados["reus"][nome_reu]["pode_receber_visita"] = False
            salvar_dados(dados, 'dados_reus.json')
            print(f"O réu {nome_reu} foi adicionado à lista de não permitidos a receber visita.")
        else:
            print(f"O nome do réu não foi encontrado na lista.")
    else:
        print("Chave 'reus' não encontrada nos dados.")

# Função para agendar uma visita
def agendar_visita(detentos, detento, horario, visitante, duracao, instrucoes):
    if detento in detentos:
        horarios_disponiveis = detentos[detento]["horarios"]
        if horario in horarios_disponiveis:
            # Implemente sua lógica de agendamento aqui
            # Por enquanto, vamos apenas retornar uma mensagem
            return f"Visita agendada para {detento} no horário {horario}."
        else:
            return f"O horário {horario} não está disponível para visita do {detento}. Horários disponíveis: {', '.join(horarios_disponiveis)}"
    else:
        return f"{detento} não encontrado na lista de detentos."


# Parte principal do programa
# Criar a estrutura inicial dos dados_reus.json
dados_reus_inicial = {
    "reus": {
        "Antonio freitas": {"horarios": ["09:00", "10:00"], "instrucoes": "não levar aparelho celular", "pode_receber_visita": True},
        "Ygor gabriel": {"horarios": ["10:00", "11:00"], "instrucoes": "não levar aparelho celular", "pode_receber_visita": False},
        "Antony gama": {"horarios": ["09:00", "10:00"], "instrucoes": "não levar aparelho celular", "pode_receber_visita": True},
        "Caio cesar": {"horarios": ["10:00", "11:00"], "instrucoes": "não levar aparelho celular", "pode_receber_visita": True},
        "Carlos eduardo": {"horarios": ["09:00", "10:00"], "instrucoes": "não levar aparelho celular", "pode_receber_visita": False},
        "Fred sanggio": {"horarios": ["09:00", "10:00"], "instrucoes": "não levar aparelho celular", "pode_receber_visita": True},
        "Lucas": {"horarios": ["10:00", "11:00"], "instrucoes": "não levar aparelho celular", "pode_receber_visita": True},
        "Gustavo henrique": {"horarios": ["09:00", "10:00"], "instrucoes": "não levar aparelho celular", "pode_receber_visita": False},
        "Lucas teodosio": {"horarios": ["09:00", "10:00"], "instrucoes": "não levar aparelho celular", "pode_receber_visita": False},
        "Joao marcelo": {"horarios": ["10:00", "11:00"], "instrucoes": "não levar aparelho celular", "pode_receber_visita": True},
        "Joao gabriel": {"horarios": ["09:00", "10:00"], "instrucoes": "não levar aparelho celular", "pode_receber_visita": False},
    }
}

# Salvar a estrutura inicial dos dados_reus.json
salvar_dados(dados_reus_inicial, 'dados_reus.json')

# Carregar os dados de visitas e réus
registro_de_visitas = carregar_dados('dados_visitas.json')

# Chamar a função para registrar uma visita
registrar_visita(registro_de_visitas)

# Agora, podemos verificar se um réu pode receber visita
nome_do_reu = input('Digite o nome completo do presidiário: ')
resultado_verificacao = verificar_pode_receber_visita(nome_do_reu)
print(resultado_verificacao)
print("Verificando o possível agendamento")

# Se o detento não puder receber visita, exibir a mensagem e encerrar o programa
# Verificar se o detento pode receber visita
if "não pode receber visita" in resultado_verificacao:
    print(resultado_verificacao)
else:
    # Definindo os parâmetros necessários para agendar a visita
    detentos = dados_reus_inicial["reus"]
    horario = input("Digite o horário de visita (hh:mm): ")
    visitante = "Visitante Exemplo"
    duracao = "1 hora"
    instrucoes = "Instruções Exemplo"

    # Chamar a função para agendar a visita
    visita_agendada = agendar_visita(detentos, nome_do_reu, horario, visitante, duracao, instrucoes)
    print(visita_agendada)

    # ... (código original do sistema de agendamento de visitas) ...


def registrar_realizacao_visita(cpf_visitante, nome_presidiario, data_hora_visita):
    """
    Função para registrar a realização de uma visita.

    Args:
        cpf_visitante (str): CPF do visitante.
        nome_presidiario (str): Nome do presidiário.
        data_hora_visita (str): Data e hora da visita no formato 'YYYY-MM-DD HH:MM'.
    """

    registro_de_visitas = carregar_dados('dados_visitas.json')

    if cpf_visitante in registro_de_visitas:
        visita = registro_de_visitas[cpf_visitante]

        if nome_presidiario in visita["visitas"]:
            visita["visitas"][nome_presidiario]["realizada"] = True
            salvar_dados(registro_de_visitas, 'dados_visitas.json')
            print(f"Visita do visitante {visita['nome']} ao presidiário {nome_presidiario} em {data_hora_visita} marcada como realizada.")
        else:
            print(f"Visita ao presidiário {nome_presidiario} não encontrada para o visitante {visita['nome']}.")
    else:
        print(f"Visitante com CPF {cpf_visitante} não encontrado.")

# ... (código original do sistema de agendamento de visitas) ...


def gerar_relatorio_visitas(data_inicio, data_fim):
    """
    Função para gerar um relatório de visitas.

    Args:
        data_inicio (str): Data de início do período do relatório no formato 'YYYY-MM-DD'.
        data_fim (str): Data de fim do período do relatório no formato 'YYYY-MM-DD'.
    """

    registro_de_visitas = carregar_dados('dados_visitas.json')

    visitas_realizadas = 0
    visitas_agendadas = 0
    visitas_nao_realizadas = []

    for cpf_visitante, dados_visitante in registro_de_visitas.items():
        for nome_presidiario, dados_visita in dados_visitante["visitas"].items():
            data_hora_visita = dados_visita["data_hora"]

            if data_hora_visita >= data_inicio and data_hora_visita <= data_fim:
                visitas_agendadas += 1

            if dados_visita["realizada"]:
                visitas_realizadas += 1
            else:
                visitas_nao_realizadas.append({
                    # ... (completar dados da visita não realizada) ...
                })

    # ... (processamento e impressão do relatório) ...

# ... (código original do sistema de agendamento de visitas) ...


def registrar_realizacao_visita(cpf_visitante, nome_presidiario, data_hora_visita):
    """
    Função para registrar a realização de uma visita.

    Args:
        cpf_visitante (str): CPF do visitante.
        nome_presidiario (str): Nome do presidiário.
        data_hora_visita (str): Data e hora da visita no formato 'YYYY-MM-DD HH:MM'.
    """

    registro_de_visitas = carregar_dados('dados_visitas.json')

    if cpf_visitante in registro_de_visitas:
        visita = registro_de_visitas[cpf_visitante]

        if nome_presidiario in visita["visitas"]:
            visita["visitas"][nome_presidiario]["realizada"] = True
            salvar_dados(registro_de_visitas, 'dados_visitas.json')
            print(f"Visita do visitante {visita['nome']} ao presidiário {nome_presidiario} em {data_hora_visita} marcada como realizada.")
        else:
            print(f"Visita ao presidiário {nome_presidiario} não encontrada para o visitante {visita['nome']}.")
    else:
        print(f"Visitante com CPF {cpf_visitante} não encontrado.")

# ... (código original do sistema de agendamento de visitas) ...


def gerar_relatorio_visitas(data_inicio, data_fim):
    """
    Função para gerar um relatório de visitas.

    Args:
        data_inicio (str): Data de início do período do relatório no formato 'YYYY-MM-DD'.
        data_fim (str): Data de fim do período do relatório no formato 'YYYY-MM-DD'.
    """

    registro_de_visitas = carregar_dados('dados_visitas.json')

    visitas_realizadas = 0
    visitas_agendadas = 0
    visitas_nao_realizadas = []

    for cpf_visitante, dados_visitante in registro_de_visitas.items():
        for nome_presidiario, dados_visita in dados_visitante["visitas"].items():
            data_hora_visita = dados_visita["data_hora"]

            if data_hora_visita >= data_inicio and data_hora_visita <= data_fim:
                visitas_agendadas += 1

            if dados_visita["realizada"]:
                visitas_realizadas += 1
            else:
                visitas_nao_realizadas.append({
                    # ... (completar dados da visita não realizada) ...
                })

    # ... (processamento e impressão do relatório) ...
