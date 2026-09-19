from datetime import datetime
from app.models.saida import Entrada

class Entrada_Controller:
    def __init__(self, view, dao):
        self.dao = dao
        self.view = view
        self.saida_selecionada = None
        
    def new(self):
        self.saida_selecionada = None
        self.view.limpar_campos()
        
    def save(self):
        try:
            lote_id, qtd_entrada, data_entrada, usuario_id = self.view_ler_dados_saida()
            data_entrada = datetime.strftime(data_entrada, "%d/%m/%Y").date()
            entrada = Entrada(None, lote_id, qtd_entrada, usuario_id)
            self.dao.save(entrada)
            self.get_all()
            self.view.exibir_mensagem("Entrada registrada!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)
            
    def update(self):
        if self.saida_selecionada is None:
            self.view.exibir_mensagem("Selecione uma saída na lista", False)
            return
        try:
            lote_id, qtd_entrada, data_entrada, usuario_id = self.view.ler_dados_saida()
            data_entrada = datetime.strftime(data_entrada, "%d/%m/%Y").date()
            self.entrada_selecionado.atualizar_dados(lote_id, qtd_entrada, usuario_id, data_entrada)
            self.dao.update(self.saida_selecionada)
            self.get_all()
            self.view.exibir_mensagem("Entrada atualizada com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)
            
    def get_all(self):
        entradas = self.dao.get_all()
        self.view.exibir_entradas(entradas)