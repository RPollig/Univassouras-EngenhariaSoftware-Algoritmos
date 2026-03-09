# 17. Some todos os números de 1 até N.
# 17. Some todos os números de 1 até N

n = int(input("Digite um número: "))

soma = 0

for i in range(1, n + 1):
    soma = soma + i

print("A soma é:", soma)