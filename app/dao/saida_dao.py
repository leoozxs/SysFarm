from app.dao.dao import DAO
from app.models.saida import Saida

class Saida_DAO(DAO):
    def __init__(self, database):
        super().__init__ (database)
        
    def save (self, saida):
        conexao, cursor = self.conectar
        try:
            sql =   """
                        INSERT INTO SAIDA(
                            LOTE_ID,
                            QTD_SAIDA,
                            DATA_SAIDA,
                            TIPO_SAIDA,
                            USUARIO_ID)
                        VALUES(
                            %s,
                            %s,
                            %s,
                            %s,
                            %s)
                    """
            cursor.execute(sql, (saida.lote_id,
                                 saida.qtd_saida,
                                 saida.data_saida,
                                 saida.tipo_saida,
                                 saida.usuario_id))
            conexao.commit()
            saida.id = cursor.lastrowid
            return saida
        except Exception as e:
            conexao.rollback()
            raise
        finally:
            self.desconectar(conexao, cursor)
            
    def update(self, saida):
        conexao, cursor = self.conectar
        try:
            sql =   """
                        UPDATE SAIDA SET
                            LOTE_ID = %s,
                            QTD_SAIDA = %s,
                            DATA_SAIDA = %s,
                            TIPO_SAIDA = %s,
                            USUARIO_ID = %s
                        WHERE 
                            ID = %s
                    """
            cursor.execute(sql, (saida.lote_id,
                                 saida.qtd_saida,
                                 saida.data_saida,
                                 saida.tipo_saida,
                                 saida.usuario_id,
                                 saida.id))
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
            sql =   """
                        SELECT
                            ID,
                            LOTE_ID,
                            QTD_SAIDA,
                            DATA_SAIDA,
                            TIPO_SAIDA,
                            USUARIO_ID
                        FROM
                            SAIDA
                        WHERE
                            ID = %s
                    """
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()
            if registro is None:
                return None
            return Saida(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
                registro[4],
                registro[5]
            )
        finally:
            self.desconectar(conexao, cursor)
            
    def get_all(self):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        SELECT
                            ID,
                            LOTE_ID,
                            QTD_SAIDA,
                            DATA_SAIDA,
                            TIPO_SAIDA,
                            USUARIO_ID
                        FROM 
                            SAIDA
                    """
            cursor.execute(sql)
            registros = cursor.fetchall()
            saidas = []
            for registro in registros:
                saida = Saida(
                    registro[0],
                    registro[1],
                    registro[2],
                    registro[3],
                    registro[4],
                    registro[5]
                )
                saidas.append(saida)
            return saidas
        finally:
            self.desconectar(conexao, cursor)
            
    def delete(self, id):
        raise NotImplementedError(
        "Registros de entrada não podem ser excluídos."
    )