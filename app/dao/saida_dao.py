from app.dao.dao import DAO
from app.models.saida import Saida
from app.models.lote import Lote
from app.models.medicamento import Medicamento
from app.models.fornecedor import Fornecedor
from app.models.usuario import Usuario

class Saida_DAO(DAO):
    def __init__(self, database):
        super().__init__(database)

    def save(self, saida):
        conexao, cursor = self.conectar()
        try:
            sql = """
                INSERT INTO SAIDA(
                    LOTE_ID,
                    QTD_SAIDA,
                    TIPO_SAIDA,
                    USUARIO_ID,
                    DATA_SAIDA)
                VALUES(%s, %s, %s, %s, %s)
            """
            cursor.execute(sql, (
                saida.lote.id,
                saida.qtd_saida,
                saida.tipo_saida,
                saida.usuario.id,
                saida.data_saida
            ))
            conexao.commit()
            saida.id = cursor.lastrowid
            return saida
        except Exception:
            conexao.rollback()
            raise
        finally:
            self.desconectar(conexao, cursor)

    def update(self, saida):
        conexao, cursor = self.conectar()
        try:
            sql = """
                UPDATE SAIDA SET
                    LOTE_ID = %s,
                    QTD_SAIDA = %s,
                    TIPO_SAIDA = %s,
                    USUARIO_ID = %s,
                    DATA_SAIDA = %s
                WHERE ID = %s
            """
            cursor.execute(sql, (
                saida.lote.id,
                saida.qtd_saida,
                saida.tipo_saida,
                saida.usuario.id,
                saida.data_saida,
                saida.id
            ))
            conexao.commit()
            return cursor.rowcount > 0
        except Exception:
            conexao.rollback()
            raise
        finally:
            self.desconectar(conexao, cursor)

    def get_by_id(self, id):
        conexao, cursor = self.conectar()
        try:
            sql = """
                SELECT
                    s.id, s.qtd_saida, s.tipo_saida, s.data_saida,
                    l.id, l.numero_lote, l.validade,
                    m.id, m.nome, m.tipo, m.categoria, m.dosagem, m.ativo,
                    f.id, f.nome, f.cnpj, f.ativo,
                    u.id, u.nome, u.cpf, u.senha, u.cargo, u.data_entrada, u.ativo
                FROM SAIDA s
                JOIN LOTE l ON s.lote_id = l.id
                JOIN MEDICAMENTO m ON l.medicamento_id = m.id
                JOIN FORNECEDOR f ON l.fornecedor_id = f.id
                JOIN USUARIO u ON s.usuario_id = u.id
                WHERE s.id = %s
            """
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()
            if registro is None:
                return None
            return self._montar_saida(registro)
        finally:
            self.desconectar(conexao, cursor)

    def get_all(self):
        conexao, cursor = self.conectar()
        try:
            sql = """
                SELECT
                    s.id, s.qtd_saida, s.tipo_saida, s.data_saida,
                    l.id, l.numero_lote, l.validade,
                    m.id, m.nome, m.tipo, m.categoria, m.dosagem, m.ativo,
                    f.id, f.nome, f.cnpj, f.ativo,
                    u.id, u.nome, u.cpf, u.senha, u.cargo, u.data_entrada, u.ativo
                FROM SAIDA s
                JOIN LOTE l ON s.lote_id = l.id
                JOIN MEDICAMENTO m ON l.medicamento_id = m.id
                JOIN FORNECEDOR f ON l.fornecedor_id = f.id
                JOIN USUARIO u ON s.usuario_id = u.id
            """
            cursor.execute(sql)
            registros = cursor.fetchall()
            return [self._montar_saida(r) for r in registros]
        finally:
            self.desconectar(conexao, cursor)
            
    def delete(self, id):
        pass
        # saida não tem delete

    def _montar_saida(self, registro):
        medicamento = Medicamento(registro[7], registro[8], registro[9], registro[10], registro[11], registro[12])
        fornecedor = Fornecedor(registro[13], registro[14], registro[15], registro[16])
        lote = Lote(registro[4], registro[5], medicamento, fornecedor, registro[6])
        usuario = Usuario(registro[17], registro[18], registro[19], registro[20], registro[21], registro[22], registro[23])
        return Saida(registro[0], lote, registro[1], registro[2], usuario, registro[3])
