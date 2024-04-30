#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 11:13:53 2024

@author: rebecark
"""

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

    def __init__(self, grupo_id, nome, senha=''):
        super().__init__()
        self._grupo_id = grupo_id
        self._nome = nome
        self._participantes = []  
        self._total_despesas = 0.0 
        self._senha = senha

        Grupo.obj[grupo_id] = self
        Grupo.lst.append(grupo_id)

    @property
    def grupo_id(self):
        return self._grupo_id

    @grupo_id.setter
    def grupo_id(self, grupo_id):
        self._grupo_id = grupo_id

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def participantes(self):
        return self._participantes

    def adicionar_participante(self, participante):
        self._participantes.append(participante)

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
