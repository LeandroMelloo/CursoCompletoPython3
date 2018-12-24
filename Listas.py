# Criando uma variavel my_list e inserindo valores dentro de um array em python. 
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Printando a variavel my_list.
print(my_list)

# Criando uma variavel my_list1 e inserindo diversos valores dentro de um array em python. 
my_list1 = [1, 2.9, 'String 3', 4.99, '5', 6, 7.999, 8, 9, 0]

# Printando a variavel my_list1.
print(my_list1)

# Uma lista é uma sequencia de valores ou objetos.

# Printando uma posição dentro de um array da variavel my_list.
print(my_list[3])

# Printando uma posição dentro de um array da variavel my_list1.
print(my_list1[2: ])

# Printando uma posição dentro de um array da variavel my_list1.
print(my_list1[-1]) # pego a última posição => 0.

# Concatenado as duas variaveis my_list + my_list1.
print(my_list + my_list1)

# Inserindo um valor numa nova lista my_list.
my_list = my_list + ['Beatriz']

# Printando a variavel my_list com um novo valor => 'Leandro'.
print(my_list)

# Inserindo um valor numa nova lista my_list.
my_list = my_list + ['Leandro']

# Printando a variavel my_list com um novo valor => 'Beatriz'.
print(my_list)

# Printando a Lista varias vezes, ou seja printando a variavel my_list 10 vezes => my_list * 10.
print(my_list * 10)

# Verificando o tipo da variavel my_list => com o metodo 'type'.
print(type(my_list))

# Verificando o tamanho da variavel my_list => com o metodo 'len'.
print(len(my_list))

# Acessando os metodos de uma lista, método .append => adiciona um elemento a sua lista.
my_list.append('Luciana')

# Printando o elemento my_list.append('Luciana').
print(my_list)


# Acessando os metodos de uma lista, método .pop => remove um elemento da sua lista, e imprime na tela, no caso o elemento da posição [0].
# .pop() por padrão remove o último valor de uma lista.
my_list.pop(0)

# Printando o elemento my_list.append('Luciana').
print(my_list)

# Acessando os metodos de uma lista, método .pop => remove um elemento da sua lista, e imprime na tela, no caso o elemento da posição [0].
# .pop() por padrão remove o último valor de uma lista.
my_list.pop()

# Printando o elemento my_list.append('Luciana').
print(my_list)

# Guardando um elemnto em uma variavel, após remover com o metodo .pop().
# Criando a variavel pop.
pop = my_list.pop(1)

# Printando a variavel pop.
print(pop)

# Printando a variavel my_list.
print(my_list)

# Criando uma variavel new_list.
new_list = ['a', 'c', 'e', 'x', 'b']

# Printando a variavel new_list.
print(new_list)

# Revertendo a variavel new_list com o método reverse.
new_list.reverse()

# Printando a variavel new_list.
print(new_list)

# Método sort => ordena os elementos de uma lista.
new_list.sort()

# Printando a variavel new_list.
print(new_list)

# Reverse utilizando indexação.
new_list[::-1]

# Printando a variavel new_list.
print(new_list)

# Revertendo a variavel new_list com o método reverse.
new_list.reverse()

# Printando a variavel new_list.
print(new_list)

# Criando variaveis list1, list2, list3 e inserindo valores.
list1 = [1,2,3]
list2 = [4,5,6]
list3 = [7,8,9]

# Criando uma Matriz com as variaveis list1, list2, list3 iniciando uma variavel matriz.
matriz = [list1, list2, list3]

# Printando a variavel matriz, lista de duas dimensões.
print(matriz)

# Printando o tamanho da matriz.
print(len(matriz))

# Printando o tamanho da matriz da posição 0.
print(len(matriz[0]))

# Posição [0] da variavel matriz
matriz[0]

# Printando a matriz
print(matriz)

# Printando o indice[0] da matriz
print(matriz[1])

# Printando o tamanho da da matriz
print(len(matriz[0]))

# Printando o indice[1] da matriz.
print(matriz[1][1])

# Metodo first_col = [row] = linha for row = linha in = na matriz, ou seja, pega linha a linha os elementos da posição [0].
first_col = [row[1] for row in matriz]

# Printando as linhas.
print(first_col)

# Metodo first_col1 = [matriz[0][0], matriz[1][0], matriz[2][0]] ou seja, pega linha a linha os elementos da posição [0].
first_col1 = [matriz[0][1], matriz[1][1], matriz[2][1]]

# Printando as linhas.
print(first_col1)

# 1. Como indexar uma lista aninhada? Por exemplo, se eu quiser puxar 2 da lista [1,1, [1,2]]?

# Você simplesmente adicionaria outro conjunto de colchetes para indexar a lista aninhada, 
# por exemplo: my_list [2] [1]. Descobriremos mais tarde objetos mais aninhados e 
# você terá a oportunidade de treinar mais.