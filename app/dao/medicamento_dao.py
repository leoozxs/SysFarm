from app.dao.dao import DAO
from app.models.medicamento import Medicamento

class Medicamento_DAO(DAO):
    def __init__(self, database):
        super().__init__(database)
        
    def save(self, medicamento):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                    INSERT INTO MEDICAMENTO(
                        NOME,
                        TIPO,
                        CATEGORIA,
                        DOSAGEM,
                        ATIVO)
                    VALUES(
                        %s,
                        %s,
                        %s,
                        %s,
                        %s)
                    """
            cursor.execute(sql, (medicamento.nome,
                                 medicamento.tipo,
                                 medicamento.categoria,
                                 medicamento.dosagem,
                                 medicamento.ativo))
            conexao.commit()
            medicamento.id = cursor.lastrowid
            return medicamento
        except Exception as e:
            conexao.rollback()
            raise
        finally:
            self.desconectar(conexao, cursor)
            
    def update(self, medicamento):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        UPDATE MEDICAMENTO SET
                            NOME = %s,
                            TIPO = %s,
                            CATEGORIA = %s,
                            DOSAGEM = %s,
                            ATIVO = %s
                        WHERE
                            ID = %s
                    """
            cursor.execute(sql, (medicamento.nome,
                                 medicamento.tipo,
                                 medicamento.categoria,
                                 medicamento.dosagem,
                                 medicamento.ativo,
                                 medicamento.id))
            conexao.commit()
            return cursor.rowcount > 0
        except Exception as e:
            conexao.rollback()
            raise
        finally:
            self.desconectar(conexao, cursor)
            
    def get_by_id(self, id):
        conexao, cursor = self.conectar()
        try:
            sql = """
                    SELECT
                        ID,
                        NOME,
                        TIPO,
                        CATEGORIA,
                        DOSAGEM,
                        ATIVO
                    FROM
                        MEDICAMENTO
                    WHERE
                        ID = %s
                        AND ATIVO = True
                    """
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()
            if registro is None:
                return None
            return Medicamento(
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
                            NOME,
                            TIPO,
                            CATEGORIA,
                            DOSAGEM,
                            ATIVO
                        FROM
                            MEDICAMENTO
                        WHERE
                            ATIVO = True
                    """
            cursor.execute(sql)
            registros = cursor.fetchall()
            medicamentos = []
            
            for registro in registros:
                medicamentos.append(Medicamento(
                    registro[0],
                    registro[1],
                    registro[2],
                    registro[3],
                    registro[4],
                    registro[5]
                ))
            return medicamentos
        finally:
            self.desconectar(conexao, cursor)
            
    def delete(self, id):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        UPDATE MEDICAMENTO SET
                            ATIVO = False
                        WHERE
                            ID = %s
                    """
            cursor.execute(sql,(id,))
            conexao.commit()
        except Exception:
            conexao.rollback()
            raise
        finally:
            self.desconectar(conexao, cursor)            