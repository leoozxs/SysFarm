import ttkbootstrap as ttk
import customtkinter as ctk
from ttkbootstrap.dialogs import Messagebox
from PIL import Image
from app.core.idioma import Idioma

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
        self.root.title(Idioma.t("login.janela_titulo"))
        self.root.resizable(False, False)

    def criar_componentes(self):
        
        #pegar a imagem no repositório e colocar em uma variavel
        self.icone_usuario = ctk.CTkImage(light_image=Image.open("assets/icone_usuario.png"),size=(18, 18))
        self.icone_cadeado = ctk.CTkImage(light_image=Image.open("assets/icone_cadeado.png"),size=(28, 25))
        self.icone_sistema = ctk.CTkImage(light_image=Image.open("assets/logo_sys_farm.png"),size=(250, 170))
        
        self.lbl_icone_sistema = ctk.CTkLabel(self.root, image=self.icone_sistema, text="")
        self.lbl_icone_sistema.place(relx=0.2, rely=0.25, anchor="w")
        
        self.lbl_titulo = ttk.Label(self.root, text=Idioma.t("login.titulo"), font=("Aptos",10,"bold"))
        self.lbl_titulo.place(relx= 0.5, rely= 0.5, anchor="center")
        
        self.txt_cpf = ctk.CTkEntry(self.root, width=180, placeholder_text=Idioma.t("login.cpf"), height=35, justify="center", corner_radius=0)
        self.txt_cpf.place(relx= 0.5, rely= 0.6, anchor="center")
        
        self.txt_senha = ctk.CTkEntry(self.root, width=180, show="*", placeholder_text=Idioma.t("login.senha"), height=35, justify="center", corner_radius=0)
        self.txt_senha.place(relx= 0.5, rely= 0.7, anchor="center")
        
        self.cmb_idioma = ctk.CTkComboBox(self.root, width=180, values=list(Idioma.NOMES.values()),justify="center", height=35, corner_radius=0, state="readonly",
        command=self.mudar_idioma)
        self.cmb_idioma.place(relx = 0.5, rely = 0.8, anchor="center")
        self.cmb_idioma.set(Idioma.nome_atual())
        
        
        #colocar a imagem no entry
        self.lbl_icone_usuario = ctk.CTkLabel(self.txt_cpf, image=self.icone_usuario, text="")
        self.lbl_icone_usuario.place(relx=0.85, rely=0.5, anchor="w")
        
        self.lbl_icone_cadeado = ctk.CTkLabel(self.txt_senha, image=self.icone_cadeado, text="")
        self.lbl_icone_cadeado.place(relx=0.83, rely=0.48, anchor="w")
        
        
        #botao
        self.btn_entrar = ttk.Button(self.root,text = Idioma.t("login.entrar"),width = 25, bootstyle="success-outline", cursor="hand2") 
        self.btn_entrar.place(relx = 0.5, rely = 0.9, anchor="center")

    def configurar_eventos(self):

        self.btn_entrar.configure(command=self.controller.autenticar)
        self.txt_cpf.bind("<Return>", self.on_enter)
        self.txt_senha.bind("<Return>", self.on_enter)
    
    def on_enter(self, event=None):
        self.controller.autenticar()

    def ler_credenciais(self):
        cpf = self.txt_cpf.get()
        senha = self.txt_senha.get()
        return cpf, senha
    
    def mudar_idioma(self, nome_selecionado):
        Idioma.definir(Idioma.codigo_por_nome(nome_selecionado))
        self.atualizar_textos()

    def atualizar_textos(self):
        self.root.title(Idioma.t("login.janela_titulo"))
        self.lbl_titulo.configure(text=Idioma.t("login.titulo"))
        self.txt_cpf.configure(placeholder_text=Idioma.t("login.cpf"))
        self.txt_senha.configure(placeholder_text=Idioma.t("login.senha"))
        self.btn_entrar.configure(text=Idioma.t("login.entrar"))

    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            Messagebox.show_info(mensagem,"SysFarm", parent=self.root)
        else:
            Messagebox.show_error(mensagem,"SysFarm", parent=self.root)
            
            
if __name__ == "__main__":

    class ControllerFake:

        def abrir_medicamentos(self): print("medicamento")

        def abrir_fornecedores(self): print("fornecedor")

        def abrir_estoque(self): print("estoque")

        def abrir_entrada(self): print("entrada")

        def abrir_saida(self): print("saida")

        def abrir_usuarios(self): print("usuarios")
        
        def autenticar(self): print("usuarios")
 
    janela = ttk.Window(themename="darkly")

    view = Login_View(janela, controller=ControllerFake())

    janela.mainloop()
 
            
