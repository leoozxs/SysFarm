from datetime import datetime
from app.models.saida import Saida

class Saida_Controller:
    def __init__(self, view, dao):
        self.dao = dao
        self.view = view
        self.saida_selecionada = None
        
    def new(self):
        self.saida_selecionada = None
        self.view.limpar_campos()
        
    def save(self):
        try:
            lote_id, qtd_saida, tipo_saida, usuario_id, data_saida = self.view.ler_dados_saida()
            data_saida = datetime.strftime(data_saida, "%d/%m/%Y").date()
            saida = Saida(None, lote_id, qtd_saida, tipo_saida, usuario_id, data_saida)
            self.dao.save(saida)
            self.get_all()
            self.view.exibir_mensagem("Saída registrada!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)
            
    def update(self):
        if self.saida_selecionada is None:
            self.view.exibir_mensagem("Selecione uma saída na lista", False)
            return
        try:
            lote_id, qtd_saida, tipo_saida, usuario_id, data_saida = self.view.ler_dados_saida()
            data_saida = datetime.strftime(data_saida, "%d/%m/%Y").date()
            self.saida_selecionada.atualizar_dados(lote_id, qtd_saida, tipo_saida, usuario_id, data_saida)
            self.dao.update(self.saida_selecionada)
            self.get_all()
            self.view.exibir_mensagem("Saída atualizada com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)
    
    def get_all(self):
        saidas = self.dao.get_all()
        self.view.exibir_saidas(saidas)