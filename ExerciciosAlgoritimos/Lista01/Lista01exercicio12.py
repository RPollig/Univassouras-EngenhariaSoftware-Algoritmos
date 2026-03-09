# 12. Leia três números e mostre o maior deles.
print("Vou te mostrar qual o maior número dos três que você digitar")
a = int(input("Primeiro número: "))
b = int(input("Segundo número: "))
c = int(input("Terceiro número: "))

if a > b and a > c:
    print(a,"é maior")

elif b > a and b > c:
    print(b,"é o maior")

else:
    print(c,"é o maior")