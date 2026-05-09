import random # usado para gerar números aleatórios para os testes
import time # usado para medir quanto tempo cada algoritmo demora


# ------------------------------------------------------------
# FUNÇÃO PARA VERIFICAR SE A LISTA FICOU ORDENADA
# ------------------------------------------------------------

def verificar_ordenada(lista): # verifica se a lista está realmente em ordem crescente
    for i in range(len(lista) - 1): # percorre a lista até o penúltimo elemento
        if lista[i] > lista[i + 1]: # se um número atual for maior que o próximo, a lista não está ordenada
            return False # retorna falso porque encontrou erro na ordenação
    return True # retorna verdadeiro se não encontrou nenhum erro


# ------------------------------------------------------------
# 1 - SELECTION SORT
# ------------------------------------------------------------

def selection_sort(lista): # ordena procurando o menor elemento e colocando no começo
    n = len(lista) # guarda o tamanho da lista para controlar os laços

    for i in range(n): # percorre cada posição da lista
        menor = i # considera que a posição atual tem o menor valor

        for j in range(i + 1, n): # procura um valor menor no restante da lista
            if lista[j] < lista[menor]: # compara o valor atual com o menor encontrado
                menor = j # atualiza a posição do menor valor

        lista[i], lista[menor] = lista[menor], lista[i] # troca o menor valor encontrado com a posição atual

    return lista # retorna a lista ordenada


# ------------------------------------------------------------
# 2 - BUBBLE SORT
# ------------------------------------------------------------

def bubble_sort(lista): # ordena comparando pares vizinhos e empurrando os maiores para o final
    n = len(lista) # guarda o tamanho da lista

    for i in range(n): # controla quantas passagens serão feitas pela lista
        for j in range(0, n - i - 1): # percorre a parte ainda não ordenada
            if lista[j] > lista[j + 1]: # se o valor da esquerda for maior que o da direita, está fora de ordem
                lista[j], lista[j + 1] = lista[j + 1], lista[j] # troca os dois valores de posição

    return lista # retorna a lista ordenada


# ------------------------------------------------------------
# 3 - INSERTION SORT
# ------------------------------------------------------------

def insertion_sort(lista): # ordena como se estivesse organizando cartas na mão
    for i in range(1, len(lista)): # começa da segunda posição, pois a primeira já é considerada ordenada
        chave = lista[i] # guarda o valor que será encaixado na parte ordenada
        j = i - 1 # começa comparando com o valor anterior

        while j >= 0 and lista[j] > chave: # enquanto o valor anterior for maior, ele precisa andar para a direita
            lista[j + 1] = lista[j] # desloca o valor maior uma posição para frente
            j = j - 1 # volta uma posição para continuar comparando

        lista[j + 1] = chave # coloca a chave na posição correta

    return lista # retorna a lista ordenada


# ------------------------------------------------------------
# 4 - MERGE SORT
# ------------------------------------------------------------

def merge_sort(lista): # divide a lista em partes menores e depois junta tudo ordenado
    if len(lista) <= 1: # se a lista tem zero ou um elemento, ela já está ordenada
        return lista # retorna a própria lista

    meio = len(lista) // 2 # encontra o meio da lista
    esquerda = merge_sort(lista[:meio]) # ordena recursivamente a metade esquerda
    direita = merge_sort(lista[meio:]) # ordena recursivamente a metade direita

    resultado = [] # lista que vai receber os valores já ordenados
    i = 0 # índice da lista esquerda
    j = 0 # índice da lista direita

    while i < len(esquerda) and j < len(direita): # compara enquanto ainda existirem valores nas duas metades
        if esquerda[i] <= direita[j]: # se o valor da esquerda for menor ou igual
            resultado.append(esquerda[i]) # adiciona o valor da esquerda no resultado
            i = i + 1 # avança na esquerda
        else: # se o valor da direita for menor
            resultado.append(direita[j]) # adiciona o valor da direita no resultado
            j = j + 1 # avança na direita

    resultado = resultado + esquerda[i:] # adiciona o que sobrou da esquerda
    resultado = resultado + direita[j:] # adiciona o que sobrou da direita

    return resultado # retorna a lista ordenada


# ------------------------------------------------------------
# 5 - QUICK SORT
# ------------------------------------------------------------

def quick_sort(lista): # ordena escolhendo um pivô e separando menores e maiores
    if len(lista) <= 1: # se a lista tem zero ou um elemento, já está ordenada
        return lista # retorna a própria lista

    pivo = lista[len(lista) // 2] # escolhe o elemento do meio como pivô

    menores = [] # guarda valores menores que o pivô
    iguais = [] # guarda valores iguais ao pivô
    maiores = [] # guarda valores maiores que o pivô

    for valor in lista: # percorre todos os valores da lista
        if valor < pivo: # se o valor for menor que o pivô
            menores.append(valor) # adiciona na lista de menores
        elif valor == pivo: # se o valor for igual ao pivô
            iguais.append(valor) # adiciona na lista de iguais
        else: # se o valor for maior que o pivô
            maiores.append(valor) # adiciona na lista de maiores

    return quick_sort(menores) + iguais + quick_sort(maiores) # junta menores ordenados, iguais e maiores ordenados


# ------------------------------------------------------------
# 6 - HEAP SORT
# ------------------------------------------------------------

def ajustar_heap(lista, tamanho, raiz): # organiza uma parte da lista como estrutura de heap
    maior = raiz # considera a raiz como maior valor
    esquerda = 2 * raiz + 1 # calcula a posição do filho da esquerda
    direita = 2 * raiz + 2 # calcula a posição do filho da direita

    if esquerda < tamanho and lista[esquerda] > lista[maior]: # verifica se o filho da esquerda é maior
        maior = esquerda # atualiza a posição do maior

    if direita < tamanho and lista[direita] > lista[maior]: # verifica se o filho da direita é maior
        maior = direita # atualiza a posição do maior

    if maior != raiz: # se o maior não for a raiz, precisa trocar
        lista[raiz], lista[maior] = lista[maior], lista[raiz] # coloca o maior valor na raiz
        ajustar_heap(lista, tamanho, maior) # ajusta novamente a parte afetada


def heap_sort(lista): # ordena usando a ideia de árvore heap
    n = len(lista) # guarda o tamanho da lista

    for i in range(n // 2 - 1, -1, -1): # começa montando o heap a partir do meio da lista
        ajustar_heap(lista, n, i) # organiza a lista para manter o maior valor no topo

    for i in range(n - 1, 0, -1): # retira o maior valor e coloca no final
        lista[i], lista[0] = lista[0], lista[i] # troca o primeiro valor com o último da parte não ordenada
        ajustar_heap(lista, i, 0) # reorganiza o heap reduzido

    return lista # retorna a lista ordenada


# ------------------------------------------------------------
# 7 - COUNTING SORT
# ------------------------------------------------------------

def counting_sort(lista): # ordena contando quantas vezes cada número aparece
    if len(lista) == 0: # se a lista estiver vazia
        return lista # retorna a própria lista

    menor = min(lista) # encontra o menor valor da lista
    maior = max(lista) # encontra o maior valor da lista

    contagem = [0] * (maior - menor + 1) # cria uma lista para contar as ocorrências de cada número

    for valor in lista: # percorre todos os valores
        contagem[valor - menor] = contagem[valor - menor] + 1 # soma uma ocorrência daquele valor

    resultado = [] # lista que vai receber os valores ordenados

    for i in range(len(contagem)): # percorre a lista de contagem
        quantidade = contagem[i] # pega quantas vezes aquele número apareceu
        valor_original = i + menor # transforma o índice de volta no valor original

        for j in range(quantidade): # repete conforme a quantidade de ocorrências
            resultado.append(valor_original) # adiciona o valor na lista final

    return resultado # retorna a lista ordenada


# ------------------------------------------------------------
# 8 - RADIX SORT
# ------------------------------------------------------------

def counting_sort_por_digito(lista, casa): # ordena os números olhando uma casa decimal por vez
    tamanho = len(lista) # guarda o tamanho da lista
    resultado = [0] * tamanho # cria uma lista do mesmo tamanho para guardar o resultado
    contagem = [0] * 10 # cria contagem para dígitos de 0 até 9

    for valor in lista: # percorre os valores da lista
        digito = (valor // casa) % 10 # pega o dígito da casa atual
        contagem[digito] = contagem[digito] + 1 # conta quantas vezes esse dígito aparece

    for i in range(1, 10): # percorre a contagem a partir do segundo dígito
        contagem[i] = contagem[i] + contagem[i - 1] # acumula as posições para montar a ordenação

    i = tamanho - 1 # começa do final para manter a ordem dos elementos iguais
    while i >= 0: # percorre a lista de trás para frente
        valor = lista[i] # pega o valor atual
        digito = (valor // casa) % 10 # pega o dígito da casa atual
        resultado[contagem[digito] - 1] = valor # coloca o valor na posição correta
        contagem[digito] = contagem[digito] - 1 # reduz a posição disponível daquele dígito
        i = i - 1 # anda para o elemento anterior

    for i in range(tamanho): # copia o resultado para a lista original
        lista[i] = resultado[i] # atualiza cada posição da lista


def radix_sort(lista): # ordena números inteiros olhando unidade, dezena, centena e assim por diante
    if len(lista) == 0: # se a lista estiver vazia
        return lista # retorna a própria lista

    maior = max(lista) # encontra o maior número para saber quantas casas decimais serão usadas
    casa = 1 # começa pela unidade

    while maior // casa > 0: # continua enquanto ainda existir casa decimal para analisar
        counting_sort_por_digito(lista, casa) # ordena pela casa decimal atual
        casa = casa * 10 # passa para dezena, centena, milhar e assim por diante

    return lista # retorna a lista ordenada


# ------------------------------------------------------------
# 9 - BUCKET SORT
# ------------------------------------------------------------

def bucket_sort(lista): # ordena distribuindo os valores em baldes
    if len(lista) == 0: # se a lista estiver vazia
        return lista # retorna a própria lista

    menor = min(lista) # encontra o menor valor
    maior = max(lista) # encontra o maior valor
    quantidade_baldes = 10 # define a quantidade de baldes usados na separação

    baldes = [] # lista principal dos baldes

    for i in range(quantidade_baldes): # cria os baldes vazios
        baldes.append([]) # adiciona um balde vazio

    for valor in lista: # percorre todos os valores da lista
        if maior == menor: # evita divisão por zero se todos os valores forem iguais
            indice = 0 # coloca tudo no primeiro balde
        else: # caso normal
            indice = int((valor - menor) / (maior - menor) * (quantidade_baldes - 1)) # calcula em qual balde o valor deve entrar

        baldes[indice].append(valor) # adiciona o valor no balde calculado

    resultado = [] # lista final ordenada

    for balde in baldes: # percorre cada balde
        insertion_sort(balde) # ordena cada balde com insertion sort, pois os baldes ficam menores
        resultado = resultado + balde # junta o balde ordenado no resultado final

    return resultado # retorna a lista ordenada


# ------------------------------------------------------------
# FUNÇÃO PARA TESTAR CADA ALGORITMO
# ------------------------------------------------------------

def testar_algoritmo(nome, funcao, lista_teste): # recebe o nome do algoritmo, a função e a lista que será testada
    copia = lista_teste.copy() # cria uma cópia para não alterar a lista original usada nos outros testes

    inicio = time.time() # marca o horário inicial
    resultado = funcao(copia) # executa o algoritmo de ordenação
    fim = time.time() # marca o horário final

    tempo = fim - inicio # calcula o tempo gasto
    ordenada = verificar_ordenada(resultado) # verifica se a lista realmente ficou ordenada

    print("--------------------------------------------") # separador visual
    print("Algoritmo:", nome) # mostra o nome do algoritmo testado
    print("Quantidade de elementos:", len(lista_teste)) # mostra o tamanho da lista usada
    print("Tempo gasto:", round(tempo, 4), "segundos") # mostra o tempo aproximado
    print("Lista ordenada corretamente:", ordenada) # mostra se o resultado ficou certo


# ------------------------------------------------------------
# RESUMO PARA APRESENTAÇÃO
# ------------------------------------------------------------

def mostrar_vantagens_desvantagens(): # mostra um resumo útil para explicar os algoritmos
    print("\nRESUMO DOS ALGORITMOS") # título do resumo

    print("\nSelection Sort") # nome do algoritmo
    print("Vantagem: simples de entender e implementar.") # ponto positivo
    print("Desvantagem: lento para listas grandes, pois faz muitas comparações.") # ponto negativo

    print("\nBubble Sort") # nome do algoritmo
    print("Vantagem: fácil de visualizar, pois compara elementos vizinhos.") # ponto positivo
    print("Desvantagem: muito ineficiente para grandes quantidades de dados.") # ponto negativo

    print("\nInsertion Sort") # nome do algoritmo
    print("Vantagem: bom para listas pequenas ou quase ordenadas.") # ponto positivo
    print("Desvantagem: fica lento quando a lista é grande e muito desorganizada.") # ponto negativo

    print("\nMerge Sort") # nome do algoritmo
    print("Vantagem: eficiente para listas grandes e tem bom desempenho constante.") # ponto positivo
    print("Desvantagem: usa mais memória, pois divide e cria novas listas.") # ponto negativo

    print("\nQuick Sort") # nome do algoritmo
    print("Vantagem: geralmente é muito rápido na prática.") # ponto positivo
    print("Desvantagem: pode piorar dependendo da escolha do pivô.") # ponto negativo

    print("\nHeap Sort") # nome do algoritmo
    print("Vantagem: tem bom desempenho e não depende de lista auxiliar grande.") # ponto positivo
    print("Desvantagem: é mais difícil de entender por usar a ideia de heap.") # ponto negativo

    print("\nCounting Sort") # nome do algoritmo
    print("Vantagem: muito rápido quando os números estão em um intervalo conhecido.") # ponto positivo
    print("Desvantagem: não é ideal quando o intervalo dos valores é muito grande.") # ponto negativo

    print("\nRadix Sort") # nome do algoritmo
    print("Vantagem: eficiente para ordenar números inteiros com várias casas decimais.") # ponto positivo
    print("Desvantagem: funciona melhor em números inteiros não negativos.") # ponto negativo

    print("\nBucket Sort") # nome do algoritmo
    print("Vantagem: pode ser rápido quando os dados estão bem distribuídos.") # ponto positivo
    print("Desvantagem: perde eficiência se muitos valores caírem no mesmo balde.") # ponto negativo


# ------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------

print("TRABALHO DE ALGORITMOS DE ORDENAÇÃO") # título do programa
print("Criando lista com 100.000 elementos aleatórios...") # avisa que a lista grande será criada

lista_grande = [] # lista principal pedida no trabalho

for i in range(100000): # repete 100.000 vezes para gerar os elementos
    numero = random.randint(0, 999999) # gera um número aleatório entre 0 e 999.999
    lista_grande.append(numero) # adiciona o número na lista grande

lista_pequena = lista_grande[:2000] # cria uma lista menor para testar algoritmos lentos sem travar o computador

print("Lista grande criada com", len(lista_grande), "elementos.") # confirma a criação da lista grande
print("Lista menor criada com", len(lista_pequena), "elementos para os algoritmos mais lentos.") # explica o uso da lista menor

print("\nOBSERVAÇÃO IMPORTANTE") # título da observação
print("Selection Sort, Bubble Sort e Insertion Sort são simples, mas ficam muito lentos com 100.000 elementos.") # explica a limitação prática
print("Por isso, eles serão demonstrados com 2.000 elementos, para evitar travamento e mostrar a diferença de desempenho.") # justifica a escolha
print("Os algoritmos mais eficientes serão testados com a lista completa de 100.000 elementos.") # explica os testes maiores

testar_algoritmo("Selection Sort", selection_sort, lista_pequena) # testa Selection Sort com lista menor
testar_algoritmo("Bubble Sort", bubble_sort, lista_pequena) # testa Bubble Sort com lista menor
testar_algoritmo("Insertion Sort", insertion_sort, lista_pequena) # testa Insertion Sort com lista menor

testar_algoritmo("Merge Sort", merge_sort, lista_grande) # testa Merge Sort com lista grande
testar_algoritmo("Quick Sort", quick_sort, lista_grande) # testa Quick Sort com lista grande
testar_algoritmo("Heap Sort", heap_sort, lista_grande) # testa Heap Sort com lista grande
testar_algoritmo("Counting Sort", counting_sort, lista_grande) # testa Counting Sort com lista grande
testar_algoritmo("Radix Sort", radix_sort, lista_grande) # testa Radix Sort com lista grande
testar_algoritmo("Bucket Sort", bucket_sort, lista_grande) # testa Bucket Sort com lista grande

mostrar_vantagens_desvantagens() # mostra o resumo para ajudar na apresentação

print("\nFim dos testes.") # mensagem final