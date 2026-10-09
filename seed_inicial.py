"""
Seed inicial do SysFarm.

Cria o primeiro usuário do sistema (administrador) quando a tabela USUARIO
está vazia, para que seja possível fazer login na aplicação.

"""
import getpass
from datetime import date

from mysql.connector import IntegrityError

from app.core.database import Database
from app.dao.usuario_dao import Usuario_DAO
from app.models.usuario import Usuario

CARGO_PADRAO = "Administrador"


def limpar_cpf(cpf):
    # Mantém só os dígitos (aceita "123.456.789-09" ou "12345678909")
    return "".join(caractere for caractere in cpf if caractere.isdigit())


def criar_usuario_inicial(usuario_dao, nome, cpf, senha, cargo=CARGO_PADRAO):

    # Só cria se ainda não existir nenhum usuário ativo
    if usuario_dao.get_all():
        return None

    # Atenção: o login atual (Usuario_DAO.autenticar) compara a senha em
    # texto puro, então ela é salva do mesmo jeito. Se um dia o login passar
    # a usar hash, troque `senha` por `Senha_Utils.gerar_hash(senha)` aqui.
    usuario = Usuario(
        None,
        nome,
        cpf,
        senha,
        cargo,
        date.today()
    )

    return usuario_dao.save(usuario)


def main():

    database = Database()
    usuario_dao = Usuario_DAO(database)

    if usuario_dao.get_all():
        print("Já existem usuários cadastrados. Seed não é necessário.")
        return

    print("=== Criação do usuário administrador inicial ===")
    nome = input("Nome: ").strip()
    cpf = limpar_cpf(input("CPF (somente números): "))
    senha = getpass.getpass("Senha: ")

    if not nome or not cpf or not senha:
        print("Nome, CPF e senha são obrigatórios. Seed cancelado.")
        return

    if len(cpf) != 11:
        print("O CPF deve ter 11 dígitos. Seed cancelado.")
        return

    try:
        usuario = criar_usuario_inicial(usuario_dao, nome, cpf, senha)
    except IntegrityError:
        print("Já existe um usuário (inativo) com esse CPF. Seed cancelado.")
        return

    print()
    print(f"Usuário administrador criado com sucesso: {usuario.nome} (CPF {usuario.cpf})")
    print("Já pode fazer login na aplicação com essas credenciais.")


if __name__ == "__main__":
    main()
