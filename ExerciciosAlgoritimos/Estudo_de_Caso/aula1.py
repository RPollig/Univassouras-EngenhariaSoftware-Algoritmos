def soma(a,b): 
    return a+b

def subtracao(a,b):
    return a-b

def multiplicacao(a,b):
    return a*b

def divisao(a,b):
    return a/b

def testeAB():
    # global a
    # global b

    a = float(input("Insira o primeiro valor: "))
    b = float(input("Insira o segundo valor: ")) 
 
    if a > b:
        print("certo")
    else:
        while(a<b):
            print("deu erro")
            a = float(input("Insira o primeiro valor: "))
            b = float(input("Insira o segundo valor: "))
            # print(a,b)

    return a,b
                
resultado = testeAB()
# print(resultado)
resultado1 = soma(a,b)
resultado2 = subtracao(a,b)
resultado3 = multiplicacao(a,b)
resultado4 = divisao(a,b)

# print(resultado)
# print(f"{resultado1:.3f}")

print(resultado,f"{resultado1:.3f}, {resultado2:.3f}, {resultado3:.3f}, {resultado4:.3f}")

