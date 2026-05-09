# Exercício 2: Simulação dos Movimentos do Cavalo em um Tabuleiro
# Contextualização
# No jogo de xadrez, o cavalo possui um movimento único em formato de “L”, podendo saltar
# sobre outras peças. Esse movimento consiste em:
# • 2 casas em uma direção (horizontal ou vertical)
# •
# o 1 casa em direção perpendicular
# Exemplo: de uma posição (linha, coluna), o cavalo pode ir para posições como (linha ±2, coluna
# ±1) ou (linha ±1, coluna ±2).
# Objetivo
# Desenvolver um programa em Python que simule os movimentos possíveis de um cavalo em um
# tabuleiro de xadrez representado por uma matriz 8x8.
# Requisitos
# O programa deve:
# • Criar uma matriz 8x8 para representar o tabuleiro
# • Solicitar ao usuário a posição inicial do cavalo (linha e coluna entre 0 e 7)
# • Posicionar o cavalo na matriz usando o caractere C
# • Calcular todos os movimentos válidos do cavalo a partir da posição informada
# • Marcar na matriz com * todas as posições possíveis de movimento
# • Preencher as demais posições com .
# • Exibir o tabuleiro final no console
# Regras importantes
# • O programa deve validar se os movimentos permanecem dentro dos limites da matriz
# • Não considerar posições fora do tabuleiro
# • O cavalo não pode sair da matriz 

tabuleiro = [] # cria uma lista vazia para guardar o tabuleiro

for i in range(8): # repete 8 vezes para criar as linhas
    linha = [] # cria uma linha vazia
    for j in range(8): # repete 8 vezes para criar as colunas
        linha.append(".") # coloca ponto em cada posição do tabuleiro
    tabuleiro.append(linha) # adiciona a linha dentro do tabuleiro

linha_cavalo = int(input("Digite a linha do cavalo de 0 a 7: ")) # pede a linha inicial do cavalo
coluna_cavalo = int(input("Digite a coluna do cavalo de 0 a 7: ")) # pede a coluna inicial do cavalo

if linha_cavalo < 0 or linha_cavalo > 7 or coluna_cavalo < 0 or coluna_cavalo > 7: # verifica se a posição é inválida
    print("Posição inválida") # mostra erro se estiver fora do tabuleiro
else: # se a posição estiver correta
    tabuleiro[linha_cavalo][coluna_cavalo] = "C" # coloca o cavalo na posição digitada

    movimentos = [ # lista com todos os movimentos possíveis do cavalo
        [-2, -1], # sobe 2 e vai 1 para esquerda
        [-2, 1], # sobe 2 e vai 1 para direita
        [-1, -2], # sobe 1 e vai 2 para esquerda
        [-1, 2], # sobe 1 e vai 2 para direita
        [1, -2], # desce 1 e vai 2 para esquerda
        [1, 2], # desce 1 e vai 2 para direita
        [2, -1], # desce 2 e vai 1 para esquerda
        [2, 1] # desce 2 e vai 1 para direita
    ]

    for movimento in movimentos: # passa por cada movimento da lista
        nova_linha = linha_cavalo + movimento[0] # calcula a nova linha
        nova_coluna = coluna_cavalo + movimento[1] # calcula a nova coluna

        if nova_linha >= 0 and nova_linha <= 7 and nova_coluna >= 0 and nova_coluna <= 7: # verifica se ficou dentro do tabuleiro
            tabuleiro[nova_linha][nova_coluna] = "*" # marca com estrela o movimento possível

    print("TABULEIRO FINAL:") # mostra o título

    for linha in tabuleiro: # passa por cada linha do tabuleiro
        print(linha) # imprime a linha