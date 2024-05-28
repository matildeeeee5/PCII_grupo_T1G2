import bcrypt
from classes.Gclass import Gclass
import datetime
class User(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey= 1
    att = ['_username','_nome','_email','_senha','_ncartao','_dvc','_cvc','_ntelemovel','_saldo']
    header = 'Utilizador'
    des = ['Username','Nome','Email','Senha','Número do Cartão','Data de Vencimento do Cartão','Código de Verificação do Cartão','Número de Telemóvel','Saldo']
    username = ""
    def __init__ (self, username, nome, email, senha, ncartao, dvc, cvc, ntelemovel, saldo=0):
        super().__init__()
        self._username = username
        self._nome= nome 
        self._email = email 
        self._senha = self.set_password(senha) 
        self._ncartao = int(ncartao)
        self._dvc = datetime.date.fromisoformat(dvc) 
        self._cvc= int(cvc) 
        self._saldo = float(saldo)
        self._ntelemovel= int(ntelemovel)
        
        User.obj[username] = self
        User.lst.append(username)
        
    @property 
    def username(self):
        return self._username
        
    @property
    def nome(self):
        return self._nome
    @nome.setter 
    def nome(self,nome):
        self._nome = nome
        
    @property
    def email(self):
        return self._email
    @email.setter
    def email(self, email):
        self._email= email
        
    @property
    def senha(self):
        return ""
    @senha.setter
    def senha(self, senha):
        self._senha= senha

    @classmethod
    def chk_password(cls, user, senha):
        cls.username = ''
        if user in User.obj:
            obj = User.obj[user]
            valid = bcrypt.checkpw(senha.encode(), obj._senha.encode())
            if valid:
                User.username = user
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

    @property
    def ncartao(self):
        return self._ncartao
    @ncartao.setter
    def ncartao(self, ncartao):
        self._ncartao = ncartao
        
    @property
    def dvc(self):
        return self._dvc
    @dvc.setter
    def dvc(self, dvc):
        self._dvc = datetime.date.fromisoformat(dvc)
        
    @property
    def cvc(self):
        return self._cvc
    @cvc.setter
    def cvc(self, cvc):
        self._cvc = cvc

    @property
    def saldo(self):
        return self._saldo

    @property
    def ntelemovel(self):
        return self._ntelemovel
    @ntelemovel.setter
    def ntelemovel(self, ntelemovel):
        self._ntelemovel = ntelemovel