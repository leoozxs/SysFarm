from datetime import date
from app.models.saida import Saida

class Saida_Controller:
    def __init__(self, view, lote_dao, saida_dao, estoque_dao, usuario_dao):
        self.view = view
        self.lote_dao = lote_dao
        self.saida_dao = saida_dao
        self.estoque_dao = estoque_dao
        self.usuario_dao = usuario_dao
        self._lotes = []
        self._usuarios = []

    def new(self):
        self.view.limpar_campos()

    def lote_selecionado(self, idx):
        if idx < 0 or idx >= len(self._lotes):
            return
        lote = self._lotes[idx]
        self.view.exibir_medicamento_do_lote(lote.medicamento.nome)

    def save(self):
        try:
            lote_idx, qtd_saida_str, tipo_saida, usuario_idx = self.view.ler_dados_saida()

            if lote_idx < 0 or usuario_idx < 0:
                self.view.exibir_mensagem("Selecione o lote e o usuário responsável.", False)
                return
            if not tipo_saida:
                self.view.exibir_mensagem("Selecione o tipo de saída.", False)
                return

            lote = self._lotes[lote_idx]
            usuario = self._usuarios[usuario_idx]
            qtd_saida = int(qtd_saida_str)

            if qtd_saida <= 0:
                self.view.exibir_mensagem("Quantidade de saída deve ser maior que zero.", False)
                return

            estoque_atual = self.estoque_dao.get_by_lote_id(lote.id)
            if estoque_atual is None:
                self.view.exibir_mensagem("Não há estoque registrado para esse lote.", False)
                return

            if qtd_saida > estoque_atual.qtd_atual:
                self.view.exibir_mensagem("Quantidade de saída maior que a disponível no lote.", False)
                return

            # 1. Registra a saída
            saida = Saida(None, lote, qtd_saida, tipo_saida, usuario, date.today())
            self.saida_dao.save(saida)

            # 2. Atualiza o estoque (desconta a quantidade)
            nova_qtd = estoque_atual.qtd_atual - qtd_saida
            novo_status = self.calcular_status(nova_qtd)
            self.estoque_dao.atualizar_quantidade(lote.id, nova_qtd, novo_status)

            self.get_all()
            self.view.limpar_campos()
            self.view.exibir_mensagem("Saída registrada com sucesso!")
        except ValueError as e:
            self.view.exibir_mensagem(f"Erro: {str(e)}", False)

    def calcular_status(self, qtd_atual):
        if qtd_atual == 0:
            return "Esgotado"
        elif qtd_atual < 20:
            return "Baixo"
        else:
            return "Disponível"

    def get_all(self):
        saidas = self.saida_dao.get_all()
        self.view.exibir_saidas(saidas)

    def carregar_combos(self):
        self._lotes = self.lote_dao.get_all()
        self._usuarios = self.usuario_dao.get_all()
        self.view.carregar_lotes(self._lotes)
        self.view.carregar_usuarios(self._usuarios)

    def iniciar(self):
        self.carregar_combos()
        self.get_all()