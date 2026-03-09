EXERCÍCIO 1
1. Crie uma lista chamada frutas com "maçã", "banana", "laranja". Imprima o segundo item.
2. Adicione "uva" no final da lista frutas e depois remova "banana". Imprima a lista.
3. Crie uma lista vazia numeros. Usando um loop for, adicione os números de 1 a 10. Imprima o
tamanho da lista.
4. Verifique se o número 7 está na lista numeros e imprima "Sim" ou "Não".
5. Use slicing para imprimir apenas os 3 primeiros itens da lista numeros.
6. Ordene a lista notas = [8.5, 7.0, 9.5, 6.0] do maior para o menor.
7. Conte quantas vezes o número 5 aparece na lista numeros.
8. Inverta a lista numeros sem usar o método reverse().
9. Crie uma nova lista com os quadrados dos números de 1 a 8 usando list comprehension.
10. Dada palavras = ["python", "lista", "exercicio", "legal"], crie uma nova lista só com palavras
que têm 5 letras ou mais.
11. Junte as listas a = [1, 2, 3] e b = [4, 5, 6] em uma única lista.
12. Remova todos os números duplicados da lista [1, 2, 2, 3, 4, 4, 5] mantendo a ordem original.
13. Escreva uma função que recebe uma lista e retorna o maior e o menor valor.
14. Crie uma matriz 2x3 (lista de listas) e imprima o elemento da linha 1, coluna 2.
15. Faça uma cópia profunda de matriz = [[1,2],[3,4]], altere um valor na cópia e prove que a
original não mudou (use copy).
16. Usando list comprehension, crie uma lista só com números pares entre 0 e 20.
17. Escreva uma função que recebe duas listas e retorna True se elas tiverem os mesmos
elementos (mesma quantidade e valores, sem considerar ordem).
18. Crie uma lista de 10 números aleatórios (use random) e depois ordene apenas os números
pares dessa lista.
19. Remova da lista numeros todos os números menores que 5 sem criar uma nova lista.
20. Escreva uma função que recebe uma lista de números e retorna uma nova lista com a soma
acumulada (ex: [1,2,3] → [1,3,6]).

EXERCÍCIOS 2
1. Crie um dicionário aluno com as chaves "nome": "João", "idade": 18, "nota": 9.5. Imprima a
idade.
2. Adicione a chave "cidade": "São Paulo" no dicionário aluno. Imprima todas as chaves.
3. Use um loop for para imprimir todas as chaves e valores do dicionário aluno.
4. Crie um dicionário estoque com "maçã": 10, "banana": 5. Verifique se "laranja" existe (se não
existir, adicione com valor 0).
5. Crie um dicionário agenda onde cada contato é outro dicionário (nome, telefone, email).
Adicione 2 contatos e depois imprima o telefone do primeiro contato.

EXERCÍCIOS 3
Crie um programa simples de Lista de Tarefas (TODO List) em Python que funcione n
terminal.
O programa deve ter as seguintes opções:
1. Adicionar tarefa
2. Listar todas as tarefas
3. Marcar tarefa como concluída
4. Remover tarefa
5. Sair
Cada tarefa deve ser armazenada como um dicionário com duas chaves: "nome" (string) e "feito"
(booleano).
Regras obrigatórias:
• Use apenas listas e dicionários (sem arquivos ou bibliotecas extras).
• Ao listar, mostre um número ao lado de cada tarefa e status FEITO ou ESPERA indicando
se está feita.
• Valide a entrada do usuário para não dar erro se ele digitar letra em vez de número.
• O programa deve continuar rodando até o usuário escolher sair.