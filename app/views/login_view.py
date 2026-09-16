import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox

class Login_View:
    def __init__(self, root, controller=None):
        self.root = root
        self.controller = controller
        self.criar_componentes()
        self.configurar_eventos()

    def criar_componentes(self):
        self.lbl_cpf = ttk.Label(self.root, text="CPF")
        self.lbl_cpf.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.txt_cpf = ttk.Entry(self.root, width=20)
        self.txt_cpf.grid(row=0, column=1, padx=10, pady=10)

        self.lbl_senha = ttk.Label(self.root, text="Senha")
        self.lbl_senha.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.txt_senha = ttk.Entry(self.root, width=20, show="*")
        self.txt_senha.grid(row=1, column=1, padx=10, pady=10)

        self.btn_entrar = ttk.Button(self.root, text="Entrar")
        self.btn_entrar.grid(row=2, column=0, columnspan=2, pady=10)

    def configurar_eventos(self):
        self.btn_entrar.config(command=self.controller.autenticar)

    def ler_credenciais(self):
        cpf = self.txt_cpf.get()
        senha = self.txt_senha.get()
        return cpf, senha

    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            Messagebox.showinfo("SysFarm", mensagem, parent=self.root)
        else:
            Messagebox.showerror("SysFarm", mensagem, parent=self.root)