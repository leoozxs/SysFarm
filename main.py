# main.py
import ttkbootstrap as ttk
from app.core.database import Database


#componentes login
from app.views.login_view import Login_View
from app.controllers.login_controller import Login_Controller

#componentes menu
from app.views.menu_principal import Menu_View

#componentes entra/lote
from app.dao.entrada_dao import Entrada_DAO
from app.dao.lote_dao import Lote_DAO
from app.views.entrada_lote_view import Entrada_View
from app.controllers.entrada_lote_controller import Entrada_Controller

#componentes saida
from app.dao.saida_dao import Saida_DAO
from app.views.saida_view import Saida_View
from app.controllers.saida_controller import Saida_Controller

#componentes usuario
from app.dao.usuario_dao import Usuario_DAO
from app.views.usuario_view import Usuario_View
from app.controllers.usuario_controller import Usuario_Controller

#componentes fornecedor
from app.dao.fornecedor_dao import Fornecedor_DAO
from app.views.fornecedor_view import Fornecedor_View
from app.controllers.fornecedor_controller import Fornecedor_Controller

#componentes medicamento
from app.dao.medicamento_dao import Medicamento_DAO
from app.views.medicamento_view import Medicamento_View
from app.controllers.medicamento_controller import Medicamento_Controller

#componentes estoque
from app.dao.estoque_dao import Estoque_DAO
from app.views.estoque_view import Estoque_View
from app.controllers.estoque_controller import Estoque_Controller




class SysFarmApp:
    def __init__(self):
        self._database = Database()
        self._root = ttk.Window(themename="darkly")
        self._root.title("SysFarm")

        self._janela_entrada = None
        self._janela_saida = None
        self._janela_usuarios = None
        self._janela_fornecedores = None
        self._janela_medicamentos = None
        self._janela_estoque = None

        # --- DAOs ---
        self._dao_usuarios = Usuario_DAO(self._database)
        self._dao_medicamentos = Medicamento_DAO(self._database)
        self._dao_fornecedores = Fornecedor_DAO(self._database)
        self._dao_lotes = Lote_DAO(self._database)
        self._dao_entradas = Entrada_DAO(self._database)
        self._dao_saidas = Saida_DAO(self._database)
        self._dao_estoque = Estoque_DAO(self._database)

        # --- Controllers, todos criados já no início, com view=None ---
        self._ctrl_login = Login_Controller(view=None, usuario_dao=self._dao_usuarios, ao_logar_com_sucesso=self._abrir_menu)
        self._ctrl_entrada = Entrada_Controller(view=None, lote_dao=self._dao_lotes, entrada_dao=self._dao_entradas, estoque_dao=self._dao_estoque,
                                                  medicamento_dao=self._dao_medicamentos, fornecedor_dao=self._dao_fornecedores,
                                                  usuario_dao=self._dao_usuarios)
        self._ctrl_saida = Saida_Controller(view=None, lote_dao=self._dao_lotes, saida_dao=self._dao_saidas, estoque_dao=self._dao_estoque,usuario_dao=self._dao_usuarios)
        self._ctrl_usuarios = Usuario_Controller(view=None, dao=self._dao_usuarios)
        self._ctrl_fornecedores = Fornecedor_Controller(view=None, dao=self._dao_fornecedores)
        self._ctrl_medicamentos = Medicamento_Controller(view=None, dao=self._dao_medicamentos)
        self._ctrl_estoque = Estoque_Controller(view=None, dao=self._dao_estoque, abrir_entrada=self.abrir_entrada, abrir_saida=self.abrir_saida)

        # --- Só a tela de Login abre primeiro; o resto começa fechado ---
        self._ctrl_login.view = Login_View(self._root, self._ctrl_login)

    def _abrir_menu(self, usuario_logado):
        for widget in self._root.winfo_children():
            widget.destroy()
        self._root.geometry("1060x490")
        Menu_View(self._root, controller=self)  # o próprio App vira o "controller" do Menu

    def _abrir_janela(self, atributo_janela, classe_view, controller):
        janela_existente = getattr(self, atributo_janela)
        if janela_existente is not None and janela_existente.winfo_exists():
            janela_existente.lift()
            janela_existente.focus_force()
            return
        janela = ttk.Toplevel(self._root)
        setattr(self, atributo_janela, janela)
        controller.view = classe_view(janela, controller)
        controller.view.iniciar()

    def abrir_entrada(self):
        self._abrir_janela("_janela_entrada", Entrada_View, self._ctrl_entrada)

    def abrir_saida(self):
        self._abrir_janela("_janela_saida", Saida_View, self._ctrl_saida)

    def abrir_usuarios(self):
        self._abrir_janela("_janela_usuarios", Usuario_View, self._ctrl_usuarios)

    def abrir_fornecedores(self):
        self._abrir_janela("_janela_fornecedores", Fornecedor_View, self._ctrl_fornecedores)

    def abrir_medicamentos(self):
        self._abrir_janela("_janela_medicamentos", Medicamento_View, self._ctrl_medicamentos)

    def abrir_estoque(self):
        self._abrir_janela("_janela_estoque", Estoque_View, self._ctrl_estoque)

    def run(self):
        self._root.mainloop()


if __name__ == "__main__":
    app = SysFarmApp()
    app.run()
