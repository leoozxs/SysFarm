# app/views/menu_view.py
import ttkbootstrap as ttk
import customtkinter as ctk
from PIL import Image

class Menu_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.tema_atual = "escuro" 
        self.configurar_janela()
        self.carregar_imagens()
        self.criar_componentes()

    def configurar_janela(self):
        self.root.title("SysFarm - Menu Principal")
        self.root.resizable(True,True)
        self.root.minsize(1650, 800)
        
    def _centralizar(self):
        self.root.update_idletasks()
        largura, altura = 1850, 920
        x = (self.root.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.root.winfo_screenheight() // 2) - (altura // 2)
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")
    
    def carregar_imagens(self):
        self.logo_image = ctk.CTkImage(
            light_image=Image.open("assets/logo_sys_farm_bemvindo.png"),
            size=(650, 600)
        )
        
        self.icone_medicamento = ctk.CTkImage(
            light_image=Image.open("assets/icone_medicamento_claro.png"),
            dark_image=Image.open("assets/icone_medicamento.png"), 
            size=(200, 200)
            )
        
        self.icone_fornecedor = ctk.CTkImage(
            light_image=Image.open("assets/icone_fornecedor_claro.png"),
            dark_image=Image.open("assets/icone_fornecedor.png"), 
            size=(200, 200)
            )
        
        self.icone_estoque = ctk.CTkImage(
            light_image=Image.open("assets/icone_estoque_claro.png"),
            dark_image=Image.open("assets/icone_estoque.png"), 
            size=(128, 128)
            )
        
        self.icone_entrada = ctk.CTkImage(
            light_image=Image.open("assets/icone_entrada_claro.png"),
            dark_image=Image.open("assets/icone_entrada.png"), 
            size=(128, 128)
            )
        
        self.icone_saida = ctk.CTkImage(
            light_image=Image.open("assets/icone_saida_claro.png"),
            dark_image=Image.open("assets/icone_saida.png"), 
            size=(128, 128)
            )
        
        self.icone_usuarios = ctk.CTkImage(
            light_image=Image.open("assets/icone_usuario_claro.png"),
            dark_image=Image.open("assets/icone_usuario.png"), 
            size=(128, 128)
            )
        
        # icones do próprio botão de alternar tema
        self.icone_sol = ctk.CTkImage(light_image=Image.open("assets/icone_sol.png"), size=(28, 28))
        self.icone_lua = ctk.CTkImage(light_image=Image.open("assets/icone_lua.png"), size=(28, 28))
        

    def criar_card(self, texto, imagem, comando, relx, rely, relwidth, relheight):
        card = ctk.CTkButton(
            self.root,
            text=texto,
            image=imagem,
            compound="top",
            font=("Courier New", 14, "bold"),
            fg_color="transparent",
            border_width=2,
            border_color="#FFFFFF",
            hover_color="#1e2a24",
            corner_radius=12,
            command=comando
        )
        card.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight, anchor="center")
        return card

    def criar_componentes(self):
        # Botão de alternar tema, canto superior direito
        self.btn_tema = ctk.CTkButton(
            self.root,
            text="",
            image=self.icone_sol,  # começa mostrando o sol (ação: ir pro modo claro)
            width=40,
            height=40,
            fg_color="transparent",
            hover_color="#1e2a24",
            corner_radius=20,
            command=self.alternar_tema
        )
        self.btn_tema.place(relx=0.97, rely=0.04, anchor="center")

        # Logo + nome, centralizados
        self.lbl_logo = ctk.CTkLabel(self.root, image=self.logo_image, text="")
        self.lbl_logo.place(relx=0.5, rely=0.28, anchor="center")

        self.lbl_nome = ctk.CTkLabel(self.root, text="Sys.Farm", font=("Courier New", 34, "bold"))
        self.lbl_nome.place(relx=0.5, rely=0.46, anchor="center")

        self.lbl_bemvindo = ctk.CTkLabel(self.root, text="Bem-vindo", font=("Courier New", 16, "bold"))
        self.lbl_bemvindo.place(relx=0.5, rely=0.52, anchor="center")

        # Linha de cima
        self.card_medicamento = self.criar_card(
            "MEDICAMENTO", self.icone_medicamento, self.controller.abrir_medicamentos,
            relx=0.15, rely=0.32, relwidth=0.16, relheight=0.40
        )
        self.card_fornecedor = self.criar_card(
            "FORNECEDOR", self.icone_fornecedor, self.controller.abrir_fornecedores,
            relx=0.85, rely=0.32, relwidth=0.16, relheight=0.40
        )

        # Linha de baixo
        self.card_estoque = self.criar_card(
            "ESTOQUE", self.icone_estoque, self.controller.abrir_estoque,
            relx=0.26, rely=0.78, relwidth=0.15, relheight=0.34
        )
        self.card_entrada = self.criar_card(
            "ENTRADA", self.icone_entrada, self.controller.abrir_entrada,
            relx=0.43, rely=0.78, relwidth=0.15, relheight=0.34
        )
        self.card_saida = self.criar_card(
            "SAÍDA", self.icone_saida, self.controller.abrir_saida,
            relx=0.60, rely=0.78, relwidth=0.15, relheight=0.34
        )
        self.card_usuarios = self.criar_card(
            "USUÁRIOS", self.icone_usuarios, self.controller.abrir_usuarios,
            relx=0.77, rely=0.78, relwidth=0.15, relheight=0.34
        )

    def alternar_tema(self):
        if self.tema_atual == "escuro":
            ttk.Style().theme_use("flatly")
            ctk.set_appearance_mode("light")
            self.btn_tema.configure(image=self.icone_lua)  # agora mostra lua (ação: voltar pro escuro)
            self.tema_atual = "claro"
        else:
            ttk.Style().theme_use("darkly")
            ctk.set_appearance_mode("dark")
            self.btn_tema.configure(image=self.icone_sol)
            self.tema_atual = "escuro"


if __name__ == "__main__":
    class ControllerFake:
        def abrir_medicamentos(self): print("medicamento")
        def abrir_fornecedores(self): print("fornecedor")
        def abrir_estoque(self): print("estoque")
        def abrir_entrada(self): print("entrada")
        def abrir_saida(self): print("saida")
        def abrir_usuarios(self): print("usuarios")

    janela = ttk.Window(themename="darkly")
    view = Menu_View(janela, controller=ControllerFake())
    janela.mainloop()