# 37. Leia um arquivo texto e conte o número de linhas.

arquivo = open("arquivo.txt", "r")

linhas = arquivo.readlines()

arquivo.close()

print("Número de linhas:", len(linhas))