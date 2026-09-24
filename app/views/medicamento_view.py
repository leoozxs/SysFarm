import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox

class Medicamento_View:
    def __init__(self, root, controller=None):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()
        self._centralizar()

    def configurar_janela(self):
        self.root.title("Gestão de Medicamentos")
        self.root.geometry("700x600")
        self.root.resizable(False, False)

    def _centralizar(self):
        self.root.update_idletasks()
        largura, altura = 665, 600
        x = (self.root.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.root.winfo_screenheight() // 2) - (altura // 2)
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")

    def criar_componentes(self):
        self.lbl_titulo = ttk.Label(self.root, text="Gestão de Medicamentos", font=("Cour6ier New", 20, "bold"))
        self.lbl_titulo.grid(row=0, column=0, columnspan=4, pady=10)

        self.frm_dados = ttk.Labelframe(self.root, text="Dados do Medicamento", labelanchor="n")
        self.frm_dados.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky="ew")

        self.lbl_id = ttk.Label(self.frm_dados, text="ID")
        self.lbl_id.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.txt_id = ttk.Entry(self.frm_dados, width=5, state="readonly")
        self.txt_id.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.lbl_nome = ttk.Label(self.frm_dados, text="Nome")
        self.lbl_nome.grid(row=0, column=2, padx=10, pady=10, sticky="w")
        self.txt_nome = ttk.Entry(self.frm_dados, width=28)
        self.txt_nome.grid(row=0, column=3, padx=10, pady=10, sticky="w")

        self.lbl_tipo = ttk.Label(self.frm_dados, text="Tipo")
        self.lbl_tipo.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.cmb_tipo = ttk.Combobox(self.frm_dados, width=20, state="readonly",
            values=['Comprimido',
                    'Cápsula',
                    'Drágea',
                    'Pastilha',
                    'Goma medicamentosa',
                    'Pó',
                    'Granulado',
                    'Sachê',
                    'Xarope',
                    'Solução oral',
                    'Suspensão oral',
                    'Gotas',
                    'Spray',
                    'Aerossol',
                    'Inalável',
                    'Creme',
                    'Pomada',
                    'Gel',
                    'Loção',
                    'Espuma',
                    'Adesivo transdérmico',
                    'Supositório',
                    'Óvulo vaginal',
                    'Colírio',
                    'Pomada oftálmica',
                    'Gotas otológicas',
                    'Spray nasal',
                    'Injetável',
                    'Implante',
                    'Outros'])
        self.cmb_tipo.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.lbl_categoria = ttk.Label(self.frm_dados, text="Categoria")
        self.lbl_categoria.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.cmb_categoria = ttk.Combobox(self.frm_dados, width=20, state="readonly",
            values=['Analgésico',
                    'Antibiótico',
                    'Anti-inflamatório',
                    'Antialérgico',
                    'Antitérmico',
                    'Antifúngico',
                    'Antiviral',
                    'Antidepressivo',
                    'Ansiolítico',
                    'Antisséptico',
                    'Anticoagulante',
                    'Anti-hipertensivo',
                    'Antidiabético',
                    'Anticoncepcional',
                    'Antiácido',
                    'Antiemético',
                    'Laxante',
                    'Antidiarreico',
                    'Expectorante',
                    'Descongestionante',
                    'Corticoide',
                    'Relaxante muscular',
                    'Vitaminas',
                    'Outros'])
        self.cmb_categoria.grid(row=1, column=3, padx=10, pady=10, sticky="w")

        self.lbl_dosagem = ttk.Label(self.frm_dados, text="Dosagem")
        self.lbl_dosagem.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.txt_dosagem = ttk.Entry(self.frm_dados, width=15)
        self.txt_dosagem.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.frm_botoes = ttk.Frame(self.frm_dados)
        self.frm_botoes.grid(row=3, column=0, columnspan=4, pady=10)

        self.btn_novo = ttk.Button(self.frm_botoes, text="Novo", width=15, bootstyle="primary-outline")
        self.btn_novo.grid(row=0, column=0, padx=5)
        self.btn_salvar = ttk.Button(self.frm_botoes, text="Salvar", width=15, bootstyle="success-outline")
        self.btn_salvar.grid(row=0, column=1, padx=5)
        self.btn_alterar = ttk.Button(self.frm_botoes, text="Alterar", width=15, bootstyle="warning-outline")
        self.btn_alterar.grid(row=0, column=2, padx=5)
        self.btn_excluir = ttk.Button(self.frm_botoes, text="Excluir", width=15, bootstyle="danger-outline")
        self.btn_excluir.grid(row=0, column=3, padx=5)
        self.btn_fechar = ttk.Button(self.frm_botoes, text="Fechar", width=15, bootstyle="secondary-outline")
        self.btn_fechar.grid(row=0, column=4, padx=5)

        self.tbl_medicamentos = ttk.Treeview(self.root, height=18, bootstyle="light")
        self.tbl_medicamentos.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

    def configurar_treeview(self):
        self.tbl_medicamentos["columns"] = ("id", "nome", "tipo", "categoria", "dosagem")
        self.tbl_medicamentos.column("#0", width=0, stretch=False)
        self.tbl_medicamentos.column("id", width=40, anchor="center", stretch=False)
        self.tbl_medicamentos.column("nome", width=180, anchor="w", stretch=False)
        self.tbl_medicamentos.column("tipo", width=120, anchor="w", stretch=False)
        self.tbl_medicamentos.column("categoria", width=120, anchor="w", stretch=False)
        self.tbl_medicamentos.column("dosagem", width=180, anchor="center", stretch=False)
        
        
        self.tbl_medicamentos.heading("id", text="ID")
        self.tbl_medicamentos.heading("nome", text="NOME")
        self.tbl_medicamentos.heading("tipo", text="TIPO")
        self.tbl_medicamentos.heading("categoria", text="CATEGORIA")
        self.tbl_medicamentos.heading("dosagem", text="DOSAGEM")

    def preencher_campos(self, medicamento):
        self.limpar_campos()
        self.txt_id.config(state="normal")
        self.txt_id.insert(0, str(medicamento.id))
        self.txt_id.config(state="readonly")
        self.txt_nome.insert(0, str(medicamento.nome))
        self.cmb_tipo.set(medicamento.tipo)
        self.cmb_categoria.set(medicamento.categoria)
        self.txt_dosagem.insert(0, str(medicamento.dosagem))

    def limpar_campos(self):
        self.txt_id.config(state="normal")
        self.txt_id.delete(0, "end")
        self.txt_id.config(state="readonly")
        self.txt_nome.delete(0, "end")
        self.cmb_tipo.set("")
        self.cmb_categoria.set("")
        self.txt_dosagem.delete(0, "end")
        self.txt_nome.focus()

    def ler_dados_medicamento(self):
        nome = self.txt_nome.get()
        tipo = self.cmb_tipo.get()
        categoria = self.cmb_categoria.get()
        dosagem = self.txt_dosagem.get()
        return nome, tipo, categoria, dosagem

    def get_id_selecionado(self):
        item = self.tbl_medicamentos.selection()[0]
        return self.tbl_medicamentos.item(item)["values"][0]

    def limpar_treeview(self):
        for item in self.tbl_medicamentos.get_children():
            self.tbl_medicamentos.delete(item)

    def exibir_medicamentos(self, medicamentos):
        self.limpar_treeview()
        for m in medicamentos:
            self.tbl_medicamentos.insert("", "end", values=(m.id, m.nome, m.tipo, m.categoria, m.dosagem))

    def confirmar_exclusao(self):
        resposta = Messagebox.yesno( "Deseja realmente excluir este medicamento?","Confirmação", parent=self.root)
        return resposta == "Yes"

    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            Messagebox.show_info(mensagem,"SysFarm", parent=self.root)
        else:
            Messagebox.show_error(mensagem,"SysFarm", parent=self.root)
            
    def configurar_eventos(self):
        self.btn_novo.config(command=self.controller.new)
        self.btn_salvar.config(command=self.controller.save)
        self.btn_alterar.config(command=self.controller.update)
        self.btn_excluir.config(command=self.controller.delete)
        self.btn_fechar.config(command=self.fechar)
        self.tbl_medicamentos.bind("<<TreeviewSelect>>", self.controller.selecionar_medicamento)

    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.get_all()

