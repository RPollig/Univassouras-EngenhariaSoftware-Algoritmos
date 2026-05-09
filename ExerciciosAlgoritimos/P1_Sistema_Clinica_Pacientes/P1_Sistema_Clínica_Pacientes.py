# Questão 01

pacientes = [] # paciente é uma lista vazia

# Questão 02 e 07

def adicionar_paciente(): # função chamada adicionar_paciente
    nome = input("Digite o nome do paciente: ") # pedindo o nome do paciente e guardando na variável nome

    while True: # fica repetindo até agente mandar parar
        try: # tenta executar o bloco abaixo
            idade = int(input("Digite a idade: ")) # pede a idade e converte para inteiro
        except ValueError: # se o usuario digitar letra, apresenta erro
            print("Digite apenas números") # apresenta esta mensagem para digitar a numeração valida 
            continue
        if idade >= 0 and idade <= 120: # corrigido aqui
            break # pare
        else: # se não 
            print("Idade inválida")  # apresenta esse erro 
    while True: # fica repetindo até agente mandar parar
        try: # tenta executar o bloco abaixo
            quantidade_de_consultas = int(input("Quantidade de consultas deseja registar: ")) # a variavel quantidade é um numero 
        except ValueError: # se digitar letra, apresenta erro
            print("Digite apenas números") # mensagem para o usuario
            continue
        if quantidade_de_consultas >= 1 and quantidade_de_consultas <= 4: # corrigido aqui + :
            break # para o loop
        else: # se não
            print("Quantidade invalida") # avisa que a quantidade é invalida.
    consultas = [] # lista para guardar os valores das consultas
    for i in range(quantidade_de_consultas): # repete conforme a quantidade de consultas
        while True: # repete até digitar um valor certo
            try: # tenta executar
                valor = float(input("Digite o valor da consulta: ")) # pede o valor da consulta
                if valor >= 50 and valor <= 1500: # verifica se o valor está entre 50 e 1500
                    consultas.append(valor) # adiciona o valor na lista
                    break # para o while
                else: # se o valor estiver errado
                    print("Valor inválido") # mostra mensagem de erro
            except ValueError: # se digitar letra no lugar de número
                print("Digite apenas números") # avisa o erro
    media_gastos = sum(consultas) / len(consultas) # calcula a média das consultas
    paciente = { # cria o dicionário do paciente
        "nome": nome, # guarda o nome
        "idade": idade, # guarda a idade
        "consultas": consultas, # guarda a lista de consultas
        "media_gastos": media_gastos # guarda a média
    }
    pacientes.append(paciente) # adiciona o paciente na lista principal
    print("Paciente cadastrado com sucesso") # mostra que cadastrou

# Questão 03

def listar_pacientes(): # função para listar os pacientes
    if len(pacientes) == 0: # verifica se a lista está vazia
        print("Nenhum paciente cadastrado") # avisa que não tem paciente
    else: # se tiver paciente
        for paciente in pacientes: # passa por cada paciente da lista
            print(f"Nome: {paciente['nome']} | Idade: {paciente['idade']} | Média de Gastos: R$ {paciente['media_gastos']:.2f}") # mostra os dados


# Questão 04

def ordenar_pacientes(): # função para ordenar pacientes
    pacientes.sort(key=lambda paciente: paciente["media_gastos"], reverse=True) # ordena pela média maior primeiro
    listar_pacientes() # mostra a lista ordenada


# Questão 05

def salvar_em_arquivo(): # função para salvar no arquivo
    arquivo = open("pacientes.txt", "w") # abre o arquivo para escrever
    for paciente in pacientes: # passa por cada paciente
        arquivo.write(f"{paciente['nome']};{paciente['idade']};{paciente['consultas']};{paciente['media_gastos']}\n") # escreve no arquivo
    arquivo.close() # fecha o arquivo
    print("Dados salvos") # avisa que salvou


# Questão 06

def carregar_pacientes(): # função para carregar do arquivo
    try: # tenta abrir o arquivo
        arquivo = open("pacientes.txt", "r") # abre o arquivo para leitura
        for linha in arquivo: # lê cada linha do arquivo
            dados = linha.strip().split(";") # separa os dados pelo ponto e vírgula
            paciente = { # cria o dicionário do paciente
                "nome": dados[0], # pega o nome
                "idade": int(dados[1]), # pega a idade
                "consultas": [], # deixa a lista de consultas vazia
                "media_gastos": float(dados[3]) # pega a média
            }
            pacientes.append(paciente) # adiciona na lista
        arquivo.close() # fecha o arquivo
        print("Dados carregados") # avisa que carregou
    except FileNotFoundError: # se o arquivo não existir
        print("Arquivo não encontrado") # mostra erro


# Questão 08 e 09

while True: # loop do menu
    print("1 - Adicionar paciente") # opção 1
    print("2 - Listar pacientes") # opção 2
    print("3 - Ordenar pacientes por gastos") # opção 3
    print("4 - Salvar dados") # opção 4
    print("5 - Carregar dados") # opção 5
    print("6 - Sair") # opção 6
    opcao = input("Escolha uma opção: ") # pede a opção

    if opcao == "1": # se escolher 1
        adicionar_paciente() # chama a função adicionar
    elif opcao == "2": # se escolher 2
        listar_pacientes() # chama a função listar
    elif opcao == "3": # se escolher 3
        ordenar_pacientes() # chama a função ordenar
    elif opcao == "4": # se escolher 4
        salvar_em_arquivo() # chama a função salvar
    elif opcao == "5": # se escolher 5
        carregar_pacientes() # chama a função carregar
    elif opcao == "6": # se escolher 6
        resposta = input("Deseja salvar antes de sair? S/N: ") # pergunta se quer salvar
        if resposta == "S" or resposta == "s": # se responder sim
            salvar_em_arquivo() # salva antes de sair
        print("Programa encerrado") # mostra mensagem final
        break # encerra o loop
    else: # se digitar opção errada
        print("Opção inválida") # avisa que está errado