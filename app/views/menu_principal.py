# app/views/menu_view.py
import customtkinter as ctk
from PIL import Image

class Menu_View:
    def __init__(self, root, controller=None):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.carregar_imagens()
        self.criar_componentes()

    def configurar_janela(self):
        self.root.title("SysFarm - Menu Principal")
        self.root.geometry("1040x440")
        self.root.resizable(False, False)

    def carregar_imagens(self):
        self.logo_image = ctk.CTkImage(
            light_image=Image.open("app/assets/logo_sysfarm.png"),
            size=(160, 160)
        )

    def criar_componentes(self):
        self.lbl_logo = ctk.CTkLabel(self.root, image=self.logo_image, text="")
        self.lbl_logo.place(relx=0.5, rely=0.30, anchor="center")

        self.lbl_nome = ctk.CTkLabel(self.root, text="Sys.Farm", font=("Courier New", 32, "bold"))
        self.lbl_nome.place(relx=0.5, rely=0.55, anchor="center")

        self.lbl_bemvindo = ctk.CTkLabel(self.root, text="Bem-vindo", font=("Courier New", 16, "bold"))
        self.lbl_bemvindo.place(relx=0.5, rely=0.63, anchor="center")

        self.btn_entrada = ctk.CTkButton(
            self.root, text="ENTRADA", width=220, height=55, corner_radius=12,
            fg_color="transparent", border_width=2, border_color="#FFFFFF",
            hover_color="#1e2a24", command=self.controller.abrir_entrada
        )
        self.btn_entrada.place(relx=0.24, rely=0.27, anchor="center")

        self.btn_saida = ctk.CTkButton(
            self.root, text="SAIDA", width=220, height=55, corner_radius=12,
            fg_color="transparent", border_width=2, border_color="#FFFFFF",
            hover_color="#1e2a24", command=self.controller.abrir_saida
        )
        self.btn_saida.place(relx=0.20, rely=0.50, anchor="center")

        self.btn_usuarios = ctk.CTkButton(
            self.root, text="USUARIOS", width=220, height=55, corner_radius=12,
            fg_color="transparent", border_width=2, border_color="#FFFFFF",
            hover_color="#1e2a24", command=self.controller.abrir_usuarios
        )
        self.btn_usuarios.place(relx=0.24, rely=0.73, anchor="center")

        self.btn_fornecedor = ctk.CTkButton(
            self.root, text="FORNECEDOR", width=220, height=55, corner_radius=12,
            fg_color="transparent", border_width=2, border_color="#FFFFFF",
            hover_color="#1e2a24", command=self.controller.abrir_fornecedor
        )
        self.btn_fornecedor.place(relx=0.76, rely=0.27, anchor="center")

        self.btn_medicamento = ctk.CTkButton(
            self.root, text="MEDICAMENTO", width=220, height=55, corner_radius=12,
            fg_color="transparent", border_width=2, border_color="#FFFFFF",
            hover_color="#1e2a24", command=self.controller.abrir_medicamento
        )
        self.btn_medicamento.place(relx=0.80, rely=0.50, anchor="center")

        self.btn_estoque = ctk.CTkButton(
            self.root, text="ESTOQUE", width=220, height=55, corner_radius=12,
            fg_color="transparent", border_width=2, border_color="#FFFFFF",
            hover_color="#1e2a24", command=self.controller.abrir_estoque
        )
        self.btn_estoque.place(relx=0.76, rely=0.73, anchor="center")