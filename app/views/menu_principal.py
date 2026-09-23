# app/views/menu_view.py
import customtkinter as ctk
import ttkbootstrap as ttk
from PIL import Image

class Menu_View:
    def __init__(self, root, controller=None):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.carregar_imagens()
        self.criar_componentes()
        self._centralizar()

    def configurar_janela(self):
        self.root.title("SysFarm - Menu Principal")
        self.root.resizable(False, False)

    def _centralizar(self):
        self.root.update_idletasks()
        largura, altura = 1060, 490
        x = (self.root.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.root.winfo_screenheight() // 2) - (altura // 2)
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")


    def carregar_imagens(self):
        self.logo_image = ctk.CTkImage(
            light_image=Image.open("assets/logo_sys_farm_bemvindo.png"),
            size=(500, 400)
        )

    def criar_componentes(self):
        self.lbl_logo = ctk.CTkLabel(self.root, image=self.logo_image, text="")
        self.lbl_logo.place(relx=0.5, rely=0.45, anchor="center")

        self.btn_entrada = ctk.CTkButton(
        self.root, text="ENTRADA", width=220, height=55, corner_radius=28,
        fg_color="transparent", border_width=2, border_color="#FFFFFF",
        hover_color="#1e2a24", command=self.controller.abrir_entrada
        )
        self.btn_entrada.place(relx=0.15, rely=0.27, anchor="center")

        self.btn_saida = ctk.CTkButton(
            self.root, text="SAIDA", width=220, height=55, corner_radius=28,
            fg_color="transparent", border_width=2, border_color="#FFFFFF",
            hover_color="#1e2a24", command=self.controller.abrir_saida)
        
        self.btn_saida.place(relx=0.11, rely=0.50, anchor="center")

        self.btn_usuarios = ctk.CTkButton(
            self.root, text="USUARIOS", width=220, height=55, corner_radius=28,
            fg_color="transparent", border_width=2, border_color="#FFFFFF",
            hover_color="#1e2a24", command=self.controller.abrir_usuarios)
        
        self.btn_usuarios.place(relx=0.15, rely=0.73, anchor="center")



        self.btn_fornecedor = ctk.CTkButton(
            self.root, text="FORNECEDOR", width=220, height=55, corner_radius=28,
            fg_color="transparent", border_width=2, border_color="#FFFFFF",
            hover_color="#1e2a24", command=self.controller.abrir_fornecedores
        )
        self.btn_fornecedor.place(relx=0.84, rely=0.27, anchor="center")

        self.btn_medicamento = ctk.CTkButton(
            self.root, text="MEDICAMENTO", width=220, height=55, corner_radius=28,
            fg_color="transparent", border_width=2, border_color="#FFFFFF",
            hover_color="#1e2a24", command=self.controller.abrir_medicamentos
        )
        self.btn_medicamento.place(relx=0.88, rely=0.50, anchor="center")

        self.btn_estoque = ctk.CTkButton(
            self.root, text="ESTOQUE", width=220, height=55, corner_radius=28,
            fg_color="transparent", border_width=2, border_color="#FFFFFF",
            hover_color="#1e2a24", command=self.controller.abrir_estoque
        )
        self.btn_estoque.place(relx=0.84, rely=0.73, anchor="center")
        
        
