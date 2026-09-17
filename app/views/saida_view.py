import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox

class Saida_View:
    def __init__(self, root, controller=None):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()
        self._centralizar()

    def configurar_janela(self):
        self.root.title("Registrar Saída")
        self.root.resizable(False, False)

    def _centralizar(self):
        self.root.update_idletasks()
        largura, altura = 350, 550
        x = (self.root.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.root.winfo_screenheight() // 2) - (altura // 2)
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")
    
    def criar_componentes(self):
        self.lbl_titulo = ttk.Label(self.root, text="Saída", font=("Courier New", 20, "bold"))
        self.lbl_titulo.place(relx=0.5, rely=0.05, anchor="center")

        self.lbl_lote = ttk.Label(self.root, text="Serial Lote", font=("Courier New", 13, "bold"))
        self.lbl_lote.place(relx=0.5, rely=0.15, anchor="center")
        self.cmb_lote = ttk.Combobox(self.root, width=18)
        self.cmb_lote.place(relx=0.5, rely=0.20, anchor="center")

        self.lbl_tipo_saida = ttk.Label(self.root, text="Tipo de Saída", font=("Courier New", 13, "bold"))
        self.lbl_tipo_saida.place(relx=0.5, rely=0.43, anchor="center")
        self.cmb_tipo_saida = ttk.Combobox(self.root, width=15)
        self.cmb_tipo_saida.place(relx=0.5, rely=0.50, anchor="center")

        self.lbl_qtd_saida = ttk.Label(self.root, text="Quantidade de Saída", font=("Courier New", 13, "bold"))
        self.lbl_qtd_saida.place(relx=0.5, rely=0.29, anchor="center")
        self.txt_qtd_saida = ttk.Entry(self.root, width=10)
        self.txt_qtd_saida.place(relx=0.5, rely=0.35, anchor="center")

        self.lbl_data_saida = ttk.Label(self.root, text="Data de Saída", font=("Courier New", 13, "bold"))
        self.lbl_data_saida.place(relx=0.5, rely=0.60, anchor="center")
        self.txt_data_saida = ttk.DateEntry(self.root, width=11, date_format="%d/%m/%Y", bootstyle="light-outline")
        self.txt_data_saida.place(relx=0.5, rely=0.65, anchor="center")

        self.btn_ok = ttk.Button(self.root, text="OK", width=8, bootstyle="success-outline")
        self.btn_ok.place(relx=0.3, rely=0.75, anchor="center")

        self.btn_x = ttk.Button(self.root, text="X", width=8, bootstyle="danger-outline")
        self.btn_x.place(relx=0.6, rely=0.75, anchor="center")

    def configurar_eventos(self):
        pass
    
    def configurar_treeview(self):
        pass

    def configurar_eventos(self):
        pass






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
    view = Saida_View(janela, controller=ControllerFake())
    janela.mainloop()