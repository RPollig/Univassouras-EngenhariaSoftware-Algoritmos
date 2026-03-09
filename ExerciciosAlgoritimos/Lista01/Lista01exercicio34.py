# 34. Crie uma função recursiva para calcular o fatorial.

def fatorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

numero = int(input("Digite um número: "))

print("Fatorial:", fatorial(numero))