# -*- coding: utf-8 -*-
"""
@author: António Brito / Carlos Bragança
(2024)
#objective: Teste da classe Person
"""
# Importa a classe 'Person' que se encontra na pasta 'classes'
from classes.User import User

# Lê os dados da classe Person
User.read("data/")

# Percorre os objetos do primeiro ao último
print("\nprimeiro->último:")
p1 = User.first()
while p1 != None:
    print(p1)
    p1 = User.nextrec()

# Percorre os objetos do último ao primeiro
print("\núltimo->primeiro:")
p1 = User.last()
while p1 != None:
    print(p1)
    p1 = User.previous()

# Cria um novo objeto Pessoa
print("\nPessoa com o código 'mul06' criada:")
p1 = User("mul06","André Pereira","679@up.pt","ddDfe23","3002348","15-03-2032","92345867")
print(p1)

# Percorre os objetos usando as variáveis de classe 'obj' e 'lst'
print("\nVariáveis de classe 'obj' e 'lst'")
for codigo in User.lst:
    p1 = User.obj[codigo]
    print(p1)

# Acede ao objeto cujo código é 555
print("\nPessoa com o código 'mul06':")
p1 = User.obj['mul06']
print(p1)

# Apaga a o objeto pessoa com o código '555'
print("\nPessoa com o código mul06 removida")
User.remove('mul06')

# Percorre os objetos usando a variável de classe 'obj'
print("\nVariável de classe 'obj':")
for p1 in User.obj.values():
    print(p1)

# Escreve os dados da classe Person
User.write("data/")
