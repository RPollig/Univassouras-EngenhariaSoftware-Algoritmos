# 23. Substitua espaços por hífens em uma frase.
frase = input("Digite uma frase: ")

nova_frase = ""

for letra in frase:
    if letra == " ":
        nova_frase = nova_frase + "-"
    else:
        nova_frase = nova_frase + letra

print(nova_frase)