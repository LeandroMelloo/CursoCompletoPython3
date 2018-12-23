#Printando uma String em python.
print('Olá Mundo!!!')

#Printando o tipo de valor em python.
print(type('Olá Mundo!!!'))

#Printando uma citação utilizando aspas duplas => "".
print('Olá Mundo, "tudo bem"?') # => valid syntax.

#Citação utilizando aspas simples => '', da erro.
# print('Olá Mundo, 'tudo bem'?') => invalid syntax.

# printando o tamanho da String => len.
print(len('Olá Mundo, "tudo bem"?')) # => valid syntax.

# declarando uma variavel s.
s = 'Olá Mundo'

# printando a variavel s.
print(s)

# printando o tipo da variavel s.
print(type(s))

# printando a posicao 1 => l da variavel s, indexação do ponto.
print(s[1])

# ignorando as duas primeiras posições e as 3 últimas posições printando a palavra 'Mundo', indexação múltiplos.
print(s[4:9])

# começando do final pro inicio e ignorando as três últimas posições.
print(s[:-3])

#indexação de espaçamentos de elementos de 2 em 2.
print(s[::2])

#indexação de espaçamentos de elementos de de 3 em 3.
print(s[::3])

#invertendo strings pegando elementos de -1.
print(s[::-1])

#concatenando string => +.
s = s + ', que dia lindo!!!'

#printando a variavel s concatenada.
print(s)

#declarando a variavel letra.
letra = 'g'

#printando a variavel g.
print(letra)

#printando 10 x a variavel letra => 'gggggggggg'
print(letra * 10)

#objetos tem seu metodo especifico s.lower() => coloca tudo em caixa baixa, minusculo.
print(s.lower())

#objetos tem seu metodo especifico s.split() => dividi minha string.
print(s.split())

#objetos tem seu metodo especifico s.split() => dividi minha string em 2 objetos.
print(s.split(','))