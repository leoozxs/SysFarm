import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from app.core.idioma import Idioma

class Entrada_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()
        self._centralizar()

    def configurar_janela(self):
        self.root.title(Idioma.t("entrada.janela_titulo"))
        self.root.resizable(False, False)

    def _centralizar(self):
        self.root.update_idletasks()
        largura, altura = 695, 630
        x = (self.root.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.root.winfo_screenheight() // 2) - (altura // 2)
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")

    def criar_componentes(self):
        self.lbl_titulo = ttk.Label(self.root, text=Idioma.t("entrada.titulo"), font=("Courier New", 20, "bold"))
        self.lbl_titulo.grid(row=0, column=0, columnspan=4, pady=10)

        self.frm_dados = ttk.Labelframe(self.root, text=Idioma.t("entrada.dados_frame"), labelanchor="n")
        self.frm_dados.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky="ew")

        self.lbl_medicamento = ttk.Label(self.frm_dados, text=Idioma.t("entrada.medicamento"))
        self.lbl_medicamento.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.cmb_medicamento = ttk.Combobox(self.frm_dados, width=25, state="readonly")
        self.cmb_medicamento.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.lbl_fornecedor = ttk.Label(self.frm_dados, text=Idioma.t("entrada.fornecedor"))
        self.lbl_fornecedor.grid(row=0, column=2, padx=10, pady=10, sticky="w")
        self.cmb_fornecedor = ttk.Combobox(self.frm_dados, width=25, state="readonly")
        self.cmb_fornecedor.grid(row=0, column=3, padx=10, pady=10, sticky="w")

        self.lbl_numero_lote = ttk.Label(self.frm_dados, text=Idioma.t("entrada.numero_lote"))
        self.lbl_numero_lote.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.txt_numero_lote = ttk.Entry(self.frm_dados, width=20)
        self.txt_numero_lote.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.lbl_validade = ttk.Label(self.frm_dados, text=Idioma.t("entrada.validade"))
        self.lbl_validade.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.txt_validade = ttk.DateEntry(self.frm_dados, width=11, date_format="%d/%m/%Y", bootstyle="dark")
        self.txt_validade.grid(row=1, column=3, padx=10, pady=10, sticky="w")

        self.lbl_qtd_entrada = ttk.Label(self.frm_dados, text=Idioma.t("entrada.qtd"))
        self.lbl_qtd_entrada.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.txt_qtd_entrada = ttk.Entry(self.frm_dados, width=10)
        self.txt_qtd_entrada.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.lbl_usuario = ttk.Label(self.frm_dados, text=Idioma.t("entrada.usuario_responsavel"))
        self.lbl_usuario.grid(row=2, column=2, padx=10, pady=10, sticky="w")
        self.cmb_usuario = ttk.Combobox(self.frm_dados, width=25, state="readonly")
        self.cmb_usuario.grid(row=2, column=3, padx=10, pady=10, sticky="w")

        self.frm_botoes = ttk.Frame(self.frm_dados)
        self.frm_botoes.grid(row=3, column=0, columnspan=4, pady=10)

        self.btn_novo = ttk.Button(self.frm_botoes, text=Idioma.t("comum.novo"), width=15, bootstyle="primary-outline")
        self.btn_novo.grid(row=0, column=0, padx=5)
        self.btn_salvar = ttk.Button(self.frm_botoes, text=Idioma.t("comum.salvar"), width=15, bootstyle="success-outline")
        self.btn_salvar.grid(row=0, column=1, padx=5)
        self.btn_fechar = ttk.Button(self.frm_botoes, text=Idioma.t("comum.fechar"), width=15, bootstyle="secondary-outline")
        self.btn_fechar.grid(row=0, column=2, padx=5)
        
        self.lbl_registro_de_entradas = ttk.Label(self.root, text=Idioma.t("entrada.registro_entradas"), font=("Courier New", 12, "bold"))
        self.lbl_registro_de_entradas.grid(row=2, column=0, columnspan=4)

        self.tbl_entradas = ttk.Treeview(self.root, height=18, bootstyle="light")
        self.tbl_entradas.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

    def configurar_treeview(self):
        self.tbl_entradas["columns"] = ("id", "lote", "medicamento", "fornecedor", "qtd", "validade", "data de entrada")
        self.tbl_entradas.column("#0", width=0, stretch=False)
        self.tbl_entradas.column("id", width=40, anchor="center", stretch=False)
        self.tbl_entradas.column("lote", width=90, anchor="center", stretch=False)
        self.tbl_entradas.column("medicamento", width=140, anchor="w", stretch=False)
        self.tbl_entradas.column("fornecedor", width=140, anchor="w", stretch=False)
        self.tbl_entradas.column("qtd", width=60, anchor="center", stretch=False)
        self.tbl_entradas.column("validade", width=90, anchor="center", stretch=False)
        self.tbl_entradas.column("data de entrada", width=110, anchor="center", stretch=False)
        
        
        self.tbl_entradas.heading("id", text=Idioma.t("comum.id"))
        self.tbl_entradas.heading("lote", text=Idioma.t("entrada.lote"))
        self.tbl_entradas.heading("medicamento", text=Idioma.t("entrada.medicamento"))
        self.tbl_entradas.heading("fornecedor", text=Idioma.t("entrada.fornecedor"))
        self.tbl_entradas.heading("qtd", text=Idioma.t("entrada.qtd_entrada"))
        self.tbl_entradas.heading("validade", text=Idioma.t("entrada.validade"))
        self.tbl_entradas.heading("data de entrada", text=Idioma.t("entrada.data_entrada"))

    def limpar_campos(self):
        self.cmb_medicamento.set("")
        self.cmb_fornecedor.set("")
        self.txt_numero_lote.delete(0, "end")
        self.txt_validade.entry.delete(0, "end")
        self.txt_qtd_entrada.delete(0, "end")
        self.cmb_usuario.set("")
        self.cmb_medicamento.focus()

    def ler_dados_entrada(self):
        medicamento_idx = self.cmb_medicamento.current()
        fornecedor_idx = self.cmb_fornecedor.current()
        numero_lote = self.txt_numero_lote.get()
        validade = self.txt_validade.entry.get()
        qtd_entrada = self.txt_qtd_entrada.get()
        usuario_idx = self.cmb_usuario.current()
        return medicamento_idx, fornecedor_idx, numero_lote, validade, qtd_entrada, usuario_idx

    def carregar_medicamentos(self, medicamentos):
        self.cmb_medicamento["values"] = [m.nome for m in medicamentos]

    def carregar_fornecedores(self, fornecedores):
        self.cmb_fornecedor["values"] = [f.nome for f in fornecedores]

    def carregar_usuarios(self, usuarios):
        self.cmb_usuario["values"] = [u.nome for u in usuarios]

    def limpar_treeview(self):
        for item in self.tbl_entradas.get_children():
            self.tbl_entradas.delete(item)

    def exibir_entradas(self, entradas):
        self.limpar_treeview()
        for e in entradas:
            self.tbl_entradas.insert("", "end", values=(
                e.id, e.lote.numero_lote, e.lote._medicamento.nome, e.lote._fornecedor.nome,
                e.qtd_entrada, e.lote.validade, e.data_entrada
            ))

    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            Messagebox.show_info(mensagem,"SysFarm", parent=self.root)
        else:
            Messagebox.show_error(mensagem,"SysFarm", parent=self.root)

    def configurar_eventos(self):
        self.btn_novo.config(command=self.controller.new)
        self.btn_salvar.config(command=self.controller.save)
        self.btn_fechar.config(command=self.fechar)

    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.carregar_combos()
        self.controller.get_all()