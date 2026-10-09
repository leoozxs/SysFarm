# Definindo a classe de estoque

class Estoque_Controller:
    def __init__(self, view, dao, abrir_entrada, abrir_saida):
        self.dao = dao
        self.view = view
        self._abrir_entrada = abrir_entrada
        self._abrir_saida = abrir_saida

# Definindo a lista do estoque
    def listar(self):
        estoques = self.dao.get_all()
        self.view.exibir_estoque(estoques)

# Função para abrir entrada de produtos
    def abrir_entrada(self):
        if self._abrir_entrada:
            self._abrir_entrada()

# Função para abrir a saída de produtos
    def abrir_saida(self):
        if self._abrir_saida:
            self._abrir_saida()