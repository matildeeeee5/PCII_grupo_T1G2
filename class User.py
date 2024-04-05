from classes.gclass import Gclass
import datetime
class User(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey= 1
    att = ['_username','_nome','_email','_senha','_ncartao','_dvc','_cvc','_saldo','_ntelemovel']
    header = 'Utilizador'
    des = ['Username','Nome','Email','Senha','Número do Cartão','Data de Vencimento do Cartão','Código de Verificação do Cartão','Saldo','Número de Telemóvel']
    def _init_ (self, username, nome, email, senha, ncartao, dvc, cvc, ntelemovel, saldo=0):
        super().__init__()
        self._username = username
        self._nome= nome 
        self._email = email 
        self._senha = str(senha) 
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
    @username.setter 
    def username(self,username):
        self._username = username
        
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
        return self._senha
    @senha.setter
    def senha(self, senha):
        self._senha= senha
        
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