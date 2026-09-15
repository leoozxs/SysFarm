from app.models.usuario import Usuario

class Usuario_Controller:
    def __init__(self, view, dao):
        self.dao = dao
        self.view = view
        self.usuario_selecionado = None
    
    def new(self):
        pass
    
    def save(self):
        pass
    
    def update(self, usuario):
        pass
    
    def delete(self):
        pass
    
    def get_all(self):
        pass
    
    def selecionar_usuario(self, event):
        pass