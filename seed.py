import getpass
from datetime import date

from app.core.database import Database
from app.dao.usuario_dao import Usuario_DAO
from app.models.usuario import Usuario


def criar_usuario_inicial(usuario_dao, nome, cpf, senha):
    if usuario_dao.get_all():
        return None

    usuario = Usuario(None, nome, cpf, senha, "SemiDeusDoSisteminha", date.today())
    return usuario_dao.save(usuario)


def main():
    usuario_dao = Usuario_DAO(Database())

    if usuario_dao.get_all():
        print("Já existem usuários cadastrados. Seed não é necessário.")
        return

    print("=== Criação do usuário administrador inicial ===")
    nome = input("Nome: ").strip()
    cpf = input("CPF (somente números): ").strip()
    senha = getpass.getpass("Senha: ")

    if not nome or not cpf or not senha:
        print("Nome, CPF e senha são obrigatórios. Seed cancelado.")
        return

    if not cpf.isdigit() or len(cpf) != 11:
        print("O CPF deve ter 11 números. Seed cancelado.")
        return

    usuario = criar_usuario_inicial(usuario_dao, nome, cpf, senha)

    print()
    print(f"Usuário administrador criado com sucesso: {usuario.nome} (CPF {usuario.cpf})")
    print("Já pode fazer login na aplicação com essas credenciais.")


if __name__ == "__main__":
    main()