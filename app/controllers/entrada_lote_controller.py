from datetime import datetime, date
from app.models.entrada import Entrada
from app.models.lote import Lote
from app.models.estoque import Estoque
from app.core.idioma import Idioma

# Inicio da entrada de medicamentos no estoque
class Entrada_Controller:
    def __init__(self, view, lote_dao, entrada_dao, estoque_dao, medicamento_dao, fornecedor_dao, usuario_dao):
        self.view = view
        self.lote_dao = lote_dao
        self.entrada_dao = entrada_dao
        self.estoque_dao = estoque_dao
        self.medicamento_dao = medicamento_dao
        self.fornecedor_dao = fornecedor_dao
        self.usuario_dao = usuario_dao
        self._medicamentos = []
        self._fornecedores = []
        self._usuarios = []

# Criação de um novo lote e registro da entrada no estoque
    def new(self):
        self.view.limpar_campos()

#Definindo o status do estoque com base na quantidade atual
    def save(self):
        try:
            medicamento_idx, fornecedor_idx, numero_lote, validade_str, qtd_entrada_str, usuario_idx = self.view.ler_dados_entrada()

            if medicamento_idx < 0 or fornecedor_idx < 0 or usuario_idx < 0:
                self.view.exibir_mensagem(Idioma.t("entrada.ausencia_campos"), False)
                return
            
            if not numero_lote:
                self.view.exibir_mensagem(Idioma.t("entrada.ausencia_lote"))
                return
                
            medicamento = self._medicamentos[medicamento_idx]
            fornecedor = self._fornecedores[fornecedor_idx]
            usuario = self._usuarios[usuario_idx]

            try:
                validade = datetime.strptime(validade_str, "%d/%m/%Y").date()
            except ValueError:
                self.view.exibir_mensagem(Idioma.t("usuario.erro_data_invalida"), False)
                return
            try:
                qtd_entrada = int(qtd_entrada_str)
            except ValueError:
                self.view.exibir_mensagem(Idioma.t("entrada.erro_qtd_invalida"))
                return
            data_entrada = date.today()

            # 1. Cria o lote
            lote = Lote(None, numero_lote, medicamento, fornecedor, validade)
            lote = self.lote_dao.save(lote)

            # 2. Registra a entrada
            entrada = Entrada(None, lote, qtd_entrada, data_entrada, usuario)
            self.entrada_dao.save(entrada)

            # 3. Cria a linha de estoque correspondente a esse lote
            status = self.calcular_status(qtd_entrada)
            estoque = Estoque(None, lote, medicamento, fornecedor, data_entrada, validade, qtd_entrada, status)
            self.estoque_dao.save(estoque)

            self.get_all()
            self.view.limpar_campos()
            self.view.exibir_mensagem(Idioma.t("entrada.cadastrado_sucesso"))
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)
            
# Cálculo do status do estoque referente a quantidade atual de medicamentos
    def calcular_status(self, qtd_atual):
        if qtd_atual == 0:
            return Idioma.t("entrada.status_esgotado")
        elif qtd_atual < 20:
            return Idioma.t("entrada.status_baixo")
        else:
            return Idioma.t("entrada.status_disponivel")
        
# Exibição de todas as entradas registradas no estoque
    def get_all(self):
        entradas = self.entrada_dao.get_all()
        self.view.exibir_entradas(entradas)

# Carregamento dos combos de seleção de medicamentos, fornecedores e usuários
    def carregar_combos(self):
        self._medicamentos = self.medicamento_dao.get_all()
        self._fornecedores = self.fornecedor_dao.get_all()
        self._usuarios = self.usuario_dao.get_all()
        self.view.carregar_medicamentos(self._medicamentos)
        self.view.carregar_fornecedores(self._fornecedores)
        self.view.carregar_usuarios(self._usuarios)

# Carregamento para iniciar as combos registradas
    def iniciar(self):
        self.carregar_combos()
        self.get_all()