# 15. Gere os 10 primeiros números da sequência de Fibonacci. Obs.: Não entendi!
# 15. Gere os 10 primeiros números da sequência de Fibonacci.

a = 0
b = 1

for i in range(10):
    print(a)

    proximo = a + b
    a = b
    b = proximo 

    # https://www.youtube.com/watch?v=CPm9jyw5zKk
    # N + 1 = N + N-1
    anterior = 0
    atual = 1       
    for i in range(10):
        print(anterior)
        proximo = anterior + atual
        anterior = atual
        atual = proximo