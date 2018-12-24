# Criando uma variavel 'x' e uma estrutura de set.
x = set()

# Printando o tipo da variavel x.
print(x)

# Printando o tipo da variavel x.
print(type(x))

# Metodo add(), irá adcionar elementos dentro do meu set().
x.add(1)
x.add(2)
x.add(1) # este 1 é ignorado no set().

# Printando o tipo da variavel x, set não precisa de chave valor.
print(x)

# Criando uma lista com varios elementos repetidos.
lista = [11, 11, 11, 22, 22, 22, 3, 4, 5, 6, 7, 7, 7]

# Printando a variavel lista.
print(lista)

# Criando uma variavel set_list, e passando por parametro lista.
set_list = set(lista)

# Printando a variavel set_list.
print(set_list) # elementos ordenados e únicos.

# Booleanos
a = True
b = False

# Printando elementos 
print(1 > 2)