from app.models.lote import Lote
from app.models.usuario import Usuario
class Entrada:
    def __init__(self, id, lote: Lote, qtd_entrada, data_entrada, usuario: Usuario):
        self._id = id
        self._lote = lote
        self._qtd_entrada = qtd_entrada
        self._data_entrada = data_entrada
        self._usuario = usuario
        
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
    def qtd_entrada(self):
        return self._qtd_entrada
    @qtd_entrada.setter
    def qtd_entrada(self, novo_entrada):
        self._qtd_entrada = novo_entrada
        
    
    @property
    def data_entrada(self):
        return self._data_entrada
    @data_entrada.setter
    def data_entrada(self, novo_entrada):
        self._data_entrada = novo_entrada

    @property
    def usuario(self):
        return self._usuario
    @usuario.setter
    def usuario(self, novo_usuario):
        self._usuario = novo_usuario