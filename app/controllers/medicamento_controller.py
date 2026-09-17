from datetime import datetime
from app.models.medicamento import Medicamento

class Medicamento_Controller:
    def __init__ (self, view, dao):
        self.dao = dao
        self.view = view
        self.medicamento_selecionado = None
        
    def new(self):
        self.medicamento_selecionado = None
        self.view.limpar_campos()
        
    def save(self):
        try:
            nome, descricao, preco, quantidade, data_validade = self.view.ler_dados_medicamento()
            data_validade = datetime.strptime(data_validade, "%d/%m/%Y").date()
            medicamento = Medicamento(None, nome, descricao, preco, quantidade, data_validade)
            self.dao.save(medicamento)
            self.get_all()
            self.view.exibir_mensagem("Medicamento cadastrado com sucesso")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)
            
    def update(self):
        if self.medicamento_selecionado is None:
            self.view.exibir_mensagem("Selecione um medicamento na lista", False)
            return
        try:
            nome, descricao, preco, quantidade, data_validade = self.view.ler_dados_medicamento()
            data_validade = datetime.strptime(data_validade, "%d/%m/%Y").date()
            self.medicamento_selecionado.atualizar_dados(nome, descricao, preco, quantidade, data_validade)
            self.dao.update(self.medicamento_selecionado)
            self.get_all()
            self.view.exibir_mensagem("Medicamento atualizado com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)
            
    def delete(self):
        if self.medicamento_selecionado is None:
            self.view.exibir_mensagem("Selecione um medicamento na lista.", False)
            return
        if not self.view.confirma_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.usuario_selecionado.id)
            if sucesso:
                self.medicamento_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem("Medicamento excluído com sucesso!")
            else:
                self.view.exibir_mensagem("Medicamento não encontrado.", False)
        except Exception as e:
            self.view.exibir_mensagem(f"Problemas ao excluir medicamento. Erro: {str(e)}", False)
            
    def get_all(self):
        medicamentos = self.dao.get_all()
        self.view.exibir_medicamentos(medicamentos)
        
    def selecionar_medicamento(self, event):
        try:
            id_medicamento = self.view.get_id_selecionado()
            self.medicamento_selecionado = self.dao.get_by_id(id_medicamento)
            self.view.preencher_campos(self.usuario_selecionado)
        except IndexError:
            pass