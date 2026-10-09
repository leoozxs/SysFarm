from datetime import datetime
from app.models.usuario import Usuario
from app.core.idioma import Idioma
from mysql.connector import IntegrityError

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
            if not nome or not cpf or not senha or not cargo or not data_entrada:
                self.view.exibir_mensagem(Idioma.t("usuario.campo_ausente"), False)
                return
            try:
                data_entrada = datetime.strptime(data_entrada, "%d/%m/%Y").date()
            except ValueError:
                self.view.exibir_mensagem(Idioma.t("usuario.erro_data_invalida"), False)
                return
            usuario = Usuario(None, nome, cpf, senha, cargo, data_entrada)
            self.dao.save(usuario)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("usuario.cadastrado_sucesso"))
        except IntegrityError:
            self.view.exibir_mensagem(Idioma.t("usuario.IntegrityError1062"), False)
            return
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{str(e)}", False)

    def update(self):
        if self.usuario_selecionado is None:
            self.view.exibir_mensagem(Idioma.t("usuario.selecione_da_lista"), False)
            return
        
        try:
            nome, cpf, senha, cargo, data_entrada = self.view.ler_dados_usuario()
            if not nome or not cpf or not senha or not cargo or not data_entrada:
                self.view.exibir_mensagem(Idioma.t("usuario.campo_ausente"), False)
                return
            try:
                data_entrada = datetime.strptime(data_entrada, "%d/%m/%Y").date()
            except ValueError:
                self.view.exibir_mensagem(Idioma.t("usuario.erro_data_invalida"), False)
                return
            self.usuario_selecionado.atualizar_dados(nome, cpf, senha, cargo, data_entrada)
            self.dao.update(self.usuario_selecionado)
            self.get_all()
            self.view.exibir_mensagem(Idioma.t("usuario.atualizado_sucesso"))
        except IntegrityError:
            self.view.exibir_mensagem(Idioma.t("usuario.IntegrityError1062"), False)
            return
        except ValueError as e:
            self.view.exibir_mensagem(f"{Idioma.t('comum.erro_prefixo')}{str(e)}", False)

    def delete(self):
        if self.usuario_selecionado is None:
            self.view.exibir_mensagem(Idioma.t("usuario.selecione_da_lista"), False)
            return
        if not self.view.confirmar_exclusao():
            return
        try:
            sucesso = self.dao.delete(self.usuario_selecionado.id)
            if sucesso:
                self.usuario_selecionado = None
                self.view.limpar_campos()
                self.get_all()
                self.view.exibir_mensagem(Idioma.t("usuario.excluido_sucesso"))
            else:
                self.view.exibir_mensagem(Idioma.t("usuario.nao_encontrado"), False)
        except Exception as e:
            self.view.exibir_mensagem(f"{Idioma.t('usuario.erro_ao_excluir')}. {Idioma.t('comum.erro_prefixo')} {str(e)}", False)

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