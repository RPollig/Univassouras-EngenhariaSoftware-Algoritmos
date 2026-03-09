# 26. Remova elementos duplicados de uma lista.

lista = input("Digite números separados por espaço: ").split()

lista = [int(num) for num in lista]

nova_lista = []

for num in lista:
    if num not in nova_lista:
        nova_lista.append(num)

print("Lista sem duplicados:", nova_lista)