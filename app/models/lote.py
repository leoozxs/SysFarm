from app.models.medicamento import Medicamento
from app.models.fornecedor import Fornecedor

class Lote:
    def __init__(self, id, numero_lote, medicamento: Medicamento, fornecedor: Fornecedor, validade):
        self._id = id
        self._numero_lote = numero_lote
        self._medicamento = medicamento
        self._fornecedor = fornecedor
        self._validade = validade
        
@property
def id(self):
    return self._id

@id.setter
def id(self, novo_id):
    self._id = novo_id

@property
def numero_lote(self):
    return self._numero_lote

@numero_lote.setter
def numero_lote(self, novo_numero_lote):
    self._numero_lote = novo_numero_lote

@property
def medicamento_id(self):
    return self._medicamento

@medicamento_id.setter
def medicamento_id(self, novo_medicamento):
    self._medicamento = novo_medicamento

@property
def fornecedor_id(self):
    return self._fornecedor

@fornecedor_id.setter
def fornecedor_id(self, novo_fornecedor):
    self._fornecedor = novo_fornecedor

@property
def validade(self):
    return self._validade

@validade.setter
def validade(self, nova_validade):
    self._validade = nova_validade