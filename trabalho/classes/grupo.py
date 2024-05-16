import bcrypt
from classes.Gclass import Gclass
class Grupo(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey= 1
    att = ['_grupo_id', '_nome', '_participantes', '_total_despesas', '_senha']
    header = 'Grupo'
    des = ['ID do Grupo', 'Nome', 'Participantes', 'Total de Despesas', 'Senha']

    def __init__(self, grupo_id, nome, participantes, senha=''):
        super().__init__()
        self._grupo_id = grupo_id
        self._nome = nome
        self._participantes = participantes  
        self._total_despesas = 0.0 
        self._senha = senha

        Grupo.obj[grupo_id] = self
        Grupo.lst.append(grupo_id)

    @property
    def grupo_id(self):
        return self._grupo_id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def participantes(self):
        return self._participantes

    @property
    def total_despesas(self):
        return self._total_despesas

    def adicionar_despesa(self, valor):
        self._total_despesas += valor

    @property
    def senha(self):
        return self._senha

    @senha.setter
    def senha(self, senha):
        self._senha = senha
        
    @classmethod
    def chk_password(self, user, senha):
        Grupo.grupo_id = ''
        if user in Grupo.obj:
            obj = Grupo.obj[user]
            valid = bcrypt.checkpw(senha.encode(), obj._senha.encode())
            if valid:
                Grupo.grupo_id = user
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
