# 29. Crie um dicionário com nome e idade e exiba os dados.

nome = input("Digite o nome: ")
idade = input("Digite a idade: ")

pessoa = {
    "nome": nome,
    "idade": idade
}

print("Nome:", pessoa["nome"])
print("Idade:", pessoa["idade"])