# 32. Crie uma função que verifique se um número é primo.

def primo(num):
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


numero = int(input("Digite um número: "))

if primo(numero):
    print("É primo")
else:
    print("Não é primo")