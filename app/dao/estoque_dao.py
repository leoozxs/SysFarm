from app.models.estoque import Estoque
from app.dao.dao import DAO

from app.models.lote import Lote
from app.models.medicamento import Medicamento

class Estoque_DAO(DAO):
    def __init__(self, database):
        super().__init__(database)

    def save(self, estoque):
        conexao, cursor = self.conectar()
        try:
            sql = """
                INSERT INTO ESTOQUE(
                    lote_id,
                    medicamento_id,
                    data_entrada,
                    validade,
                    qtd_atual,
                    status
                )
                VALUES(%s, %s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                estoque.lote.id,
                estoque.medicamento.id,
                estoque.data_entrada,
                estoque.validade,
                estoque.qtd_atual,
                estoque.status
            ))
            conexao.commit()
            estoque.id = cursor.lastrowid
            return estoque
        except Exception:
            conexao.rollback()
            raise
        finally:
            self.desconectar(conexao, cursor)

    def atualizar_quantidade(self, lote_id, nova_qtd, novo_status):
        conexao, cursor = self.conectar()
        try:
            sql = """
                UPDATE ESTOQUE SET
                    QTD_ATUAL = %s,
                    STATUS = %s
                WHERE 
                    LOTE_ID = %s
            """
            cursor.execute(sql, (nova_qtd, novo_status, lote_id))
            conexao.commit()
            return cursor.rowcount > 0
        except Exception:
            conexao.rollback()
            raise
        finally:
            self.desconectar(conexao, cursor)

    def get_by_lote_id(self, lote_id):
        conexao, cursor = self.conectar()
        try:
            sql = """
                SELECT
                    E.ID, E.LOTE_ID, E.MEDICAMENTO_ID, E.DATA_ENTRADA,
                    E.VALIDADE, E.QTD_ATUAL, E.STATUS,
                    L.NUMERO_LOTE,
                    M.ID, M.NOME, M.TIPO, M.CATEGORIA, M.DOSAGEM, M.ATIVO
                FROM 
                    ESTOQUE E JOIN LOTE L ON E.LOTE_ID = L.ID
                    JOIN MEDICAMENTO M ON E.MEDICAMENTO_ID = M.ID
                WHERE e.lote_id = %s
            """
            cursor.execute(sql, (lote_id,))
            registro = cursor.fetchone()
            if registro is None:
                return None
            return self._montar_estoque(registro)
        finally:
            self.desconectar(conexao, cursor)

    def get_all(self):
        conexao, cursor = self.conectar()
        try:
            sql = """
                SELECT
                    E.ID, E.LOTE_ID, E.MEDICAMENTO_ID, E.DATA_ENTRADA,
                    E.VALIDADE, E.QTD_ATUAL, E.STATUS,
                    L.NUMERO_LOTE,
                    M.ID, M.NOME, M.TIPO, M.CATEGORIA, M.DOSAGEM, M.ATIVO
                FROM 
                    ESTOQUE E JOIN LOTE L ON E.LOTE_ID = L.ID
                JOIN MEDICAMENTO M ON E.MEDICAMENTO.ID = M.ID
            """
            cursor.execute(sql)
            registros = cursor.fetchall()
            return [self._montar_estoque(r) for r in registros]
        finally:
            self.desconectar(conexao, cursor)
    
    def delete(self):
        pass
        #não tem delete
        
    def get_by_id(self, id):
        pass
        #nao tem get_by_id
        
    def update(self):
        pass
        #tabela nn faz update por ela mesma

    def _montar_estoque(self, registro):

        medicamento = Medicamento(registro[8], registro[9], registro[10], registro[11], registro[12], registro[13])
        lote = Lote(registro[1], registro[7], medicamento, None, registro[4])  # fornecedor não buscado aqui
        return Estoque(registro[0], lote, medicamento, registro[3], registro[4], registro[5], registro[6])