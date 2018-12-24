# Criando um arquivo my_file e abrindo o Arquivo com o método open.
my_file = open('Tuplas.py')

# Printando a variavel my_file.
print(my_file)

# Printando a variavel my_file e utilizando o método read().
print(my_file.read())

# Utilizando my_file.seek(0), para pegar da posição 0, e sendo assim utilizando o método readline.
my_file.seek(0)

# Printando a variavel my_file.
print(my_file.readline())

# Criando uma variavel arq e inserindo valores dentro do arquivo texto.py.
#!/usr/bin/env python
# -*- coding: utf-8 -*-
arq = open('texto.txt', 'w')
texto = """Lista de Alunos:
1- Joao da Silva
2- Jose Lima
3- Maria das Dores
4- Luciana
5- Leandro
6- Beatriz
"""
arq.write(texto) # comando para inserir informações em um arquivo .txt.
arq.close() # finaliza comando.

#!/usr/bin/env python
# -*- coding: utf-8 -*-
arq1 = open('texto1.txt', 'w')
texto1 = [] # monta uma lista.
print(texto)
texto1.append('Lista de Alunos: 1- Joao da Silva, 2- Jose Lima, 3- Maria das Dores') # comando .append inserindo valores nas linhas.
arq1.writelines(texto1) # comando para inserir informações em um arquivo .txt por linhas.
arq1.close() # finaliza comando.

#!/usr/bin/env python
# -*- coding: utf-8 -*-
arq = open('texto.txt', 'r')
texto = arq.read() # comando para ler informações em um arquivo .txt.
print(texto)
arq.close()

#!/usr/bin/env python
# -*- coding: utf-8 -*-
arq1 = open('texto1.txt', 'r')
texto1 = arq1.read() # comando para ler informações em um arquivo .txt.
print(texto1)
arq1.close()

# printando as linhas do arquivo texto.txt com o comando for line.
for line in my_file:
    print(line)
