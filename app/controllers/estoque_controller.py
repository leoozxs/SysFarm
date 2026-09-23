from app.models.estoque import Estoque

class Estoque_Controller:
    def __init__(self, view, dao):
        self.dao = dao
        self.view = view

    def listar(self):
        estoques = self.dao.get_all()
        self.view.exibir_estoque(estoques)