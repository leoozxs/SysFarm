from app.dao.dao import DAO
from app.models.lote import Lote

class Lote_DAO(DAO):
    def __init__(self, database):
        super().__init__(database)
        
    def save(self, lote):
        conexao, cursor = self.conectar()
        try:    
            sql =   """
                        INSERT INTO LOTE(
                            NUMERO_LOTE,
                            MEDICAMENTO_ID,
                            FORNECEDOR_ID,
                            VALIDADE)
                        VALUES(
                            %s
                            %s
                            %s
                            %s)
                    """
            cursor.execute(sql, (lote.numero_lote,
                                 lote.medicamento_id,
                                 lote.fornecedor_id,
                                 lote.validade))
            conexao.commit()
            lote.id = cursor.lastrowid
            return lote
        except Exception as e:
            conexao.rollback()
            raise
        finally:
            self.desconectar(conexao, cursor)
            
    def update(self, lote):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        UPDATE LOTE SET
                            NUMERO_LOTE = %s,
                            MEDICAMENTO_ID = %s,
                            FORNECEDOR_ID = %s,
                            VALIDADE = %s
                        WHERE
                            ID = %s
                    """
            cursor.execute(sql, (lote.numero_lote,
                                 lote.medicamento_id,
                                 lote.fornecedor_id,
                                 lote.validade,
                                 lote.id))
            conexao.commit()
            return cursor.rowcount > 0
        except Exception as e:
            conexao.rollback()
            raise
        finally:
            self.desconectar(conexao, cursor)
            
    def get_by_id(self, lote_id):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        SELECT
                            ID,
                            NUMERO_LOTE,
                            MEDICAMENTO_ID,
                            FORNECEDOR_ID,
                            VALIDADE
                        FROM 
                            LOTE
                        WHERE
                            ID = %s    
                    """
            cursor.execute(sql, (lote_id,))
            registro = cursor.fetchone()
            if registro is None:
                return None
            return Lote(
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
            sql =   """
                        SELECT
                            ID,
                            NUMERO_LOTE,
                            MEDICAMENTO_ID,
                            FORNECEDOR_ID,
                            VALIDADE
                        FROM 
                            LOTE
                    """
            cursor.execute(sql)
            registros = cursor.fetchall()
            lotes = []
            
            for registro in registros:
                lote = Lote(
                    registro[0],
                    registro[1],
                    registro[2],
                    registro[3],
                    registro[4]
                )
                lotes.append(lote)
            return lotes
        finally:
            self.desconectar(conexao, cursor)
            
    def delete(self, lote_id):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        UPDATE LOTE
                        SET ATIVO = FALSE
                        WHERE ID = %s

                    """
            cursor.execute(sql, (lote_id,))
            conexao.commit()
            return cursor.rowcount > 0
        except Exception as e:
            conexao.rollback()
            raise
        finally:
            self.desconectar(conexao, cursor) #ajustar