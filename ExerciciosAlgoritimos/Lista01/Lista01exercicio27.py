# 27. Some todos os elementos de uma lista.

lista = input("Digite números separados por espaço: ").split()

lista = [int(num) for num in lista]

soma = 0

for num in lista:
    soma = soma + num

print("Soma:", soma)