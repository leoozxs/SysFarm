from app.dao.dao import DAO
from app.models.usuario import Usuario

class Usuario_DAO(DAO):
    def __init__(self, database):
        super().__init__(database)

    def save(self, usuario):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        INSERT INTO USUARIO(
                            NOME,
                            CPF,
                            SENHA,
                            CARGO,
                            DATA_ENTRADA,
                            ATIVO)
                        VALUES(
                            %s,
                            %s,
                            %s,
                            %s,
                            %s,
                            %s)
                    """
            cursor.execute(sql, (usuario.nome,
                                usuario.cpf,
                                usuario.senha,
                                usuario.cargo,
                                usuario.data_entrada,
                                usuario.ativo))
            conexao.commit()
            usuario.id = cursor.lastrowid
            return usuario
        except Exception as e:
            conexao.rollback()
            raise
        finally:
            self.desconectar(conexao, cursor)

    def update(self, usuario):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        UPDATE USUARIO SET
                            NOME = %s,
                            CPF = %s,
                            SENHA = %s,
                            CARGO = %s,
                            DATA_ENTRADA = %s,
                            ATIVO = %s
                        WHERE
                            ID = %s
                    """
            cursor.execute(sql, (usuario.nome,
                                 usuario.cpf,
                                 usuario.senha,
                                 usuario.cargo,
                                 usuario.data_entrada,
                                 usuario.ativo,
                                 usuario.id))
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
                            NOME,
                            CPF,
                            SENHA,
                            CARGO,
                            DATA_ENTRADA,
                            ATIVO
                        FROM 
                            USUARIO
                        WHERE
                            ID = %s AND 
                            ATIVO = True                  
                    """
            cursor.execute(sql, (id,))
            registro = cursor.fetchone()
            if registro is None:
                return None
            return Usuario(
                registro[0],
                registro[1],
                registro[2],
                registro[3],
                registro[4],
                registro[5],
                registro[6]
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
                            CPF,
                            SENHA,
                            CARGO,
                            DATA_ENTRADA,
                            ATIVO
                        FROM 
                            USUARIO
                        WHERE 
                            ATIVO = True
                    """
            cursor.execute(sql)
            registros = cursor.fetchall()
            usuarios = []

            for registro in registros:
                usuarios.append(Usuario(
                    registro[0],
                    registro[1],
                    registro[2],
                    registro[3],
                    registro[4],
                    registro[5],
                    registro[6]
                ))
            return usuarios
        finally:
            self.desconectar(conexao, cursor)

    def delete(self, id):
        conexao, cursor = self.conectar()
        try:
            sql =   """
                        UPDATE USUARIO SET
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
        