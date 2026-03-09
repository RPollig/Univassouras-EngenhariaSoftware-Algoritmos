# 25. Ordene uma lista de números.

lista = input("Digite números separados por espaço: ").split()

lista = [int(num) for num in lista]

lista.sort()

print("Lista ordenada:", lista)