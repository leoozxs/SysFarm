from app.dao.dao import DAO
from app.models.entrada import Entrada
from app.models.lote import Lote
from app.models.medicamento import Medicamento
from app.models.fornecedor import Fornecedor
from app.models.usuario import Usuario

class Entrada_DAO(DAO):
    def __init__(self, database):
        super().__init__(database)
        
    def save(self, entrada):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        INSERT INTO ENTRADA(
                            LOTE_ID,
                            QTD_ENTRADA,
                            DATA_ENTRADA,
                            USUARIO_ID)
                        VALUES(
                            %s,
                            %s,
                            %s,
                            %s)
                    """
            cursor.execute(sql, (entrada.lote.id,
                                 entrada.qtd_entrada,
                                 entrada.data_entrada,
                                 entrada.usuario.id))
            conexao.commit()
            entrada.id = cursor.lastrowid
            return entrada
        except Exception as e:
            conexao.rollback()
            raise
        finally:
            self.desconectar(conexao, cursor)
            
    def update(self, entrada):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        UPDATE ENTRADA SET
                            LOTE_ID = %s,
                            QTD_ENTRADA = %s,
                            DATA_ENTRADA = %s,
                            USUARIO_ID = %s
                        WHERE 
                            ID = %s
                    """
            cursor.execute(sql, (entrada.lote.id,
                                 entrada.qtd_entrada,
                                 entrada.data_entrada,
                                 entrada.usuario.id,
                                 entrada.id))
            conexao.commit()
            return cursor.rowcount > 0
        except Exception:
            conexao.rollback()
            raise
        finally:
            self.desconectar(conexao, cursor)
            
    def get_by_id(self, id):
        try:
            conexao, cursor = self.conectar()
            sql =   """
                        SELECT
                            e.id, e.qtd_entrada, e.data_entrada,
                            l.id, l.numero_lote, l.validade,
                            m.id, m.nome, m.tipo, m.categoria, m.dosagem, m.ativo,
                            f.id, f.nome, f.cnpj, f.ativo,
                            u.id, u.nome, u.cpf, u.senha, u.cargo, u.data_entrada, u.ativo
                        FROM ENTRADA e
                        JOIN LOTE l ON e.lote_id = l.id
                        JOIN MEDICAMENTO m ON l.medicamento_id = m.id
                        JOIN FORNECEDOR f ON l.fornecedor_id = f.id
                        JOIN USUARIO u ON e.usuario_id = u.id
                        WHERE e.id = %s
                    """
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()
            if registro is None:
                return None
            return self._montar_entrada(registro)
        finally:
            self.desconectar(conexao, cursor)
            
    def get_all(self):
        conexao, cursor = self.conectar()
        try:
            sql =  """
                        SELECT
                            e.id, e.qtd_entrada, e.data_entrada,
                            l.id, l.numero_lote, l.validade,
                            m.id, m.nome, m.tipo, m.categoria, m.dosagem, m.ativo,
                            f.id, f.nome, f.cnpj, f.ativo,
                            u.id, u.nome, u.cpf, u.senha, u.cargo, u.data_entrada, u.ativo
                        FROM ENTRADA e
                        JOIN LOTE l ON e.lote_id = l.id
                        JOIN MEDICAMENTO m ON l.medicamento_id = m.id
                        JOIN FORNECEDOR f ON l.fornecedor_id = f.id
                        JOIN USUARIO u ON e.usuario_id = u.id
                    """
            cursor.execute(sql)
            registros = cursor.fetchall()
            return [self._montar_entrada(r) for r in registros]
        finally:
            self.desconectar(conexao, cursor)

    def _montar_entrada(self, registro):
        medicamento = Medicamento(registro[6], registro[7], registro[8], registro[9], registro[10], registro[11])
        fornecedor = Fornecedor(registro[12], registro[13], registro[14], registro[15])
        lote = Lote(registro[3], registro[4], medicamento, fornecedor, registro[5])
        usuario = Usuario(registro[16], registro[17], registro[18], registro[19], registro[20], registro[21], registro[22])
        return Entrada(registro[0], lote, registro[1], registro[2], usuario)
            
    def delete(self, id):
        raise NotImplementedError(
        "Registros de entrada não podem ser excluídos."
    )