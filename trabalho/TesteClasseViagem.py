from datafile import filename

from classes.Viagem import Viagem

Viagem.read(filename + 'user.db')

obj = Viagem.from_string("i123;Roma;lmao;clara,maria,susana")

print("objeto sem estar gravado ",obj)

Viagem.insert(getattr(obj,Viagem.att[0]))

obj = Viagem.from_string("j459;Madrid;corpo;martim,camilo,sara")
Viagem.insert(getattr(obj,Viagem.att[0]))


print("\nLista dos onjetos gravados " ,Viagem.lst)


# alterar
obj = Viagem.first()
print ("\nPrimeiro objeto gravado ",obj)
obj.name = "WORD"
Viagem.update(getattr(obj, Viagem.att[0]))

Viagem.read(filename + 'user.db')

print("\nobjectos gravados")    
for code in Viagem.lst:
    print(Viagem.obj[code])