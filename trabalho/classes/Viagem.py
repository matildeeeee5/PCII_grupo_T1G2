import bcrypt
from classes.Gclass import Gclass
class Viagem(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey= 1
    att = ['_idviagem','_nome_viagem','_senha','_participantes']
    header = 'Viagem'
    des = ['Idviagem','Nome da Viagem','Senha','Participantes']
    idviagem = ""
    def __init__ (self, idviagem, nome_viagem, senha, participantes):
        super().__init__()
        self._idviagem = idviagem
        self._nome_viagem = str(nome_viagem)
        self._senha = senha
        self._participantes = list(participantes.split(","))
        
        Viagem.obj[idviagem] = self
        Viagem.lst.append(idviagem)
        
    @property 
    def idviagem(self):
        return self._viagem 
    
    @property 
    def nome_viagem(self):
        return self._nome_viagem
    @nome_viagem.setter 
    def nome_viagem(self,nome):
        self._nome_viagem = nome 
        
    @property 
    def senha(self):
        return self._senha
    @senha.setter 
    def senha(self,senha):
        self._senha = senha 
        
    @property 
    def participantes(self):
        return self._participantes 
    
    def adicionar_participantes(self,username):
        self._participantes.append(username)
        return self._participantes 
    
    @classmethod
    def chk_password(self, user, senha):
        Viagem.idviagem = ''
        if user in Viagem.obj:
            obj = Viagem.obj[user]
            valid = bcrypt.checkpw(senha.encode(), obj._senha.encode())
            if user in self._participantes and valid:
                Viagem.username = user
                message = "Valid"
            else:
                message = 'Wrong password'
        else:
            message = 'No existent user'
        return message
    @classmethod
    def set_password(self, password):
        passencrypted = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
        return passencrypted.decode()     