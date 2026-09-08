class Medicamento:
    def __init__(self, id, nome, tipo, categoria, dosagem, ativo=True):
        self._id = id
        self._nome = nome
        self._tipo = tipo
        self._categoria = categoria
        self._dosagem = dosagem
        self._ativo = ativo
   
        
        
    @property
    def id(self):
            return self._id
    @id.setter
    def id(self, novo_nome):
        self._id = novo_nome
        
        
        
    @property
    def nome(self):
        return self._nome
    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome
            
        
        
    @property
    def tipo(self):
        return self._tipo
    @tipo.setter
    def tipo(self, novo_tipo):
        self._tipo = novo_tipo
        
        
        
    @property
    def categoria(self):
        return self._categoria
    @categoria.setter
    def categoria(self, novo_categoria):
        self._categoria = novo_categoria
        
        
    @property
    def dosagem(self):
        return self._dosagem
    @dosagem.setter
    def dosagem(self, novo_dosagem):
        self._dosagem = novo_dosagem
        
        
        
    @property
    def ativo(self):
        return self._ativo
    @ativo.setter
    def ativo (self, novo_ativo):
        self._ativo = novo_ativo
                        
    