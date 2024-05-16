from datafile import filename

from classes.Despesas import Despesas

Despesas.read(filename + 'user.db')

obj = Despesas.from_string("123;maria;2024-02-24;300;3")

print("objeto sem estar gravado ",obj)

Despesas.insert(getattr(obj,Despesas.att[0]))

obj = Despesas.from_string("125;muito caro;2024-03-14;500;4")
Despesas.insert(getattr(obj,Despesas.att[0]))


print("\nLista dos onjetos gravados " ,Despesas.lst)


# alterar
obj = Despesas.first()
print ("\nPrimeiro objeto gravado ",obj)
obj.name = "WORD"
Despesas.update(getattr(obj, Despesas.att[0]))

Despesas.read(filename + 'user.db')

print("\nobjectos gravados")    
for code in Despesas.lst:
    print(Despesas.obj[code])