from classes.Gclass import Gclass
import datetime
class Despesas(Gclass):
    Despesass = []
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey= 1
    att = ['_idcompra','_descrição','_data','_namigos','_valorcompra','_valorpp']
    header = 'Despesas'
    des = ['Idcompra','Descrição','Data','Número de Amigos','Valor da Compra','Valor por Pessoa']
    def __init__ (self, idcompra, descricao, data, valorcompra=0, namigos=0, valorpp=0):
        super().__init__()
        self._idcompra = idcompra
        self._descrição= str(descricao)
        self._data = datetime.date.fromisoformat(data)
        self._namigos = int(namigos)
        self._valorcompra = float(valorcompra)
        self._valorpp = (float(valorcompra)/int(namigos)) if self._namigos > 0 else 0
        
        Despesas.obj[idcompra] = self
        Despesas.lst.append(idcompra)
        
        
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
    def namigos(self):
        return self._namigos 
    
    @property 
    def valorcompra(self):
        return self._valorcompra
    
    @classmethod
    def adicionar_despesas(cls, idcompra, descricao, data, valorcompra=0, namigos=0):
        despesa = Despesas(idcompra, descricao, data, valorcompra, namigos)
        cls.Despesass.append(despesa)
        return despesa
    
