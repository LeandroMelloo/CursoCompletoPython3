# Tuplas são semelhantes a listas, diferença entre elas lista inicia com [], e Tuplas com () 
# e Dicionarios com {'chave': 'valor'}.

# Criando uma variavel t.
t = ('one',2.3,[4,5,6,7,8,9],False)

# Printando o tipo da variavel t, pritando o tipo da variavel, e a posicao da variavel.
print(t)
print(type(t))
print(t.index('one'))

# Criando uma variavel l.
l = ['one',2.3,[4,5,6,7,8,9],False]

# Printando o tipo da variavel t.
print(type(l))

# Criando uma variavel d.
d = {'chave1':1,'chave2':2}

# Printando o tipo da variavel t.
print(type(d))

# Criando uma variavel t1.
t1 = (1,1,12,12,12,20,20,3,4)

# Printando a variavel t1 e contando o numero de elemento com o metodo count.
print(t1.count(12))