from classes.Gclass import Gclass
class AmigosDespesas(Gclass):
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey= 1
    att = ['_idconta','_iddespesa','_usernameamigo']
    header = 'AmigosDespesas'
    des = ['Id','Id Despesa','Username do Amigo']
    def __init__ (self, idconta, iddespesa, usernameamigo):
        super().__init__()
        self._idconta = idconta
        self._iddespesa = str(iddespesa)
        self._usernameamigo = str(usernameamigo)
        
        AmigosDespesas.obj[idconta] = self
        AmigosDespesas.lst.append(idconta)
        
        
    @property
    def idconta(self):
       return self._idconta
   
    @property 
    def iddespesa(self):
        return self._iddespesa
    
    @property 
    def usernameamigo(self):
        return self._usernameamigo