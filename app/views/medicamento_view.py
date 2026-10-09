import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
from app.core.idioma import Idioma

TIPOS_BANCO = [
    "Comprimido", "Cápsula", "Drágea", "Pastilha", "Goma medicamentosa",
    "Pó", "Granulado", "Sachê", "Xarope", "Solução oral", "Suspensão oral",
    "Gotas", "Spray", "Aerossol", "Inalável", "Creme", "Pomada", "Gel",
    "Loção", "Espuma", "Adesivo transdérmico", "Supositório", "Óvulo vaginal",
    "Colírio", "Pomada oftálmica", "Gotas otológicas", "Spray nasal",
    "Injetável", "Implante", "Outros"
]

CATEGORIAS_BANCO = [
    "Analgésico", "Antibiótico", "Anti-inflamatório", "Antialérgico",
    "Antitérmico", "Antifúngico", "Antiviral", "Antidepressivo", "Ansiolítico",
    "Antisséptico", "Anticoagulante", "Anti-hipertensivo", "Antidiabético",
    "Anticoncepcional", "Antiácido", "Antiemético", "Laxante", "Antidiarreico",
    "Expectorante", "Descongestionante", "Corticoide", "Relaxante muscular",
    "Vitaminas", "Outros"
]

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
        self.root.title(Idioma.t("medicamento.janela_titulo"))
        self.root.geometry("700x600")
        self.root.resizable(False, False)

    def _centralizar(self):
        self.root.update_idletasks()
        largura, altura = 665, 600
        x = (self.root.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.root.winfo_screenheight() // 2) - (altura // 2)
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")

    def criar_componentes(self):
        self.lbl_titulo = ttk.Label(self.root, text=Idioma.t("medicamento.titulo"), font=("Courier New", 20, "bold"))
        self.lbl_titulo.grid(row=0, column=0, columnspan=4, pady=10)

        self.frm_dados = ttk.Labelframe(self.root, text=Idioma.t("medicamento.dados_frame"), labelanchor="n")
        self.frm_dados.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky="ew")

        self.lbl_id = ttk.Label(self.frm_dados, text=Idioma.t("comum.id"))
        self.lbl_id.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.txt_id = ttk.Entry(self.frm_dados, width=5, state="readonly")
        self.txt_id.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.lbl_nome = ttk.Label(self.frm_dados, text=Idioma.t("medicamento.nome"))
        self.lbl_nome.grid(row=0, column=2, padx=10, pady=10, sticky="w")
        self.txt_nome = ttk.Entry(self.frm_dados, width=28)
        self.txt_nome.grid(row=0, column=3, padx=10, pady=10, sticky="w")

        self.lbl_tipo = ttk.Label(self.frm_dados, text=Idioma.t("medicamento.tipo"))
        self.lbl_tipo.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.cmb_tipo = ttk.Combobox(self.frm_dados, width=20, state="readonly",
            values=[Idioma.t("medicamento.tipo.comprimido"),
                    Idioma.t("medicamento.tipo.capsula"),
                    Idioma.t("medicamento.tipo.dragea"),
                    Idioma.t("medicamento.tipo.pastilha"),
                    Idioma.t("medicamento.tipo.goma"),
                    Idioma.t("medicamento.tipo.po"),
                    Idioma.t("medicamento.tipo.granulado"),
                    Idioma.t("medicamento.tipo.sache"),
                    Idioma.t("medicamento.tipo.xarope"),
                    Idioma.t("medicamento.tipo.solucao_oral"),
                    Idioma.t("medicamento.tipo.suspensao_oral"),
                    Idioma.t("medicamento.tipo.gotas"),
                    Idioma.t("medicamento.tipo.spray"),
                    Idioma.t("medicamento.tipo.aerossol"),
                    Idioma.t("medicamento.tipo.inalavel"),
                    Idioma.t("medicamento.tipo.creme"),
                    Idioma.t("medicamento.tipo.pomada"),
                    Idioma.t("medicamento.tipo.gel"),
                    Idioma.t("medicamento.tipo.locao"),
                    Idioma.t("medicamento.tipo.espuma"),
                    Idioma.t("medicamento.tipo.adesivo"),
                    Idioma.t("medicamento.tipo.supositorio"),
                    Idioma.t("medicamento.tipo.ovulo"),
                    Idioma.t("medicamento.tipo.colirio"),
                    Idioma.t("medicamento.tipo.pomada_oftalmica"),
                    Idioma.t("medicamento.tipo.gotas_otologicas"),
                    Idioma.t("medicamento.tipo.spray_nasal"),
                    Idioma.t("medicamento.tipo.injetavel"),
                    Idioma.t("medicamento.tipo.implante"),
                    Idioma.t("medicamento.tipo.outros")])
        self.cmb_tipo.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.lbl_categoria = ttk.Label(self.frm_dados, text=Idioma.t("medicamento.categoria"))
        self.lbl_categoria.grid(row=1, column=2, padx=10, pady=10, sticky="w")
        self.cmb_categoria = ttk.Combobox(self.frm_dados, width=20, state="readonly",
            values=[Idioma.t("medicamento.categoria.analgesico"),
                    Idioma.t("medicamento.categoria.antibiotico"),
                    Idioma.t("medicamento.categoria.antiinflamatorio"),
                    Idioma.t("medicamento.categoria.antialergico"),
                    Idioma.t("medicamento.categoria.antitermico"),
                    Idioma.t("medicamento.categoria.antifungico"),
                    Idioma.t("medicamento.categoria.antiviral"),
                    Idioma.t("medicamento.categoria.antidepressivo"),
                    Idioma.t("medicamento.categoria.ansiolitico"),
                    Idioma.t("medicamento.categoria.antisseptico"),
                    Idioma.t("medicamento.categoria.anticoagulante"),
                    Idioma.t("medicamento.categoria.antihipertensivo"),
                    Idioma.t("medicamento.categoria.antidiabetico"),
                    Idioma.t("medicamento.categoria.anticoncepcional"),
                    Idioma.t("medicamento.categoria.antiacido"),
                    Idioma.t("medicamento.categoria.antiemetico"),
                    Idioma.t("medicamento.categoria.laxante"),
                    Idioma.t("medicamento.categoria.antidiarreico"),
                    Idioma.t("medicamento.categoria.expectorante"),
                    Idioma.t("medicamento.categoria.descongestionante"),
                    Idioma.t("medicamento.categoria.corticoide"),
                    Idioma.t("medicamento.categoria.relaxante_muscular"),
                    Idioma.t("medicamento.categoria.vitaminas"),
                    Idioma.t("medicamento.categoria.outros")])
        self.cmb_categoria.grid(row=1, column=3, padx=10, pady=10, sticky="w")

        self.lbl_dosagem = ttk.Label(self.frm_dados, text=Idioma.t("medicamento.dosagem"))
        self.lbl_dosagem.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        self.txt_dosagem = ttk.Entry(self.frm_dados, width=15)
        self.txt_dosagem.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.frm_botoes = ttk.Frame(self.frm_dados)
        self.frm_botoes.grid(row=3, column=0, columnspan=4, pady=10)

        self.btn_novo = ttk.Button(self.frm_botoes, text=Idioma.t("comum.novo"), width=15, bootstyle="primary-outline")
        self.btn_novo.grid(row=0, column=0, padx=5)
        self.btn_salvar = ttk.Button(self.frm_botoes, text=Idioma.t("comum.salvar"), width=15, bootstyle="success-outline")
        self.btn_salvar.grid(row=0, column=1, padx=5)
        self.btn_alterar = ttk.Button(self.frm_botoes, text=Idioma.t("comum.alterar"), width=15, bootstyle="warning-outline")
        self.btn_alterar.grid(row=0, column=2, padx=5)
        self.btn_excluir = ttk.Button(self.frm_botoes, text=Idioma.t("comum.excluir"), width=15, bootstyle="danger-outline")
        self.btn_excluir.grid(row=0, column=3, padx=5)
        self.btn_fechar = ttk.Button(self.frm_botoes, text=Idioma.t("comum.fechar"), width=15, bootstyle="secondary-outline")
        self.btn_fechar.grid(row=0, column=4, padx=5)

        self.tbl_medicamentos = ttk.Treeview(self.root, height=18, bootstyle="light")
        self.tbl_medicamentos.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

    def configurar_treeview(self):
        self.tbl_medicamentos["columns"] = ("id", "nome", "tipo", "categoria", "dosagem")
        self.tbl_medicamentos.column("#0", width=0, stretch=False)
        self.tbl_medicamentos.column("id", width=40, anchor="center", stretch=False)
        self.tbl_medicamentos.column("nome", width=180, anchor="center", stretch=False)
        self.tbl_medicamentos.column("tipo", width=120, anchor="center", stretch=False)
        self.tbl_medicamentos.column("categoria", width=120, anchor="center", stretch=False)
        self.tbl_medicamentos.column("dosagem", width=180, anchor="center", stretch=False)
        
        
        self.tbl_medicamentos.heading("id", text=Idioma.t("comum.id"))
        self.tbl_medicamentos.heading("nome", text=Idioma.t("medicamento.nome"))
        self.tbl_medicamentos.heading("tipo", text=Idioma.t("medicamento.tipo"))
        self.tbl_medicamentos.heading("categoria", text=Idioma.t("medicamento.categoria"))
        self.tbl_medicamentos.heading("dosagem", text=Idioma.t("medicamento.dosagem"))

    def preencher_campos(self, medicamento):
        self.limpar_campos()
        self.txt_id.config(state="normal")
        self.txt_id.insert(0, str(medicamento.id))
        self.txt_id.config(state="readonly")
        self.txt_nome.insert(0, str(medicamento.nome))
        self.cmb_tipo.current(TIPOS_BANCO.index(medicamento.tipo))
        self.cmb_categoria.current(CATEGORIAS_BANCO.index(medicamento.categoria))
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
        i_tipo = self.cmb_tipo.current()
        i_categoria = self.cmb_categoria.current()
        tipo = TIPOS_BANCO[i_tipo] if i_tipo >= 0 else ""
        categoria = CATEGORIAS_BANCO[i_categoria] if i_categoria >= 0 else ""
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
        tipos = self.cmb_tipo["values"]
        categorias = self.cmb_categoria["values"]
        for m in medicamentos:
            tipo = tipos[TIPOS_BANCO.index(m.tipo)] if m.tipo in TIPOS_BANCO else m.tipo
            categoria = categorias[CATEGORIAS_BANCO.index(m.categoria)] if m.categoria in CATEGORIAS_BANCO else m.categoria
            self.tbl_medicamentos.insert("", "end", values=(m.id, m.nome, tipo, categoria, m.dosagem))

    def confirmar_exclusao(self):
        resposta = Messagebox.yesno( Idioma.t("medicamento.confirmar_exclusao"), Idioma.t("comum.confirmacao"), parent=self.root)
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

