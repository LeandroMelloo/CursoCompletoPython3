# Opearacao Comparação em Cadeia

# Construindo variavel a, b, c.
a = 1
b = 2
c = 1

# Printando e comparando as variaveis.
print(a == c)
print(a == b)

# Printando e comparando as variaveis com o metodo 'and', ou seja, se todas as comparações forem verdadeiras retorna True
# senão retornará False.
print(a == c and b == 2 and c == 1)
print(a == b and c == 1 and b == 2)

# Printando e comparando as variaveis com o metodo 'or', ou seja, se uma comparação for verdadeira retornará True
# senão retornará False.
print(a == 2 or b == 1 or c == 3)
print(a == 2 or b == 2 or c == 3)
print((a != b or a == c) and b == 2)
