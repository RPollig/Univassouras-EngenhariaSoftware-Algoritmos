# 19. Conte quantos números pares existem entre 1 e 50.

# 19. Conte quantos números pares existem entre 1 e 50

contador = 0

for i in range(1, 51):
    if i % 2 == 0:
        contador = contador + 1

print("Quantidade de números pares:", contador)
