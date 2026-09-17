from datetime import datetime
from app.models.fornecedor import Fornecedor

class Fornecedor_Controller:
    def __init__(self,view, dao):
        self.dao = dao
        self.view = view
        self.fornecedor_selecionado = None
        
    def new(self):
        self.fornecedor_selecionado = None
        self.view.limpar_campos()
        
    def save(self):
        try:
            nome, cnpj, telefone, email, endereco = self.view.ler_dados_fornecedor()
            fornecedor = Fornecedor(None, nome, cnpj, telefone, email, endereco)
            self.dao.save(fornecedor)
            self.get_all()
            self.view.exibir_mensagem("Fornecedor cadastrado com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)
            
    def update(self):
        if self.fornecedor_selecionado is None:
            self.view.exibir_mensagem("Selecione um fornecedor na lista", False)
            return
        try:
            nome, cnpj, telefone, email, endereco = self.view.ler_dados_fornecedor()
            self.fornecedor_selecionado.atualizar_dados(nome, cnpj, telefone, email, endereco)
            self.dao.update(self.fornecedor_selecionado)
            self.get_all()
            self.view.exibir_mensagem("Fornecedor atualizado com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)
            
    def delete(self):
        if self.fornecedor_selecionado is None:
            self.view.exibir_mensagem("Selecione um fornecedor na lista.", False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.fornecedor_selecionado.id)
            if sucesso:
                self.fornecedor_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem("Fornecedor excluído com sucesso!")
            else:
                self.view.exibir_mensagem("Fornecedor não encontrado.", False)
        except Exception as e:
            self.view.exibir_mensagem(f"Problemas ao excluir fornecedor. Erro: {str(e)}", False)
            
    def get_all(self):
        fornecedores = self.dao.get_all()
        self.view.exibir_fornecedores(fornecedores)
        
    def selecionar_fornecedor(self, fornecedor):
        try:
            id_fornecedor = self.view.get_id_selecionado()
            self.fornecedor_selecionado = self.dao.get_by_id(id_fornecedor)
            self.view.exibir_fornecedor(self.fornecedor_selecionado)
        except IndexError:
            pass