from app.dao.dao import DAO
from app.models.lote import Lote
from app.models.medicamento import Medicamento
from app.models.fornecedor import Fornecedor

class Lote_DAO(DAO):
    def __init__(self, database):
        super().__init__(database)

    def save(self, lote):
        conexao, cursor = self.conectar()
        try:
            sql = """
                INSERT INTO LOTE(
                    NUMERO_LOTE,
                    MEDICAMENTO_ID,
                    FORNECEDOR_ID,
                    VALIDADE)
                VALUES(%s, %s, %s, %s)
            """
            cursor.execute(sql, (
                lote.numero_lote,
                lote.medicamento.id,
                lote.fornecedor.id,
                lote.validade
            ))
            conexao.commit()
            lote.id = cursor.lastrowid
            return lote
        except Exception:
            conexao.rollback()
            raise
        finally:
            self.desconectar(conexao, cursor)

    def update(self, lote):
        conexao, cursor = self.conectar()
        try:
            sql = """
                UPDATE LOTE SET
                    NUMERO_LOTE = %s,
                    MEDICAMENTO_ID = %s,
                    FORNECEDOR_ID = %s,
                    VALIDADE = %s
                WHERE ID = %s
            """
            cursor.execute(sql, (
                lote.numero_lote,
                lote.medicamento.id,
                lote.fornecedor.id,
                lote.validade,
                lote.id
            ))
            conexao.commit()
            return cursor.rowcount > 0
        except Exception:
            conexao.rollback()
            raise
        finally:
            self.desconectar(conexao, cursor)

    def get_by_id(self, lote_id):
        conexao, cursor = self.conectar()
        try:
            sql = """
                SELECT
                    l.id, l.numero_lote, l.validade,
                    m.id, m.nome, m.tipo, m.categoria, m.dosagem, m.ativo,
                    f.id, f.nome, f.cnpj, f.ativo
                FROM LOTE l
                JOIN MEDICAMENTO m ON l.medicamento_id = m.id
                JOIN FORNECEDOR f ON l.fornecedor_id = f.id
                WHERE l.id = %s
            """
            cursor.execute(sql, (lote_id,))
            registro = cursor.fetchone()
            if registro is None:
                return None
            return self._montar_lote(registro)
        finally:
            self.desconectar(conexao, cursor)

    def get_all(self):
        conexao, cursor = self.conectar()
        try:
            sql = """
                SELECT
                    l.id, l.numero_lote, l.validade,
                    m.id, m.nome, m.tipo, m.categoria, m.dosagem, m.ativo,
                    f.id, f.nome, f.cnpj, f.ativo
                FROM LOTE l
                JOIN MEDICAMENTO m ON l.medicamento_id = m.id
                JOIN FORNECEDOR f ON l.fornecedor_id = f.id
            """
            cursor.execute(sql)
            registros = cursor.fetchall()
            return [self._montar_lote(r) for r in registros]
        finally:
            self.desconectar(conexao, cursor)

    def _montar_lote(self, registro):
        medicamento = Medicamento(registro[3], registro[4], registro[5], registro[6], registro[7], registro[8])
        fornecedor = Fornecedor(registro[9], registro[10], registro[11], registro[12])
        return Lote(registro[0], registro[1], medicamento, fornecedor, registro[2])

    def delete(self, lote_id):
        raise NotImplementedError(
            "Lotes não podem ser excluídos nem desativados — ficam ligados ao histórico de entrada, saída e estoque."
        )