# Formatacao de Impressao.
print('This is a string')

# Criando uma variavel s .
s = 123

# Printando e colocando com %(s) a variavel s, substituindo %s=> a frase => Temos uma string auxiliar.
# %(variavel) converte em string.
print('Temos uma sequencia %s auxiliar.' %(s))

# Printando pontos flutuantes.
print('Printando pontos flutuantes: %1.2f' %(12.444))

# Printando e colocando com %(s) a variavel s, substituindo %r=> a frase => Temos uma sequencia 123 auxiliar.
# %(variavel) converte em string e %s é semelhante a %r, são diferenciadas por str() => %s e repr() => %r.
print('Temos uma sequencia %r auxiliar.' %(s))

# Criando uma variavel A1 e A2.
A1 = 'String'
A2 = 11111

# Printando a variavel e substituindo por %s e %r.
print('Aqui temos uma %s, e aqui temos uma sequencia %r.' %(A1, A2))

# Trabalhando com o método format, ou seja utilizando o método format tudo que 
# tiver dentro da chaves, vou tar criando um dicionario e lincar os valores que 
# tiver dentro das chaves e substituir.

# Criando a variavel Formato.
Formato = 'One: {a}, Two: {b}, Three: {c}'.format(a = 1, b = 'Leandro', c = 12.5)
print({Formato})

# https://pyformat.info/ => site para formatação