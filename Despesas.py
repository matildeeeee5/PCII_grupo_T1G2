from classes.Gclass import Gclass
from classes.Grupo import Grupo
from classes.Viagem import Viagem
import datetime

class Despesas(Gclass):
    Despesass = []
    obj = dict()
    lst = list()
    pos = 0
    sortkey = ''
    auto_number = 0
    nkey = 1
    att = ['_idcompra', '_idgrupo', '_descrição', '_data', '_valorcompra', '_namigos', '_valorpp']
    header = 'Despesas'
    des = ['Idcompra', 'Idgrupo', 'Descrição', 'Data', 'Valor da Compra', 'Número de Amigos', 'Valor por Pessoa']
    grupo_not_found = False  # Variable to check if idgrupo exists

    def __init__(self, idcompra, idgrupo, descricao, data, valorcompra=0, namigos=0, valorpp=0):
        super().__init__()
        if idgrupo in Grupo.lst:
            self._idcompra = idcompra
            self._idgrupo = idgrupo
            self._descrição = str(descricao)
            self._data = datetime.date.fromisoformat(data)
            self._namigos = int(namigos)
            self._valorcompra = float(valorcompra)
            self._valorpp = round((float(valorcompra) / int(namigos)) if self._namigos > 0 else 0, 2)
            Grupo.obj[idgrupo]._total_despesas += self._valorcompra

            Despesas.obj[idcompra] = self
            Despesas.lst.append(idcompra)
            Despesas.grupo_not_found = False
        else:
            Despesas.grupo_not_found = True
            print("Este grupo não existe")

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
        if idcompra in cls.obj:
            raise ValueError("idcompra já existe")
        despesa = Despesas(idcompra, descricao, data, valorcompra, namigos)
        cls.Despesass.append(despesa)
        return despesa

    