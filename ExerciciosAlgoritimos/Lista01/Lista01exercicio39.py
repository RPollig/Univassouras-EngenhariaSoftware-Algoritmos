# 39. Crie um menu interativo simples usando while.

opcao = 0

while opcao != 3:

    print("1 - Olá")
    print("2 - Data")
    print("3 - Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        print("Olá!")

    elif opcao == 2:
        print("Hoje é um bom dia!")

print("Programa encerrado")