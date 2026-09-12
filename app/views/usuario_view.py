import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox



class Usuario_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_estilo()
        self.configurar_treeview()
        self.configurar_eventos()
        
    
    def configurar_janela(self):
        self.root.title("Gestão Usuários")
        self.root.geometry("685x600")
        self.root.resizable(False, False)

    def configurar_estilo(self):
        style = ttk.Style()
        #style.configure("TEntry", padding=(2,3))


    def criar_componentes(self):
        self.lbl_titulo = ttk.Label(self.root, text="Gerenciar Usuários", font=("Courier New",20,"bold"))   
        self.lbl_titulo.grid(row = 0, column = 0, columnspan=5) 
        self.frm_dados = ttk.Labelframe (self.root, text="Dados do Usuário", labelanchor="n")
        self.frm_dados.grid(row = 1, column = 0, columnspan = 4, padx = 10, pady = 5, sticky = "ew")
        
        
        self.lbl_id = ttk.Label(self.frm_dados, text = "ID", font=("Courier New",13,"bold"))
        self.lbl_id.grid(row = 1, column = 0, sticky = "w", padx = (20,0), pady= 5)
        self.txt_id = ttk.Entry(self.frm_dados, width=5, state="readonly")
        self.txt_id.grid(row=1, column=1, sticky="w", padx=(10,5), pady=5)
        
        
        self.lbl_nome = ttk.Label(self.frm_dados, text="Nome", font=("Courier New",13,"bold"))
        self.lbl_nome.grid(row = 1, column = 2, padx=5, sticky="w")
        self.txt_nome = ttk.Entry(self.frm_dados, width=28)
        self.txt_nome.grid(row=1, column = 2, columnspan=2)
        
        
        self.lbl_cpf = ttk.Label(self.frm_dados, text="CPF", font=("Courier New",13,"bold"))
        self.lbl_cpf.grid(row = 1, column = 3, padx=(20,5), sticky="e")
        self.txt_cpf = ttk.Entry(self.frm_dados, width=11)
        self.txt_cpf.grid(row=1, column=4, padx= 10, sticky="w")
        
        
        self.lbl_senha = ttk.Label(self.frm_dados, text="Senha", font=("Courier New",13,"bold"))
        self.lbl_senha.grid(row = 2, column = 0, padx=(10,5))
        self.txt_senha = ttk.Entry(self.frm_dados, width=20)
        self.txt_senha.grid(row=2, column=1, sticky="e", padx= 10, pady=10)
        
        
        self.lbl_cargo = ttk.Label(self.frm_dados, text="Cargo", font=("Courier New",13,"bold"))
        self.lbl_cargo.grid(row = 2, column = 2, sticky="w")
        self.txt_cargo = ttk.Entry(self.frm_dados, width=13)
        self.txt_cargo.grid(row=2, column=2, sticky="e", padx=(75,0))


        self.lbl_data_entrada = ttk.Label(self.frm_dados, text="Data de Entrada", font=("Courier New",13,"bold"))
        self.lbl_data_entrada.grid(row = 2, column = 3, padx=(10,5), sticky="w")
        self.txt_data_entrada = ttk.Entry(self.frm_dados, width=11)
        self.txt_data_entrada.grid(row=2, column=4, sticky="w", padx=10)
    
    
        #BOTOES
        self.frm_botoes = ttk.Frame(self.frm_dados)
        self.frm_botoes.grid(row=3,column=0,padx=10,pady=5, columnspan=5,)
        
        
        self.btn_novo = ttk.Button(self.frm_botoes,text = "Novo",width = 15, bootstyle="primary-outline", cursor="hand1")
        self.btn_novo.grid(row = 0,column = 0,padx = 5,pady = 5)
        
        
        self.btn_salvar = ttk.Button(self.frm_botoes,text = "Salvar",width = 15, bootstyle="success-outline", cursor="hand1")
        self.btn_salvar.grid(row = 0,column = 1,padx = 5, pady = 5)
        
        
        self.btn_alterar = ttk.Button(self.frm_botoes,text = "Alterar",width = 15, bootstyle="warning-outline", cursor="hand1")
        self.btn_alterar.grid(row = 0,column = 2,padx = 5,pady = 5)
        
        
        self.btn_excluir = ttk.Button(self.frm_botoes,text = "Excluir",width = 15, bootstyle="danger-outline", cursor="hand1")
        self.btn_excluir.grid(row = 0,column = 3,padx = 5,pady = 5)
        
        
        self.btn_fechar = ttk.Button(self.frm_botoes, text = "Fechar",width = 15, bootstyle="light-outline", cursor="hand1")
        self.btn_fechar.grid(row = 0,column = 4,padx = 5,pady = 5)
        
        #TREEVIEW
        self.tbl_usuarios = ttk.Treeview(self.root,height = 18, bootstyle="light")
        self.tbl_usuarios.grid(row = 3,column = 0,columnspan = 4,padx = 10,pady = 10,sticky = "nsew")
    
    def configurar_treeview(self):
        style = ttk.Style()
        self.tbl_usuarios["columns"] = ("id", "nome", "cpf", "senha", "cargo", "data de entrada")
        self.tbl_usuarios.column("#0",width = 0,stretch = False)
        self.tbl_usuarios.column("id", width=40, minwidth=40, anchor="center", stretch=False)
        self.tbl_usuarios.column("nome", width=140, anchor="w", stretch=False)
        self.tbl_usuarios.column("cpf", width=110, anchor="center", stretch=False)
        self.tbl_usuarios.column("senha", width=80, anchor="center", stretch=False)
        self.tbl_usuarios.column("cargo",width=120, anchor="w", stretch=False)
        self.tbl_usuarios.column("data de entrada",width=175, anchor="center", stretch=False)
        
        
        self.tbl_usuarios.heading("id",text="ID")
        self.tbl_usuarios.heading("nome",text="NOME")
        self.tbl_usuarios.heading("cpf",text="CPF")
        self.tbl_usuarios.heading("senha",text="SENHA")
        self.tbl_usuarios.heading("cargo",text="CARGO")
        self.tbl_usuarios.heading("data de entrada",text="DATA DE ENTRADA")
        style.configure("Treeview.Heading", font=("Arial", 9), padding=(1, 1))
        
        
        
    
    def configurar_eventos(self):
        
        # self.btn_novo.config(command = self.controller.new)
        # self.btn_salvar.config(command = self.controller.save)
        # self.btn_alterar.config(command = self.controller.update)
        # self.btn_excluir.config(command = self.controller.delete)
        # self.btn_fechar.config(command = self.fechar)
        # self.tbl_estados.bind("<<TreeviewSelect>>", self.controller.selecionar_estado)
        pass

    def limpar_campos(self):
        self.txt_id.config(state = "normal")
        self.txt_id.delete(0, ttk.END)
        self.txt_id.config(state = "readonly")
        self.txt_nome.delete(0, ttk.END)
        self.txt_cpf.delete(0, ttk.END)
        self.txt_cpf.delete(0, ttk.END)
        self.txt_nome.focus()

if __name__ == "__main__":
    import ttkbootstrap as ttk

    janela = ttk.Window(themename="darkly")
    view = Usuario_View(janela, controller=None)
    janela.mainloop()