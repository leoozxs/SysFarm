import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox

class Fornecedor_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_treeview()
        self.configurar_eventos()
        self._centralizar()

    def configurar_janela(self):
        self.root.title("Gestão de Fornecedores")
        self.root.geometry("700x600")
        self.root.resizable(False, False)
        
    def _centralizar(self):
        self.root.update_idletasks()
        largura, altura = 675, 585
        x = (self.root.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.root.winfo_screenheight() // 2) - (altura // 2)
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")

    def criar_componentes(self):
        self.lbl_titulo = ttk.Label(self.root, text="Gestão de Fornecedores", font=("Courier New", 20, "bold"))
        self.lbl_titulo.grid(row=0, column=0, columnspan=4, pady=10)

        self.frm_dados = ttk.Labelframe(self.root, text="Dados do Fornecedor", labelanchor="n")
        self.frm_dados.grid(row=1, column=0, columnspan=4, padx=10, pady=5, sticky="ew")

        self.lbl_id = ttk.Label(self.frm_dados, text="ID")
        self.lbl_id.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        self.txt_id = ttk.Entry(self.frm_dados, width=5, state="readonly")
        self.txt_id.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        self.lbl_nome = ttk.Label(self.frm_dados, text="Nome")
        self.lbl_nome.grid(row=0, column=2, padx=10, pady=10, sticky="w")
        self.txt_nome = ttk.Entry(self.frm_dados, width=28)
        self.txt_nome.grid(row=0, column=3, padx=10, pady=10, sticky="w")

        self.lbl_cnpj = ttk.Label(self.frm_dados, text="CNPJ")
        self.lbl_cnpj.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        self.txt_cnpj = ttk.Entry(self.frm_dados, width=18)
        self.txt_cnpj.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        self.frm_botoes = ttk.Frame(self.frm_dados)
        self.frm_botoes.grid(row=2, column=0, columnspan=4, pady=10)

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

        self.tbl_fornecedores = ttk.Treeview(self.root, height=20, bootstyle="light")
        self.tbl_fornecedores.grid(row=2, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

    def configurar_treeview(self):
        self.tbl_fornecedores["columns"] = ("id", "nome", "cnpj")
        self.tbl_fornecedores.column("#0", width=0, stretch=False)
        self.tbl_fornecedores.column("id", width=150, anchor="w", stretch=False)
        self.tbl_fornecedores.column("nome", width=300, anchor="w", stretch=False)
        self.tbl_fornecedores.column("cnpj", width=200, anchor="center", stretch=False)
        
        self.tbl_fornecedores.heading("id", text="ID")
        self.tbl_fornecedores.heading("nome", text="NOME")
        self.tbl_fornecedores.heading("cnpj", text="CNPJ")
        
        self.txt_cnpj.bind("<KeyRelease>", self.formatar_cnpj)

    def formatar_cnpj(self, event=None):
        texto = self.txt_cnpj.get()
        numeros = "".join(filter(str.isdigit, texto))[:14]
        if len(numeros) > 12:
            formatado = f"{numeros[:2]}.{numeros[2:5]}.{numeros[5:8]}/{numeros[8:12]}-{numeros[12:]}"
        elif len(numeros) > 8:
            formatado = f"{numeros[:2]}.{numeros[2:5]}.{numeros[5:8]}/{numeros[8:]}"
        elif len(numeros) > 5:
            formatado = f"{numeros[:2]}.{numeros[2:5]}.{numeros[5:]}"
        elif len(numeros) > 2:
            formatado = f"{numeros[:2]}.{numeros[2:]}"
        else:
            formatado = numeros
        self.txt_cnpj.delete(0, "end")
        self.txt_cnpj.insert(0, formatado)

    def preencher_campos(self, fornecedor):
        self.limpar_campos()
        self.txt_id.config(state="normal")
        self.txt_id.insert(0, str(fornecedor.id))
        self.txt_id.config(state="readonly")
        self.txt_nome.insert(0, str(fornecedor.nome))
        self.txt_cnpj.insert(0, str(fornecedor.cnpj))

    def limpar_campos(self):
        self.txt_id.config(state="normal")
        self.txt_id.delete(0, "end")
        self.txt_id.config(state="readonly")
        self.txt_nome.delete(0, "end")
        self.txt_cnpj.delete(0, "end")
        self.txt_nome.focus()

    def ler_dados_fornecedor(self):
        nome = self.txt_nome.get()
        cnpj = "".join(filter(str.isdigit, self.txt_cnpj.get()))
        return nome, cnpj

    def get_id_selecionado(self):
        item = self.tbl_fornecedores.selection()[0]
        return self.tbl_fornecedores.item(item)["values"][0]

    def limpar_treeview(self):
        for item in self.tbl_fornecedores.get_children():
            self.tbl_fornecedores.delete(item)

    def exibir_fornecedores(self, fornecedores):
        self.limpar_treeview()
        for f in fornecedores:
            self.tbl_fornecedores.insert("", "end", values=(f.id, f.nome, f.cnpj))

    def confirmar_exclusao(self):
        return Messagebox.askyesno("Confirmação", "Deseja realmente excluir este fornecedor?", parent=self.root)

    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            Messagebox.showinfo("SysFarm", mensagem, parent=self.root)
        else:
            Messagebox.showerror("SysFarm", mensagem, parent=self.root)

    def configurar_eventos(self):
        self.btn_novo.config(command=self.controller.new)
        self.btn_salvar.config(command=self.controller.save)
        self.btn_alterar.config(command=self.controller.update)
        self.btn_excluir.config(command=self.controller.delete)
        self.btn_fechar.config(command=self.fechar)
        self.tbl_fornecedores.bind("<<TreeviewSelect>>", self.controller.selecionar_fornecedor)

    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.get_all()