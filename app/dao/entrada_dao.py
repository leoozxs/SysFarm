from app.dao.dao import DAO
from app.models.entrada import Entrada

class Entrada_DAO(DAO):
    def __init__(self, database):
        super().__init__(database)
        
    def save(self, entrada):
        conexao, cursor = self.conectar
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
            cursor.execute(sql, (entrada.lote_id,
                                 entrada.qtd_entrada,
                                 entrada.data_entrada,
                                 entrada.usuario_id))
            conexao.commit()
            entrada.id = cursor.lastrowid
            return entrada
        except Exception as e:
            conexao.rollback()
            raise
        finally:
            self.desconectar(conexao, cursor)
            
    def update(self, entrada):
        conexao, cursor = self.conectar
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
            cursor.execute(sql, (entrada.lote_id,
                                 entrada.qtd_entrada,
                                 entrada.data_entrada,
                                 entrada.usuario_id,
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
                            ID,
                            LOTE_ID,
                            QTD_ENTRADA,
                            DATA_ENTRADA,
                            USUARIO_ID
                        FROM
                            ENTRADA
                        WHERE
                            ID = %s
                    """
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()
            if registro is None:
                return None
            return Entrada(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
                registro[4]
            )
        finally:
            self.desconectar(conexao, cursor)
            
    def get_all(self):
        conexao, cursor = self.conectar()
        try:
            sql =  """
                        SELECT
                            ID,
                            LOTE_ID,
                            QTD_ENTRADA,
                            DATA_ENTRADA,
                            USUARIO_ID
                        FROM 
                            ENTRADA
                    """
            cursor.execute(sql)
            registros = cursor.fetchall()
            entradas = []
            for registro in registros:
                entrada = Entrada(
                    registro[0],
                    registro[1],
                    registro[2],
                    registro[3],
                    registro[4]
                )
                entradas.append(entrada)
            return entradas
        finally:
            self.desconectar(conexao, cursor)
            
    def delete(self, id):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                            DELETE FROM entrada
                            WHERE 
                                id = %s
                    """
            cursor.execute(sql, (id,))
            conexao.commit()
        except Exception:
            conexao.rollback()
            raise
        finally:
            self.desconectar(conexao, cursor)
            