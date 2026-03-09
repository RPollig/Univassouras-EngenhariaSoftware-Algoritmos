# 22. Conte o número de vogais em uma string.

palavra = input("Digite uma palavra: ")

vogais = 0  

for letras in palavra: 
    if letras in "aeiouAEIOU":
        vogais = vogais + 1

print("Qntidade de vogais: ",vogais)