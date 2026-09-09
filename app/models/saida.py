from app.models.lote import Lote
from app.models.usuario import Usuario

class Saida:
    def __init__(self, id, lote: Lote, qtd_saida, tipo_saida, usuario: Usuario, data_saida): # ENUM do lote e ENUM do usuário
        self._id = id
        self._lote = lote
        self._qtd_saida = qtd_saida
        self._tipo_saida = tipo_saida
        self._usuario = usuario
        self._data_saida = data_saida
        
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, novo_id):
        self._id = novo_id
    
    
    @property
    def lote(self):
        return self._lote
    @lote.setter
    def lote(self, novo_lote):
        self._lote = novo_lote
        
        
    @property
    def qtd_saida(self):
        return self._qtd_saida
    @qtd_saida.setter
    def qtd_saida(self, novo_saida):
        self._qtd_saida = novo_saida
        
    
    @property
    def tipo_saida(self):
        return self._tipo_saida
    @tipo_saida.setter
    def tipo_saida(self, novo_saida):
        self._tipo_saida = novo_saida
    
    
    @property
    def usuario(self):
        return self._usuario
    @usuario.setter
    def usuario(self, novo_usuario):
        self._usuario = novo_usuario
        
    
    @property
    def data_saida(self):
        return self._data_saida
    @data_saida.setter
    def data_saida(self, novo_data_saida):
        self._data_saida = novo_data_saida
        