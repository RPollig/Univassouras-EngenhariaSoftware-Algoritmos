# 38. Escreva dados em um arquivo texto.

arquivo = open("arquivo.txt", "w")

texto = input("Digite algo para salvar no arquivo: ")

arquivo.write(texto)

arquivo.close()

print("Dados salvos no arquivo.")