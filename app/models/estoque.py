from app.models.lote import Lote
from app.models.medicamento import Medicamento

class Estoque:
    def __init__(self, id, lote: Lote, medicamento: Medicamento, data_entrada, validade, qtd_atual):
        self._id = id
        self._lote = lote
        self._medicamento = medicamento
        self._data_entrada = data_entrada
        self._validade = validade
        self._qtd_atual = qtd_atual
    
    
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
    def medicamento(self):
        return self._medicamento
    @medicamento.setter
    def medicamento(self, novo_medicamento):
        self._medicamento = novo_medicamento
        
    
    @property
    def data_entrada(self):
        return self._data_entrada
    @data_entrada.setter
    def data_entrada(self, novo_data_entrada):
        self._data_entrada = novo_data_entrada
        
    @property
    def validade(self):
        return self._validade
    @validade.setter
    def validade(self, novo_validade):
        self._validade = novo_validade
        
    
    @property
    def qtd_atual(self):
        return self._qtd_atual
    @qtd_atual.setter
    def qtd_atual(self, novo_qtd_atual):
        self._qtd_atual = novo_qtd_atual
        