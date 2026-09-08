class Usuario:
    def __init__(self, id, nome, cpf, senha, cargo, data_entrada, ativo=True):
        self._id = id
        self._nome = nome
        self._cpf = cpf
        self._senha = senha
        self._cargo = cargo
        self._data_entrada = data_entrada
        self._ativo = ativo
        
@property
def id(self):
    return self._id
    
@id.setter
def id(self, novo_id):
    self._id = novo_id
    
@property
def nome(self):
    return self._nome

@nome.setter
def nome(self, novo_nome):
    self._nome = novo_nome
    
@property
def cpf(self):
    return self._cpf

@cpf.setter
def cpf(self, novo_cpf):
    self._cpf = novo_cpf
    
@property
def senha(self):
    return self._senha

@senha.setter
def senha(self, novo_senha):
    self._senha = novo_senha

@property
def cargo(self):
    return self._cargo

@cargo.setter
def cargo(self, novo_cargo):
    self._cargo = novo_cargo
    
@property
def data_entrada(self):
    return self._data_entrada

@data_entrada.setter
def data_entrada(self, novo_entrada):
    self._data_entrada = novo_entrada

@property
def ativo(self):
    return self._ativo

@ativo.setter
def ativo(self, novo_ativo):
    self._ativo = novo_ativo