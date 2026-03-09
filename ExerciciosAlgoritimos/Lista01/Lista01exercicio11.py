# 11. Faça um programa que calcule o IMC.
print("Vamos calcular seu IMC!")
p = float(input("Qual o seu peso: "))
a = float(input("Qual sua altura: "))
imc = p / (a * a)
print(f"Então seu IMC é: {imc:.2f}")