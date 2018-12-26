# If, Elif e Else.
a = 1
b = 1
bol = a == b

# Printando a variavel bol e retornando a comparação.
print(bol)

# If.
if bol:
    a += 10 # adicionando 10 a variavel 'a', se ela for 'True'.

# Printando a variavel a.
print(a)

# Declarando a variavel 'nota', 'nota1', 'i', 'j'.

nota = [10, 7, 8, 9, 6, 9, 10] # Listas
nota1 = {'Adriano': 10, 'José': 7, 'Maria': 4} # Dicionario
i = 0 # indice do aluno
j = 'Maria' # aluno

if nota1[j] >= 9:
    print('Aprovado')
elif nota1[j] >= 7:
    print('Recuperação')
else:
    print('Reprovado')