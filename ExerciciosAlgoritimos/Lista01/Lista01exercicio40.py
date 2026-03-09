# 40. Trate erro de divisão por zero.

try:
    n1 = int(input("Digite o primeiro número: "))
    n2 = int(input("Digite o segundo número: "))

    resultado = n1 / n2

    print("Resultado:", resultado)

except ZeroDivisionError:
    print("Erro: divisão por zero não é permitida.")