# 14. Calcule o fatorial de um número. Obs.: Não entendi!
# 14. Calcule o fatorial de um número.

n = int(input("Digite um número: "))

fatorial = 1

for i in range(1, n + 1):
    fatorial = fatorial * i

print("O fatorial de", n, "é:", fatorial)