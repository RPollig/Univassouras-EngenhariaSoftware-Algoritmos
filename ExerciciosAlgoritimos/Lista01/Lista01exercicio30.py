# 30. Atualize um valor dentro de um dicionário.

pessoa = {
    "nome": "João",
    "idade": 20
}

nova_idade = int(input("Digite a nova idade: "))

pessoa["idade"] = nova_idade

print(pessoa)