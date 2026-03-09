# 6. Leia um número e mostre sua tabuada.
n = int(input("Digite um numero para eu informar toda sua tabeada:" ))
for i in range(1,11):
    print(n, "x", i, "=", n * i)