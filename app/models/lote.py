class Lote:
    def __init__(self, id, numero_lote, medicamento_id, fornecedor_id, validade):
        self.id = id
        self.numero_lote = numero_lote
        self.medicamento_id = medicamento_id
        self.fornecedor_id = fornecedor_id
        self.validade = validade
        
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
    return self._medicamento_id

@medicamento_id.setter
def medicamento_id(self, novo_medicamento_id):
    self._medicamento_id = novo_medicamento_id

@property
def fornecedor_id(self):
    return self._fornecedor_id

@fornecedor_id.setter
def fornecedor_id(self, novo_fornecedor_id):
    self._fornecedor_id = novo_fornecedor_id

@property
def validade(self):
    return self._validade

@validade.setter
def validade(self, nova_validade):
    self._validade = nova_validade