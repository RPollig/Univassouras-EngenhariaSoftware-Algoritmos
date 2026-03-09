# 33. Use uma função para calcular a área de um círculo.

import math

def area_circulo(raio):
    return math.pi * raio ** 2

raio = float(input("Digite o raio: "))

area = area_circulo(raio)

print("Área:", area)