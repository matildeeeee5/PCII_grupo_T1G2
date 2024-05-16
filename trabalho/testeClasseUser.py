from datafile import filename

from classes.User import User

User.read(filename + 'user.db')

obj = User.from_string("ulesr;Maria Joana;abc@gmail.com;ab23;22579;2005-03-12;345;963059685")

print("objeto sem estar gravado ",obj)

User.insert(getattr(obj,User.att[0]))

obj = User.from_string("mals;Pedro Amadeus;def@gmail.com;cd45;22580;2003-08-15;678;963059693;15")
User.insert(getattr(obj,User.att[0]))


print("\nLista dos onjetos gravados " ,User.lst)


# alterar
obj = User.first()
print ("\nPrimeiro objeto gravado ",obj)
obj.name = "WORD"
User.update(getattr(obj, User.att[0]))

User.read(filename + 'user.db')

print("\nobjectos gravados")    
for code in User.lst:
    print(User.obj[code])