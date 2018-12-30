# Criando uma lista com a variavel 'l'.
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]

# Printando a variavel 'l'.
print(l)

# Printando a variavel 'num', utilizando o método 'for', para o objeto 'l'.
for num in l:
    print('Num vezes 1:', num)
    print('Num vezes 2:', num * 2)
    print('Num vezes 3:', num * 3)

# Printando se o número dentro da lista e par ou impar com o for.
for num in l:
    if num % 2 == 0:
        print(num, 'Este número e par.')
    else:
        print(num, 'Este número é impar.')

# Printando a somatoria de todos os numeros da lista.
sum_ = 0
for num in l:
    sum_ += num
print(sum_)

# Printando uma string.
string = 'String'
for strs in string:
    print(strs) 

# Printando uma tupla.
t = (1, 2, 3, 4, 5, 6)
for tup in t:
    print(tup)

# Printando uma lista com tuplas.
tl = [(1, 2, 3), (3, 4, 5), (6, 7, 8)]
for t1 in tl:
    print(t1)

# Printando um dicionario.]
d = {'k1': 1, 'k2': 2, 'k3': 3}
for item in d:
    print(item)

for (key, valor) in d.items():
    print(key, ':', valor)

for (key, valor) in d.items():
    print(key)

for (key, valor) in d.items():
    print(valor)
