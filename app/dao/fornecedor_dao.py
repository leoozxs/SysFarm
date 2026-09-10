from app.dao.dao import DAO
from app.models.fornecedor import Fornecedor

class Fornecedor_DAO(DAO):
    def __init__(self, database):
        super().__init__(database)
        
    def save(self, fornecedor):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        INSERT INTO FORNECEDOR(
                            NOME,
                            CNPJ,
                            ATIVO)
                        VALUES(
                            %s,
                            %s,
                            %s)
                    """
            cursor.execute(sql, (fornecedor.nome,
                                 fornecedor.cnpj,
                                 fornecedor.ativo))
            conexao.commit()
            fornecedor.id = cursor.lastrowid
            return fornecedor
        except Exception as e:
            conexao.rollback()
            raise
        finally:
            self.desconectar(conexao, cursor)
            
    def update(self, fornecedor):
        conexao, cursor = self.conectar()
        try:    
            sql =   """
                    UPDATE FORNECEDOR SET
                        NOME = %s,
                        CNPJ = %s,
                        ATIVO = %s
                    WHERE
                        ID = %s
                    """
            cursor.execute(sql, (fornecedor.nome,
                                 fornecedor.cnpj,
                                 fornecedor.ativo,
                                 fornecedor.id))
            conexao.commit()
            return fornecedor
        except Exception as e:
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
                            NOME,
                            CNPJ,
                            ATIVO
                        FROM 
                            FORNECEDOR
                        WHERE 
                            ID = %s AND
                            ATIVO = True
                    """
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()
            if registro is None:
                return None
            return Fornecedor(
                registro[0],
                registro[1],
                registro[2],
                registro[3]
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
                            CNPJ,
                            ATIVO
                        FROM
                            FORNECEDOR
                        WHERE
                            ATIVO = True                        
                    """
            cursor.execute(sql)
            registros = cursor.fetchall()
            fornecedores = []
            
            for registro in registros:
                fornecedores.append(Fornecedor(
                    registro[0],
                    registro[1],
                    registro[2],
                    registro[3]
                ))
            return fornecedores
        finally:
            self.desconectar(conexao, cursor)
            
    def delete(self, id):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        UPDATE FORNECEDOR SET
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