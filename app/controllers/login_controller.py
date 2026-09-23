class Login_Controller:
    def __init__(self, view, usuario_dao, ao_logar_com_sucesso):
        self.view = view
        self.usuario_dao = usuario_dao
        self.ao_logar_com_sucesso = ao_logar_com_sucesso

    def autenticar(self):
        cpf, senha = self.view.ler_credenciais()

        if not cpf or not senha:
            self.view.exibir_mensagem(
                "Preencha CPF e senha.",
                False
            )
            return

        usuario, erro = self.usuario_dao.autenticar(cpf, senha)

        if erro == "cpf":
            self.view.exibir_mensagem(
                "CPF não encontrado.",
                False
            )
            return

        if erro == "senha":
            self.view.exibir_mensagem(
                "Senha incorreta.",
                False
            )
            return

        if erro == "inativo":
            self.view.exibir_mensagem(
                "Este usuário está inativo.",
                False
            )
            return

        self.ao_logar_com_sucesso(usuario)