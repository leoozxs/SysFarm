from app.models.fornecedor import Fornecedor
from app.core.idioma import Idioma

# Criando classe Fornecedor
class Fornecedor_Controller:
    def __init__(self, view, dao):
        self.dao = dao
        self.view = view
        self.fornecedor_selecionado = None
        
    def new(self):
        self.fornecedor_selecionado = None
        self.view.limpar_campos()

    def save(self):
        try:
            nome, cnpj = self.view.ler_dados_fornecedor()
            if not nome or not cnpj:
                self.view.exibir_mensagem(Idioma.t("fornecedor.campo_ausente"), False)
                return
            fornecedor = Fornecedor(None, nome, cnpj)
            self.dao.save(fornecedor)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("fornecedor_cadastrado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def update(self):
        if self.fornecedor_selecionado is None:
            self.view.exibir_mensagem(Idioma.t("fornecedor.campo_ausente"), False)
            return
        try:
            nome, cnpj = self.view.ler_dados_fornecedor()
            if not nome or not cnpj:
                self.view.exibir_mensagem(Idioma.t("fornecedor.erro_selecao"), False)
                return
            self.fornecedor_selecionado.nome = nome
            self.fornecedor_selecionado.cnpj = cnpj
            self.dao.update(self.fornecedor_selecionado)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("fornecedor_atualizado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def delete(self):
        if self.fornecedor_selecionado is None:
            self.view.exibir_mensagem(Idioma.t("selecione_fornecedor"), False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.fornecedor_selecionado.id)
            if sucesso:
                self.fornecedor_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(Idioma.t("fornecedor_excluido_sucesso"))
            else:
                self.view.exibir_mensagem(Idioma.t("fornecedor_nao_encontrado"), False)
        except Exception as e:
            self.view.exibir_mensagem(f"{Idioma.t('erro_excluir_fornecedor')}. {Idioma.t('comum.erro_prefixo')} {str(e)}", False)

    def get_all(self):
        fornecedores = self.dao.get_all()
        self.view.exibir_fornecedores(fornecedores)

    def selecionar_fornecedor(self, event):
        try:
            id_fornecedor = self.view.get_id_selecionado()
            self.fornecedor_selecionado = self.dao.get_by_id(id_fornecedor)
            self.view.preencher_campos(self.fornecedor_selecionado)
        except IndexError:
            pass