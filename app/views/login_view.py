import ttkbootstrap as ttk
import customtkinter as ctk
from ttkbootstrap.dialogs import Messagebox

class Login_View:
    def __init__(self, root, controller=None):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_eventos()
        self._centralizar()

    def _centralizar(self):
        self.root.update_idletasks()
        largura, altura = 250, 220
        x = (self.root.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.root.winfo_screenheight() // 2) - (altura // 2)
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")
 

    def configurar_janela(self):
        self.root.title("Login SysFarm")
        self.root.resizable(False, False)

    def criar_componentes(self):
        
        self.lbl_titulo = ttk.Label(self.root, text="Login SysFarm", font=("Courier New",15,"bold"))
        self.lbl_titulo.place(relx= 0.2, rely= 0.09)
        
        self.lbl_cpf = ttk.Label(self.root, text="CPF")
        self.lbl_cpf.place(relx= 0.1, rely= 0.28)
        self.txt_cpf = ttk.Entry(self.root, width=20)
        self.txt_cpf.place(relx= 0.26, rely= 0.28)

        self.lbl_senha = ttk.Label(self.root, text="Senha")
        self.lbl_senha.place(relx= 0.08, rely= 0.52)
        self.txt_senha = ttk.Entry(self.root, width=20, show="*")
        self.txt_senha.place(relx= 0.26, rely= 0.5)

        self.btn_entrar = ttk.Button(self.root,text = "Entrar",width = 15, bootstyle="danger-outline", cursor="hand1") 
        self.btn_entrar.place(relx = 0.5, rely = 0.78, anchor="center")

    def configurar_eventos(self):
        self.btn_entrar.configure(command=self.controller.autenticar)

    def ler_credenciais(self):
        cpf = self.txt_cpf.get()
        senha = self.txt_senha.get()
        return cpf, senha

    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            Messagebox.showinfo("SysFarm", mensagem, parent=self.root)
        else:
            Messagebox.showerror("SysFarm", mensagem, parent=self.root)
            

if __name__ == "__main__":
    import ttkbootstrap as ttk

    class ControllerFake:
        def new(self):
            print("Novo clicado")

        def save(self):
            print("Salvar clicado")

        def update(self):
            print("Alterar clicado")

        def delete(self):
            print("Excluir clicado")

        def selecionar_usuario(self, event):
            print("Linha selecionada")
        
        def autenticar(self):
            print("Autenticado!")

    janela = ttk.Window(themename="darkly")
    view = Login_View(janela, controller=ControllerFake())
    janela.mainloop()