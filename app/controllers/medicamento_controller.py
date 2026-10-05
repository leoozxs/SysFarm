from app.models.medicamento import Medicamento
from app.core.idioma import Idioma

class Medicamento_Controller:
    def __init__(self, view, dao):
        self.dao = dao
        self.view = view
        self.medicamento_selecionado = None

    def new(self):
        self.medicamento_selecionado = None
        self.view.limpar_campos()

    def save(self):
        try:
            nome, tipo, categoria, dosagem = self.view.ler_dados_medicamento()
            if not tipo or not categoria or not dosagem or not nome:
                self.view.exibir_mensagem(Idioma.t("medicamento.erro_selecao"), False)
                return
            medicamento = Medicamento(None, nome, tipo, categoria, dosagem)
            self.dao.save(medicamento)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("medicamento.cadastrado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{str(e)}", False)

    def update(self):
        if self.medicamento_selecionado is None:
            self.view.exibir_mensagem(Idioma.t("medicamento.selecione_da_lista"), False)
            return
        try:
            nome, tipo, categoria, dosagem = self.view.ler_dados_medicamento()
            if not tipo or not categoria or not dosagem or not nome:
                self.view.exibir_mensagem(Idioma.t("medicamento.erro_selecao"), False)
                return
            self.medicamento_selecionado.atualizar_dados(nome, tipo, categoria, dosagem)
            self.dao.update(self.medicamento_selecionado)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("medicamento.atualizado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def delete(self):
        if self.medicamento_selecionado is None:
            self.view.exibir_mensagem(Idioma.t("medicamento.selecione_da_lista"), False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.medicamento_selecionado.id)
            if sucesso:
                self.medicamento_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(Idioma.t("medicamento.excluido_sucesso"))
            else:
                self.view.exibir_mensagem(Idioma.t("medicamento.nao_encontrado"), False)
        except Exception as e:
            self.view.exibir_mensagem(f"{Idioma.t('medicamento.erro_ao_excluir')}. {Idioma.t('comum.erro_prefixo')} {str(e)}", False)

    def get_all(self):
        medicamentos = self.dao.get_all()
        self.view.exibir_medicamentos(medicamentos)

    def selecionar_medicamento(self, event):
        try:
            id_medicamento = self.view.get_id_selecionado()
            self.medicamento_selecionado = self.dao.get_by_id(id_medicamento)
            self.view.preencher_campos(self.medicamento_selecionado)
        except IndexError:
            pass