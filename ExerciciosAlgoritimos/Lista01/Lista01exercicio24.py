# 24. Leia uma lista de números e mostre o maior e o menor.

lista = input("Digite números separados por espaço: ").split()

lista = [int(num) for num in lista]

maior = lista[0]
menor = lista[0]

for num in lista:
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print("Maior:", maior)
print("Menor:", menor)