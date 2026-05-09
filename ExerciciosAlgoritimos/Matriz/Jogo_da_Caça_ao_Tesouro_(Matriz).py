# Exercício 1: Jogo da Caça ao Tesouro (Matriz)
# Descrição
# Você deve criar um jogo onde o jogador tenta encontrar um tesouro escondido em uma matriz
# 5x5.
# • A matriz representa um mapa
# • O tesouro está escondido em uma posição aleatória
# • O jogador informa linha e coluna para tentar encontrar
# • O jogo mostra dicas:
# o "Muito perto" (distância 1)
# o "Perto" (distância 2 ou 3)
# o "Longe" (distância maior)
# • O jogo termina quando o jogador encontra o tesouro
# Regras
# • Usar matriz (lista de listas)
# • Usar loop (while)
# • Usar entrada do usuário (input)
# • Contar número de tentativas

import random # importa a biblioteca random para sortear números

mapa = [] # cria uma lista vazia que vai virar a matriz do mapa

for i in range(5): # repete 5 vezes para criar as linhas
    linha = [] # cria uma linha vazia
    for j in range(5): # repete 5 vezes para criar as colunas
        linha.append("-") # coloca o traço em cada posição do mapa
    mapa.append(linha) # adiciona a linha dentro do mapa

tesouro_linha = random.randint(0, 4) # sorteia a linha do tesouro entre 0 e 4
tesouro_coluna = random.randint(0, 4) # sorteia a coluna do tesouro entre 0 e 4

tentativas = 0 # começa contando as tentativas do jogador

while True: # repete até o jogador encontrar o tesouro
    print("MAPA DO JOGO:") # mostra o título do mapa

    for linha in mapa: # passa por cada linha do mapa
        print(linha) # mostra a linha na tela

    linha_jogador = int(input("Digite a linha de 0 a 4: ")) # pede a linha para o jogador
    coluna_jogador = int(input("Digite a coluna de 0 a 4: ")) # pede a coluna para o jogador

    tentativas = tentativas + 1 # soma mais uma tentativa

    if linha_jogador < 0 or linha_jogador > 4 or coluna_jogador < 0 or coluna_jogador > 4: # verifica se saiu do mapa
        print("Posição inválida") # avisa que a posição está errada
    elif linha_jogador == tesouro_linha and coluna_jogador == tesouro_coluna: # verifica se achou o tesouro
        mapa[linha_jogador][coluna_jogador] = "X" # marca o tesouro encontrado no mapa
        print("Você encontrou o tesouro!") # mensagem de vitória
        print("Quantidade de tentativas:", tentativas) # mostra quantas tentativas usou
        break # encerra o jogo
    else: # se não encontrou o tesouro
        mapa[linha_jogador][coluna_jogador] = "O" # marca a tentativa do jogador no mapa

        distancia_linha = abs(linha_jogador - tesouro_linha) # calcula a distância da linha
        distancia_coluna = abs(coluna_jogador - tesouro_coluna) # calcula a distância da coluna
        distancia = distancia_linha + distancia_coluna # soma as distâncias para dar uma dica simples

        if distancia == 1: # se estiver a 1 casa de distância
            print("Muito perto") # mostra dica muito perto
        elif distancia == 2 or distancia == 3: # se estiver a 2 ou 3 casas
            print("Perto") # mostra dica perto
        else: # se estiver mais longe
            print("Longe") # mostra dica longe