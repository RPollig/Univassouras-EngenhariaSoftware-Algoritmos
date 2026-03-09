# 28. Conte quantas vezes um número aparece em uma lista.

lista = input("Digite números separados por espaço: ").split()

lista = [int(num) for num in lista]

numero = int(input("Digite o número que deseja contar: "))

contador = 0

for num in lista:
    if num == numero:
        contador = contador + 1

print("O número aparece", contador, "vezes")