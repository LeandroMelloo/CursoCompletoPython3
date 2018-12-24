# Criando uma variavel mylist e adicionando uma lista.
mylist = [1,2,3]

# Printando a variavel mylist.
print(mylist)

# Printando a posição [1] da lista.
print(mylist[1])

# Criando uma variavel my_dict e adicionando um dicionario, acessar o dicionario atraves da sua chave.
my_dict = {'chave':1.3, 'chave2':'string', 'chave3':True, 'chave4':[1,2,3,4,5]}

# Printando o tipo da variavel.
print(type(my_dict))

# Printando a variavel my_dict.
print(my_dict['chave4'])

# Criando uma variavel my_dict1 e adicionando um array.
my_dict1 = ['String']

# Printando a variavel my_dict1.
print(my_dict1[0][2])

# Dicionarios são mutaveis então eu posso modificar.
my_dict['chave4'] = {123}

# Printando a variavel my_dict.
print(my_dict)

# Criando uma variavel d, e posso criar ela vazia e adicionar valores dentro dela.
d = {}

# Adcionando valores dentro do dicionario.
d['key'] = 'Dog'
d['key1'] = 'cat'

# Printando a variavel d, com valores.
print(d)

#todos os elementos dentro da variavel d, my_dict, my_dict1, com o metodo keys().
d.keys()
my_dict.keys()

# Printando todas variaveis.
print(list(d)[1])
print(my_dict.keys())

#todos os elementos dentro da variavel d, my_dict, my_dict1, com o metodo values().
d.values()
my_dict.values()

# Printando todas variaveis.
print(d.values())
print(my_dict.values())

#todos os elementos dentro da variavel d, my_dict, my_dict1, com o metodo items().
d.items()
my_dict.items()

# Printando todas variaveis.
print(d.items())
print(my_dict.items())

#1. Os dicionários mantêm uma ordem? Como faço para imprimir os valores do dicionário em ordem?

# Os dicionários são mapeamentos e não mantêm uma ordem! Se você quer as capacidades de um dicionário, 
# mas você gostaria de fazer um ordenamento também, confira a aula de dicionário ordenado mais tarde no curso!

d1 = {'k1': [1,2,3]}
print(d1['k1'][1])