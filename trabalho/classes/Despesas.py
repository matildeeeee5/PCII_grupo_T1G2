from classes.Gclass import Gclass
import datetime
class Despesa(Gclass):
    despesas = []
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey= 1
    att = ['_idcompra','_descricao','_data','_valorpp','_namigos','_usernameamigos','_valorcompra']
    header = 'Utilizador'
    des = ['Idcompra','Descrição','Data','Valor por Pessoa','Número de Amigos','Username dos Amigos','Valor da Compra']
    username = ""
    def __init__ (self, idcompra, descricao, data, usernameamigos, valorcompra=0,namigos=0):
        super().__init__()
        self._idcompra = idcompra
        self._descricao= str(descricao)
        self._data = datetime.date.fromisoformat(data)
        self._namigos = int(namigos)
        self._usernameamigos = []
        self.add_username(usernameamigos)
        self._valorcompra = float(valorcompra)
        self._valorpp = float(valorcompra)/int(namigos)
        
        Despesa.obj[idcompra] = self
        Despesa.lst.append(idcompra)
    
    def add_username(self, namigos, username):
        for x in range(namigos-1):
            self._usernameamigos.append(username)
        
        
    @property
    def idcompra(self):
       return self._idcompra
   
    @property 
    def descricao(self):
        return self._descricao 
    
    @property 
    def data(self):
        return self._data 
    
    @property 
    def usernameamigos(self):
        return self._usernameamigos 
    
    @property 
    def valorpp(self):
        return self._valorpp 
    
    @property 
    def namigos(self):
        return self._namigos 
    
    @property 
    def valorcompra(self):
        return self._valorcompra
    
    @classmethod    
    def adicionar_despesa(cls, idcompra, descricao, data, usernameamigos, valorcompra=0, namigos=0):
        despesa = Despesa(idcompra, descricao, data, usernameamigos, valorcompra, namigos)
        cls.despesas.append(despesa)
        return despesa