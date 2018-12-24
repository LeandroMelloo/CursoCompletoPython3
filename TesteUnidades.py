# 1° Escreva uma breve descrição de todos os seguintes tipos de objetos e estruturas de dados sobre os quais aprendemos:

# Numeros:
numero = 1

# printando Numeros:
print(numero)

# printando tipo Numeros:
print(type(numero))

# String:
string = '1'

# printando String:
print(string)

# printando tipo String:
print(type(string))

# Listas:
listas = [1, 2, 3, 4]

# printando Listas:
print(listas)

# printando tipo Listas:
print(type(listas))

# Tuplas:
tuplas = (1, 2, 3, 4)

# printando Tuplas:
print(tuplas)

# printando tipo Tuplas:
print(type(tuplas))

# Dicionarios:
dicionarios = {'Chave1': 1, 'Chave2': 2, 'Chave3': 3, 'Chave4': 4}

# printando Dicionarios:
print(dicionarios)

# printando tipo Dicionarios:
print(type(dicionarios))

# 2° Escreva uma equacão que use multiplicação, divisão, adição, subtração, exponenciação igual 100.25.

# Escrevendo a equação:
equacao = ((10*10)/2 ** 2 - (-70.25) + 5)

# Printando a resposta:
print(equacao)

# 3° Responda estas 3 perguntas sem digitar o código. Em seguida, digite o código para verificar sua resposta.

# Qual é o valor da expressão 4 * (6 + 5):
# Resposta: 44.

# Criando uma variavel expressao_1.
expressao_1 = 4 * (6 + 5)

# Printando a variavel expressao_1.
print(expressao_1)

# Qual é o valor da expressão 4 * 6 + 5:
# Resposta: 29.

# Criando uma variavel expressao_2.
expressao_2 = 4 * 6 + 5

# Printando a variavel expressao_2.
print(expressao_2)

# Qual é o valor da expressão 4 + 6 * 5:
# Resposta: 34.

# Criando uma variavel expressao_3.
expressao_3 = 4 + 6 * 5

# Printando a variavel expressao_3.
print(expressao_3)

# 4° Qual o tipo do resultado da expressão 3 + 1.5 + 4?
# Resposta: Ponto Flutuante, resultado 8.5.

# Criando uma variavel expressao_4.
expressao_4 = 3 + 1.5 + 4

# Printando a variavel expressao_4.
print(expressao_4)

# Printando o tipo da variavel expressao_4.
print(type(expressao_4))

# 4° O que você usaria para encontrar a raiz quadrada de um número, bem como seu quadrado.

# Criando uma variavel raiz_quadrada.
raiz_quadrada = 100 ** 2

# Printando a variavel raiz_quadrada.
print(raiz_quadrada)

# Criando uma variavel quadrado.
quadrado = 100 * 100

# Printando a variavel quadrado.
print(quadrado)

# Strings

# 5° Dado a string 'hello', de um comando de indice que retorna 'e'. Use o código abaixo:

# Criando a variavel s.
s = 'Hello'

# Printando a palavra 'e'.
print(s[1])

# 6° Inverta a string 'hello', de um comando que inverte. Use o código abaixo:

# Printando a palavra invertida 'hello'.
print(s[::-1])

# 7° Dado o exemplo de linha, dê dois métodos pra produzir a letra 'o' usando indexação:

# Printando a palavra 'o'.
print(s[4])

# Printando a palavra 'o'.
print(s[-1])

# Printando a palavra 'o'.
print(s[4:])

# Listas

# 8° Crie esta lista [0, 0, 0] duas formas diferentes.

# Criando a variavel lista.
lista = [0] * 3

# Printando a variavel lista.
print(lista)

# Criando a variavel lista1.
lista1 = [0, 0, [1, 2, 3]]

# Printando a variavel lista1.
print(lista1)

# 9° Altere o valor da lista1 da posição => 0 com o valor '1' por 'string'.

# Alterando o valor da lista.
lista1[2][0] = 'string'

# Printando a variavel lista1.
print(lista1)

# 10° Ordenando a lista.

# Criando a variavel l.
l = [1, 4, 2, 7, 9, 4, 2, 5, 0]

# Printando a variavel l e ordenando.
print(sorted(l))

# Dicionarios

# 11° Usando chaves e indexação, pague o 'hello' dos seguintes dicionarios:

# criando a variavel d.
d = {'keys':'hello'}

# Printando a variavel d.
print(d['keys'])

# criando a variavel d1.
d1 = {'k1':{'k2':'hello'}}

# Printando a variavel d.
print(d1['k1']['k2'])

# criando a variavel d2.
d2 = {'k1':[{'nest_key':['hello is deep', ['hello']]}]}

# Printando a variavel d.
print(d2['k1'][0]['nest_key'][1][0])


# criando a variavel d3.
d3 = {'k1':[1,2,{'k2':['hello is deep',{'not found':[1,2,['hello']]}]}]}

# Printando a variavel d3.
print(d3['k1'][2]['k2'][1]['not found'][2][0])

# 12° Você pode classificar um dicionario? Por que ou por que não?
# Resposta: Não, dicionarios normais são mapeados não uma sequencia.

# Tuplas

# 13° Qual a principal diferença entre Tuplas e as Listas?
# Resposta: Tuplas são imutaveis e Listas são mutaveis.

# 14° Como você cria uma Tupla?

# Criando a variavel t, e criando uma Tupla.
t = (1, 2, 3)

# Printando a variavel t.
print(t)

# Conjuntos

# 15° O que é único em um conjunto?
# Resposta: Eles não permitem elementos duplicados, exemplo [1, 1]

# Construindo um conjunto com a variavel c.
c = [1, 1, 2, 3, 4, 4, 5, 8, 9, 4, 6, 7, 0, 0, 8, 90, 43]

# Printando o conjunto
print(set(c))

# Booleanos

# 16° Qual será o Booleano resultante dos seguintes códigos:

print(2 > 3) # False
print(3 <= 2) # False
print(3 == 0.2) # False
print(3 == 3.0) # True
print(4**0.5 != 2) # False

# 17° Qual a saída booleana do bloco de código abaixo:

# Duas listas alinhadas

l_one = [1, 2, [3, 4]]
l_two = [1, 2, {'k1': 4}]

# Verdadeira ou falsa?
b = l_one[2][0] >= l_two[2]['k1'] # False

