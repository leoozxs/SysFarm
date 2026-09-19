import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox
import customtkinter as ctk

class Usuario_View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.configurar_janela()
        self.criar_componentes()
        self.configurar_estilo()
        self.configurar_treeview()
        self.configurar_eventos()
        self._centralizar()
        
    def _centralizar(self):
        self.root.update_idletasks()
        largura, altura = 700, 600
        x = (self.root.winfo_screenwidth() // 2) - (largura // 2)
        y = (self.root.winfo_screenheight() // 2) - (altura // 2)
        self.root.geometry(f"{largura}x{altura}+{x}+{y}")
    
    def configurar_janela(self):
        self.root.title("Gestão Usuários")
        self.root.resizable(False, False)

    def configurar_estilo(self):
        style = ttk.Style()
        #style.configure("TEntry", padding=(2,3))


    def criar_componentes(self):
        self.lbl_titulo = ttk.Label(self.root, text="Gerenciar Usuários", font=("Cour6ier New", 20, "bold"))   
        self.lbl_titulo.grid(row = 0, column = 0, columnspan=5) 
        self.frm_dados = ttk.Labelframe (self.root, text="Dados do Usuário", labelanchor="n")
        self.frm_dados.grid(row = 1, column = 0, columnspan = 4, padx = 10, pady = 5, sticky = "ew")
        
        
        self.lbl_id = ttk.Label(self.frm_dados, text = "ID")
        self.lbl_id.grid(row = 1, column = 0, sticky = "w", padx = (20,0), pady= 5)
        self.txt_id = ttk.Entry(self.frm_dados, width=5, state="readonly")
        self.txt_id.grid(row=1, column=1, sticky="w", padx=(10,5), pady=5)
        
        
        self.lbl_nome = ttk.Label(self.frm_dados, text="Nome")
        self.lbl_nome.grid(row = 1, column = 2, padx=5, sticky="w")
        self.txt_nome = ttk.Entry(self.frm_dados, width=28)
        self.txt_nome.grid(row=1, column = 2, columnspan=2)
        
        
        self.lbl_cpf = ttk.Label(self.frm_dados, text="CPF")
        self.lbl_cpf.grid(row = 1, column = 3, padx=(20,5), sticky="e")
        self.txt_cpf = ttk.Entry(self.frm_dados, width=11)
        self.txt_cpf.grid(row=1, column=4, padx= 10, sticky="w")
        
        
        self.lbl_senha = ttk.Label(self.frm_dados, text="Senha")
        self.lbl_senha.grid(row = 2, column = 0, padx=(10,5))
        self.txt_senha = ttk.Entry(self.frm_dados, width=20)
        self.txt_senha.grid(row=2, column=1, sticky="w", padx= 10, pady=10)
        
        
        self.lbl_cargo = ttk.Label(self.frm_dados, text="Cargo")
        self.lbl_cargo.place(relx=0.34, rely=0.4)
        self.txt_cargo = ttk.Entry(self.frm_dados, width=13)
        self.txt_cargo.grid(row=2, column=2, sticky="e", padx=(75,0))


        self.lbl_data_entrada = ttk.Label(self.frm_dados, text="Data de Entrada")
        self.lbl_data_entrada.grid(row = 2, column = 3, padx=(10,5), sticky="w")
        self.txt_data_entrada = ttk.DateEntry(self.frm_dados, width=11, date_format="%d/%m/%Y", bootstyle="light-outline" )
        self.txt_data_entrada.grid(row=2, column=4, sticky="w", padx=10)
    
    
        #BOTOES
        self.frm_botoes = ttk.Frame(self.frm_dados)
        self.frm_botoes.grid(row=3,column=0,padx=10,pady=5, columnspan=5,)
        
        
        self.btn_novo = ttk.Button(self.frm_botoes,text = "Novo",width = 15, bootstyle="primary-outline")
        self.btn_novo.grid(row = 0,column = 0,padx = 5,pady = 5)
        
        
        self.btn_salvar = ttk.Button(self.frm_botoes,text = "Salvar",width = 15, bootstyle="success-outline")
        self.btn_salvar.grid(row = 0,column = 1,padx = 5, pady = 5)
        
        
        self.btn_alterar = ttk.Button(self.frm_botoes,text = "Alterar",width = 15, bootstyle="warning-outline")
        self.btn_alterar.grid(row = 0,column = 2,padx = 5,pady = 5)
        
        
        self.btn_excluir = ttk.Button(self.frm_botoes,text = "Excluir",width = 15, bootstyle="danger-outline")
        self.btn_excluir.grid(row = 0,column = 3,padx = 5,pady = 5)
        
        
        self.btn_fechar = ttk.Button(self.frm_botoes, text = "Fechar",width = 15, bootstyle="light-outline")
        self.btn_fechar.grid(row = 0,column = 4,padx = 5,pady = 5)
        
        #TREEVIEW
        self.tbl_usuarios = ttk.Treeview(self.root,height = 23, bootstyle="light")
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
        self.tbl_usuarios.column("data de entrada",width=190, anchor="center", stretch=False)
        
        
        self.tbl_usuarios.heading("id",text="ID")
        self.tbl_usuarios.heading("nome",text="NOME")
        self.tbl_usuarios.heading("cpf",text="CPF")
        self.tbl_usuarios.heading("senha",text="SENHA")
        self.tbl_usuarios.heading("cargo",text="CARGO")
        self.tbl_usuarios.heading("data de entrada",text="DATA DE ENTRADA")
        style.configure("Treeview.Heading", font=("Arial", 9), padding=(1, 1))
        
    def preencher_campos(self, usuario):
        self.limpar_campos()
        
        self.txt_id.config(state="normal")
        self.txt_id.insert(0, str(usuario.id))
        self.txt_id.config(state="readonly")
        
        self.txt_nome.insert(0, str(usuario.nome))
        
        self.txt_cpf.insert(0, str(usuario.cpf))
        
        self.txt_senha.insert(0, str(usuario.senha))
        
        self.txt_cargo.insert(0, str(usuario.cargo))

        self.txt_data_entrada.entry.delete(0, "end")
        self.txt_data_entrada.entry.insert(0, usuario.data_entrada.strftime("%d/%m/%Y"))
        

    def limpar_treeview(self):
        for item in self.tbl_usuarios.get_children():
            self.tbl_usuarios.delete(item)


    def get_id_selecionado(self):

        item = self.tbl_usuarios.selection()[0]

        return self.tbl_usuarios.item(item)["values"][0]

    def ler_dados_usuario(self):
        nome = self.txt_nome.get()
        cpf = self.txt_cpf.get()
        senha = self.txt_senha.get()
        cargo = self.txt_cargo.get()
        data_entrada = self.txt_data_entrada.entry.get()
        return nome, cpf, senha, cargo, data_entrada

    def confirmar_exclusao(self):

        return Messagebox.askyesno(
            "Confirmação",
            "Deseja realmente excluir este usuario?",
            parent=self.root
            )

    def exibir_mensagem(self, mensagem, sucesso=True):
        if sucesso:
            Messagebox.showinfo("SysFarm",mensagem,parent=self.root)
        else:
            Messagebox.showerror("SysFarm", mensagem, parent=self.root)
            
    def configurar_eventos(self):
        
        self.btn_novo.configure(command = self.controller.new)
        self.btn_salvar.configure(command = self.controller.save)
        self.btn_alterar.configure(command = self.controller.update)
        self.btn_excluir.configure(command = self.controller.delete)
        self.btn_fechar.configure(command = self.fechar)
        self.tbl_usuarios.bind("<<TreeviewSelect>>", self.controller.selecionar_usuario)

    def limpar_campos(self):
        self.txt_id.config(state = "normal")
        self.txt_id.delete(0, ttk.END)
        self.txt_id.config(state = "readonly")
        self.txt_nome.delete(0, ttk.END)
        self.txt_cpf.delete(0, ttk.END)
        self.txt_senha.delete(0, ttk.END)
        self.txt_cargo.delete(0, ttk.END)
        self.txt_data_entrada.entry.delete(0, "end")
        self.txt_nome.focus()
        
    def exibir_usuarios(self, usuarios):

        self.limpar_treeview()

        for usuario in usuarios:

            self.tbl_usuarios.insert(
                "",
                ttk.END,
                values=(
                    usuario.id,
                    usuario.nome,
                    usuario.cpf,
                    usuario.senha,
                    usuario.cargo,
                    usuario.data_entrada
                )
            )

    def fechar(self):
        self.root.destroy()

    def iniciar(self):
        self.controller.get_all()



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

    janela = ttk.Window(themename="darkly")
    view = Usuario_View(janela, controller=ControllerFake())
    janela.mainloop()