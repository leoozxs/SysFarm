import ttkbootstrap as ttk
import customtkinter as ctk
from ttkbootstrap.dialogs import Messagebox
from PIL import Image

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
        largura, altura = 400, 450
        x = (self.root.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.root.winfo_screenheight() // 2) - (altura // 2)
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")
 

    def configurar_janela(self):
        self.root.title("Login SysFarm")
        self.root.resizable(False, False)

    def criar_componentes(self):
        
        #pegar a imagem no repositório e colocar em uma variavel
        self.icone_usuario = ctk.CTkImage(light_image=Image.open("assets/icone_usuario.png"),size=(18, 18))
        self.icone_cadeado = ctk.CTkImage(light_image=Image.open("assets/icone_cadeado.png"),size=(28, 25))
        self.icone_sistema = ctk.CTkImage(light_image=Image.open("assets/logo_sys_farm.png"),size=(250, 170))
        
        self.lbl_icone_sistema = ctk.CTkLabel(self.root, image=self.icone_sistema, text="")
        self.lbl_icone_sistema.place(relx=0.2, rely=0.25, anchor="w")
        
        self.lbl_titulo = ttk.Label(self.root, text="━━━━ Login ━━━━", font=("Aptos",10,"bold"))
        self.lbl_titulo.place(relx= 0.5, rely= 0.5, anchor="center")
        
        self.txt_cpf = ctk.CTkEntry(self.root, width=180, placeholder_text="CPF", height=35, justify="center", corner_radius=0)
        self.txt_cpf.place(relx= 0.5, rely= 0.6, anchor="center")
        
        self.txt_senha = ctk.CTkEntry(self.root, width=180, show="*", placeholder_text="Senha", height=35, justify="center", corner_radius=0)
        self.txt_senha.place(relx= 0.5, rely= 0.7, anchor="center")
        
        
        #colocar a imagem no entry
        self.lbl_icone_usuario = ctk.CTkLabel(self.txt_cpf, image=self.icone_usuario, text="")
        self.lbl_icone_usuario.place(relx=0.85, rely=0.5, anchor="w")
        
        self.lbl_icone_cadeado = ctk.CTkLabel(self.txt_senha, image=self.icone_cadeado, text="")
        self.lbl_icone_cadeado.place(relx=0.83, rely=0.48, anchor="w")
        
        
        #botao
        self.btn_entrar = ttk.Button(self.root,text = "Entrar",width = 25, bootstyle="success-outline", cursor="hand2") 
        self.btn_entrar.place(relx = 0.5, rely = 0.8, anchor="center")

    def configurar_eventos(self):
        self.btn_entrar.configure(command=self.controller.autenticar)

    def ler_credenciais(self):
        cpf = self.txt_cpf.get()
        senha = self.txt_senha.get()
        return cpf, senha

    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            Messagebox.show_info("SysFarm", mensagem, parent=self.root)
        else:
            Messagebox.show_error("SysFarm", mensagem, parent=self.root)
            

if __name__ == "__main__":
    class ControllerFake:
        def new(self): print("novo")
        def save(self): print("salvar")
        def autenticar(self): print("Autenticado")

    janela = ttk.Window(themename="darkly")
    view = Login_View(janela, controller=ControllerFake())
    janela.mainloop()
    