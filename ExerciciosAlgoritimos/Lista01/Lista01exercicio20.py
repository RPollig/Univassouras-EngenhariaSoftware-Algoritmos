# 20. Inverta um número inteiro (ex: 123 -> 321). Obs.: Estudar mais
numero = int(input("Digite um número inteiro: "))

invertido = 0

while numero > 0:
    digito = numero % 10
    invertido = invertido * 10 + digito
    numero = numero // 10

print("Número invertido:", invertido)
