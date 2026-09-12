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
        self.root.title("Entrada")
        self.root.geometry("700x600")
        self.root.resizable(False, False)

    def configurar_estilo(self):
        pass
        #style = ttk.Style()
        #style.configure("TEntry", padding=(2,3))


    def criar_componentes(self):
        self.lbl_titulo = ttk.Label(self.root, text="Cadastrar Entrada", font=("Courier New",20,"bold"))   
        self.lbl_titulo.grid(row = 0, column = 0) 
        
        self.frm_dados = ttk.Labelframe (self.root, text="")
        self.frm_dados.grid(row = 1, column = 0, columnspan = 4, padx = 10, pady = 5, sticky = "ew")
        
        self.lbl_id = ttk.Label(self.frm_dados, text = "ID")
        self.lbl_id.grid(row = 1, column = 0, sticky = "w", padx = 10, pady= 5)
        
        
        self.txt_id = ttk.Entry(self.frm_dados, width=5, state="readonly")
        self.txt_id.grid(row=1, column=2, sticky="w", pady=5)
        
        self.lbl_lote_id = ttk.Label(self.frm_dados, text="Serial Lote")
        self.lbl_lote_id.grid(row = 1, column = 3, sticky = "e", padx=(10,0))
        
        self.txt_lote_id = ttk.Entry(self.frm_dados, width=15)
        self.txt_lote_id.grid(row=1, column=3, sticky="e")
        
    
    def configurar_treeview(self):
        pass
    
    def configurar_eventos(self):
        pass


if __name__ == "__main__":
    import ttkbootstrap as ttk

    janela = ttk.Window(themename="darkly")
    view = Usuario_View(janela, controller=None)
    janela.mainloop()