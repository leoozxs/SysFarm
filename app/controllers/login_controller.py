from app.core.idioma import Idioma

class Login_Controller:
    def __init__(self, view, usuario_dao, ao_logar_com_sucesso):
        self.view = view
        self.usuario_dao = usuario_dao
        self.ao_logar_com_sucesso = ao_logar_com_sucesso

    def autenticar(self):
        cpf, senha = self.view.ler_credenciais()

        if not cpf or not senha:
            self.view.exibir_mensagem(Idioma.t("login.campos_obrigatorios"), False)
            return
        usuario = self.usuario_dao.autenticar(cpf, senha)
        if usuario is None:
            self.view.exibir_mensagem(Idioma.t("login.credenciais_invalidas"), False)
            return
        self.ao_logar_com_sucesso()