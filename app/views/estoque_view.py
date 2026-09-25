import ttkbootstrap as ttk

class Estoque_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()
        self._centralizar()

    def configurar_janela(self):
        self.root.title("Visão Geral do Estoque")
        self.root.resizable(False, False)

    def _centralizar(self):
        self.root.update_idletasks()
        largura, altura = 700, 460
        x = (self.root.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.root.winfo_screenheight() // 2) - (altura // 2)
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")

    def criar_componentes(self):
        self.lbl_titulo = ttk.Label(self.root, text="Visão Geral do Estoque", font=("Courier New", 20, "bold"))
        self.lbl_titulo.grid(row=0, column=0, columnspan=4, pady=10)
        
        self.tbl_estoque = ttk.Treeview(self.root, height=20, bootstyle="light")
        self.tbl_estoque.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

        self.btn_atualizar = ttk.Button(self.root, text="Atualizar", width=15, bootstyle="info-outline")
        self.btn_atualizar.grid(row=2, column=0, padx=5, pady=5)

        self.btn_entrada = ttk.Button(self.root, text="Registrar Entrada", width=18, bootstyle="success-outline")
        self.btn_entrada.grid(row=2, column=1, padx=5, pady=5)

        self.btn_saida = ttk.Button(self.root, text="Registrar Saída", width=18, bootstyle="warning-outline")
        self.btn_saida.grid(row=2, column=2, padx=5, pady=5)

        self.btn_fechar = ttk.Button(self.root, text="Fechar", width=15, bootstyle="secondary-outline")
        self.btn_fechar.grid(row=2, column=3, padx=5, pady=5)
        


    def configurar_treeview(self):
        self.tbl_estoque["columns"] = ("medicamento", "lote", "fornecedor", "validade", "qtd", "status")
        self.tbl_estoque.column("#0", width=0, stretch=False)
        self.tbl_estoque.column("medicamento", width=180, anchor="w", stretch=False)
        self.tbl_estoque.column("lote", width=100, anchor="center", stretch=False)
        self.tbl_estoque.column("fornecedor", width=150, anchor="w", stretch=False)
        self.tbl_estoque.column("validade", width=90, anchor="center", stretch=False)
        self.tbl_estoque.column("qtd", width=60, anchor="center", stretch=False)
        self.tbl_estoque.column("status", width=100, anchor="center", stretch=False)
        
        
        
        self.tbl_estoque.heading("medicamento", text="MEDICAMENTO")
        self.tbl_estoque.heading("lote", text="LOTE")
        self.tbl_estoque.heading("fornecedor", text="FORNECEDOR")
        self.tbl_estoque.heading("validade", text="VALIDADE")
        self.tbl_estoque.heading("qtd", text="QTD")
        self.tbl_estoque.heading("status", text="STATUS")

    def limpar_treeview(self):
        for item in self.tbl_estoque.get_children():
            self.tbl_estoque.delete(item)

    def exibir_estoque(self, itens):
        self.limpar_treeview()
        for i in itens:
            self.tbl_estoque.insert("", "end", values=(
                i.medicamento.nome, i.lote._numero_lote, i.lote._fornecedor.nome,
                i.validade, i.qtd_atual, i.status
            ))
    

    def configurar_eventos(self):
        self.btn_atualizar.config(command=self.controller.listar)
        self.btn_entrada.config(command=self.controller.abrir_entrada)
        self.btn_saida.config(command=self.controller.abrir_saida)
        self.btn_fechar.config(command=self.fechar)

    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.listar()
