# app/views/menu_view.py
import customtkinter as ctk
from PIL import Image

class Menu_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.carregar_imagens()
        self.criar_componentes()
        self._centralizar()

    def configurar_janela(self):
        self.root.title("SysFarm - Menu Principal")
        self.root.resizable(True,True)
        self.root.minsize(1650, 870)
        
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
        self.icone_medicamento = ctk.CTkImage(light_image=Image.open("assets/icone_medicamento.png"), size=(200, 200))
        self.icone_fornecedor = ctk.CTkImage(light_image=Image.open("assets/icone_fornecedor.png"), size=(200, 200))
        self.icone_estoque = ctk.CTkImage(light_image=Image.open("assets/icone_estoque.png"), size=(128, 128))
        self.icone_entrada = ctk.CTkImage(light_image=Image.open("assets/icone_entrada.png"), size=(128, 128))
        self.icone_saida = ctk.CTkImage(light_image=Image.open("assets/icone_saida.png"), size=(128, 128))
        self.icone_usuarios = ctk.CTkImage(light_image=Image.open("assets/icone_usuario.png"), size=(128, 128))

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
        # Logo + nome, centralizados
        self.lbl_logo = ctk.CTkLabel(self.root, image=self.logo_image, text="")
        self.lbl_logo.place(relx=0.5, rely=0.28, anchor="center")

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
            relx=0.60, rely=0.78, relwidth=0.15, relheight=0.34
        )
        self.card_saida = self.criar_card(
            "SAÍDA", self.icone_saida, self.controller.abrir_saida,
            relx=0.77, rely=0.78, relwidth=0.15, relheight=0.34
        )
        self.card_usuarios = self.criar_card(
            "USUÁRIOS", self.icone_usuarios, self.controller.abrir_usuarios,
            relx=0.43, rely=0.78, relwidth=0.15, relheight=0.34
        )