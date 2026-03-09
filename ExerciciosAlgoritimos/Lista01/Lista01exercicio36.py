# 36. Utilize list comprehension para filtrar números pares.

lista = input("Digite números separados por espaço: ").split()

lista = [int(num) for num in lista]

pares = [num for num in lista if num % 2 == 0]

print("Números pares:", pares)