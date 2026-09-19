from datetime import datetime
from app.models.estoque import Estoque

class Estoque_Controller:
    def __init__(self, view, dao):
        self.dao = dao
        self.view = view
        self.estoque_selecionado = None
        
    def new(self):
        self.estoque_selecionado = None
        self.view.limpar_campos()
        
    def get_all(self):
        estoques = self.dao.get_all()
        self.view.exibir_estoques(estoques)