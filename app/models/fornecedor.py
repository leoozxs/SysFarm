class Fornecedor:
    def __init__(self, id, nome, cnpj, ativo=True):
        self._id = id
        self._nome = nome
        self._cnpj = cnpj
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
    def cnpj(self):
        return self._cnpj

    @cnpj.setter
    def cnpj(self, novo_cnpj):
        self._cnpj = novo_cnpj
        
    @property
    def ativo(self):
        return self._ativo

    @ativo.setter
    def ativo(self, novo_ativo):
        self._ativo = novo_ativo