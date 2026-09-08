from app.models.lote import Lote

class Entrada:
    def __init__(self, id, lote: Lote, qtd_entrada, data_entrada):
        self._id = id
        self._lote = lote
        self._qtd_entrada = qtd_entrada
        self._data_entrada = data_entrada
        
    @property
    def id(self):
        return self._id
    @id.setter
    def id(self, novo_id):
        self._id = novo_id
        