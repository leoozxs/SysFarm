from datetime import datetime
from app.models.usuario import Usuario

class Usuario_Controller:
    def __init__(self, view, dao):
        self.dao = dao
        self.view = view
        self.usuario_selecionado = None

    def new(self):
        self.usuario_selecionado = None
        self.view.limpar_campos()

    def save(self):
        try:
            nome, cpf, senha, cargo, data_entrada = self.view.ler_dados_usuario()
            data_entrada = datetime.strptime(data_entrada, "%d/%m/%Y").date()
            usuario = Usuario(None, nome, cpf, senha, cargo, data_entrada)
            self.dao.save(usuario)
            self.get_all()
            self.view.exibir_mensagem("Usuário cadastrado com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def update(self):
        if self.usuario_selecionado is None:
            self.view.exibir_mensagem("Selecione um usuario na lista", False)
            return
        try:
            nome, cpf, senha, cargo, data_entrada = self.view.ler_dados_usuario()
            data_entrada = datetime.strptime(data_entrada, "%d/%m/%Y").date()
            self.usuario_selecionado.atualizar_dados(nome, cpf, senha, cargo, data_entrada)
            self.dao.update(self.usuario_selecionado)
            self.get_all()
            self.view.exibir_mensagem("Usuário atualizado com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def delete(self):
        if self.usuario_selecionado is None:
            self.view.exibir_mensagem("Selecione um usuario na lista.", False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.usuario_selecionado.id)
            if sucesso:
                self.usuario_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem("Usuario excluído com sucesso!")
            else:
                self.view.exibir_mensagem("Usuario não encontrado.", False)
        except Exception as e:
            self.view.exibir_mensagem(f"Problemas ao excluir usuario. Erro: {str(e)}", False)

    def get_all(self):
        usuarios = self.dao.get_all()
        self.view.exibir_usuarios(usuarios)

    def selecionar_usuario(self, event):
        try:
            id_usuario = self.view.get_id_selecionado()
            self.usuario_selecionado = self.dao.get_by_id(id_usuario)
            self.view.preencher_campos(self.usuario_selecionado)
        except IndexError:
            pass