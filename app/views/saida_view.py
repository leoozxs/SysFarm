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

    def configurar_janela(self):
        self.root.title("Registrar Saída")
        self.root.geometry("750x600")
        self.root.resizable(False, False)

    def criar_componentes(self):
        self.lbl_titulo = ttk.Label(self.root, text="Registrar Saída", font=("Courier New", 20, "bold"))
        self.lbl_titulo.grid(row=0, column=0, columnspan=4, pady=10)

        self.frm_dados = ttk.Labelframe(self.root, text="Dados da Saída", labelanchor="n")
        self.frm_dados.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky="ew")

        self.lbl_lote = ttk.Label(self.frm_dados, text="Lote Referente")
        self.lbl_lote.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.cmb_lote = ttk.Combobox(self.frm_dados, width=25, state="readonly")
        self.cmb_lote.grid(row=0, column=1, padx=10, pady=10, sticky="w")
        self.cmb_lote.bind("<<ComboboxSelected>>", self.preencher_medicamento_automatico)

        self.lbl_medicamento = ttk.Label(self.frm_dados, text="Medicamento")
        self.lbl_medicamento.grid(row=0, column=2, padx=10, pady=10, sticky="w")
        self.txt_medicamento = ttk.Entry(self.frm_dados, width=25, state="readonly")
        self.txt_medicamento.grid(row=0, column=3, padx=10, pady=10, sticky="w")

        self.lbl_qtd_saida = ttk.Label(self.frm_dados, text="Quantidade de Saída")
        self.lbl_qtd_saida.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.txt_qtd_saida = ttk.Entry(self.frm_dados, width=10)
        self.txt_qtd_saida.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.lbl_tipo_saida = ttk.Label(self.frm_dados, text="Tipo de Saída")
        self.lbl_tipo_saida.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.cmb_tipo_saida = ttk.Combobox(
            self.frm_dados, width=15, state="readonly",
            values=["Venda", "Avaria", "Perda", "Roubo"]
        )
        self.cmb_tipo_saida.grid(row=1, column=3, padx=10, pady=10, sticky="w")

        self.lbl_usuario = ttk.Label(self.frm_dados, text="Usuário Responsável")
        self.lbl_usuario.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.cmb_usuario = ttk.Combobox(self.frm_dados, width=25, state="readonly")
        self.cmb_usuario.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.frm_botoes = ttk.Frame(self.frm_dados)
        self.frm_botoes.grid(row=3, column=0, columnspan=4, pady=10)

        self.btn_novo = ttk.Button(self.frm_botoes, text="Novo", width=15, bootstyle="primary-outline")
        self.btn_novo.grid(row=0, column=0, padx=5)
        self.btn_salvar = ttk.Button(self.frm_botoes, text="Salvar", width=15, bootstyle="success-outline")
        self.btn_salvar.grid(row=0, column=1, padx=5)
        self.btn_fechar = ttk.Button(self.frm_botoes, text="Fechar", width=15, bootstyle="secondary-outline")
        self.btn_fechar.grid(row=0, column=2, padx=5)

        self.tbl_saidas = ttk.Treeview(self.root, height=12, bootstyle="light")
        self.tbl_saidas.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

    def configurar_treeview(self):
        self.tbl_saidas["columns"] = ("id", "lote", "medicamento", "qtd", "tipo", "usuario", "data")
        self.tbl_saidas.column("#0", width=0, stretch=False)
        self.tbl_saidas.column("id", width=40, anchor="center", stretch=False)
        self.tbl_saidas.column("lote", width=80, anchor="center", stretch=False)
        self.tbl_saidas.column("medicamento", width=140, anchor="w", stretch=False)
        self.tbl_saidas.column("qtd", width=50, anchor="center", stretch=False)
        self.tbl_saidas.column("tipo", width=80, anchor="center", stretch=False)
        self.tbl_saidas.column("usuario", width=120, anchor="w", stretch=False)
        self.tbl_saidas.column("data", width=90, anchor="center", stretch=False)
        self.tbl_saidas.heading("id", text="ID")
        self.tbl_saidas.heading("lote", text="LOTE")
        self.tbl_saidas.heading("medicamento", text="MEDICAMENTO")
        self.tbl_saidas.heading("qtd", text="QTD")
        self.tbl_saidas.heading("tipo", text="TIPO")
        self.tbl_saidas.heading("usuario", text="USUÁRIO")
        self.tbl_saidas.heading("data", text="DATA")

    def preencher_medicamento_automatico(self, event=None):
        # o controller injeta a lista de lotes; aqui só repassamos o índice escolhido
        self.controller.lote_selecionado(self.cmb_lote.current())

    def exibir_medicamento_do_lote(self, nome_medicamento):
        self.txt_medicamento.config(state="normal")
        self.txt_medicamento.delete(0, "end")
        self.txt_medicamento.insert(0, nome_medicamento)
        self.txt_medicamento.config(state="readonly")

    def limpar_campos(self):
        self.cmb_lote.set("")
        self.txt_medicamento.config(state="normal")
        self.txt_medicamento.delete(0, "end")
        self.txt_medicamento.config(state="readonly")
        self.txt_qtd_saida.delete(0, "end")
        self.cmb_tipo_saida.set("")
        self.cmb_usuario.set("")
        self.cmb_lote.focus()

    def ler_dados_saida(self):
        lote_idx = self.cmb_lote.current()
        qtd_saida = self.txt_qtd_saida.get()
        tipo_saida = self.cmb_tipo_saida.get()
        usuario_idx = self.cmb_usuario.current()
        return lote_idx, qtd_saida, tipo_saida, usuario_idx

    def carregar_lotes(self, lotes):
        self.cmb_lote["values"] = [l.numero_lote for l in lotes]

    def carregar_usuarios(self, usuarios):
        self.cmb_usuario["values"] = [u.nome for u in usuarios]

    def limpar_treeview(self):
        for item in self.tbl_saidas.get_children():
            self.tbl_saidas.delete(item)

    def exibir_saidas(self, saidas):
        self.limpar_treeview()
        for s in saidas:
            self.tbl_saidas.insert("", "end", values=(
                s.id, s.lote.numero_lote, s.lote.medicamento.nome, s.qtd_saida,
                s.tipo_saida, s.usuario.nome, s.data_saida
            ))

    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            Messagebox.showinfo("SysFarm", mensagem, parent=self.root)
        else:
            Messagebox.showerror("SysFarm", mensagem, parent=self.root)

    def configurar_eventos(self):
        self.btn_novo.config(command=self.controller.new)
        self.btn_salvar.config(command=self.controller.save)
        self.btn_fechar.config(command=self.fechar)

    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.get_all()


if __name__ == "__main__":
    class ControllerFake:
        def new(self): print("novo")
        def save(self): print("salvar")
        def lote_selecionado(self, idx): print(f"lote {idx} selecionado")

    janela = ttk.Window(themename="darkly")
    view = Saida_View(janela, controller=ControllerFake())
    janela.mainloop()