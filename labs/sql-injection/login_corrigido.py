"""
login_corrigido.py
==================
Versão segura do laboratório de login com SQLite.

Correções aplicadas:
  1. Consultas parametrizadas em todas as operações SQL.
  2. Senha armazenada como hash PBKDF2-HMAC-SHA256 (salt aleatório + iterações).
  3. Comparação em tempo constante (hmac.compare_digest).
  4. Inicialização idempotente: não apaga usuários existentes.
  5. Autenticação com tratamento de erros do SQLite.
  6. Validação básica de entrada e leitura secreta da senha (getpass).

Pré-requisitos: apenas a biblioteca padrão do Python.
"""

import getpass
import hashlib
import hmac
import logging
import secrets
import sqlite3
import sys

# --------------------------------------------------------------------------- #
# Configuração
# --------------------------------------------------------------------------- #

logging.basicConfig(
    level=logging.WARNING,
    format="%(levelname)s: %(message)s",
)
logger = logging.getLogger("login")

DB_PATH = "laboratorio.db"

# Políticas de entrada
MAX_USUARIO = 64
MAX_SENHA = 256

# Configurações do hash (PBKDF2-HMAC-SHA256)
ITERACOES = 100_000
TAM_SALT = 16  # bytes


# --------------------------------------------------------------------------- #
# Criptografia de senha
# --------------------------------------------------------------------------- #

def gerar_hash_senha(senha: str) -> str:
    """Gera um hash saltante para a senha.

    Formato de retorno: "<salt_hex>$<dk_hex>"
    """
    salt = secrets.token_bytes(TAM_SALT)
    dk = hashlib.pbkdf2_hmac(
        "sha256",
        senha.encode("utf-8"),
        salt,
        ITERACOES,
    )
    return f"{salt.hex()}${dk.hex()}"


def verificar_senha(senha: str, hash_salvo: str) -> bool:
    """Compara a senha com o hash armazenado, em tempo constante."""
    try:
        salt_hex, dk_hex = hash_salvo.split("$")
        salt = bytes.fromhex(salt_hex)
        dk_esperado = bytes.fromhex(dk_hex)
    except (ValueError, AttributeError):
        # Hash corrompido ou em formato inválido
        return False

    dk_calculado = hashlib.pbkdf2_hmac(
        "sha256",
        senha.encode("utf-8"),
        salt,
        ITERACOES,
    )
    return hmac.compare_digest(dk_calculado, dk_esperado)


# Valor "falso" usado para equalizar o tempo de execução quando o usuário
# não existe no banco, dificultando ataques por análise de tempo (timing).
_DUMMY_HASH = "0" * (TAM_SALT * 2) + "$" + "0" * 64


# --------------------------------------------------------------------------- #
# Acesso ao banco de dados
# --------------------------------------------------------------------------- #

def inicializar_banco(conexao: sqlite3.Connection) -> None:
    """Cria a tabela e seeda o administrador, se necessário.

    Idempotente: não apaga nem substitui usuários já existentes.
    """
    try:
        conexao.execute(
            """
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT NOT NULL UNIQUE,
                senha TEXT NOT NULL
            )
            """
        )
        conexao.execute(
            "INSERT OR IGNORE INTO usuarios (usuario, senha) VALUES (?, ?)",
            ("admin", gerar_hash_senha("senha123")),
        )
        conexao.commit()
    except sqlite3.Error as exc:
        conexao.rollback()
        logger.error("Falha ao inicializar o banco de dados: %s", exc)
        raise


def buscar_hash_senha(usuario: str, conexao: sqlite3.Connection) -> str | None:
    """Retorna o hash de senha salvo para o usuário ou None se não existir.

    Query parametrizada: o valor de ``usuario`` nunca entra na estrutura SQL.
    """
    try:
        cursor = conexao.execute(
            "SELECT senha FROM usuarios WHERE usuario = ?",
            (usuario,),
        )
        registro = cursor.fetchone()
    except sqlite3.Error as exc:
        logger.error("Erro ao consultar usuário no banco: %s", exc)
        return None
    return registro[0] if registro else None


def autenticar(usuario: str, senha: str, conexao: sqlite3.Connection) -> bool:
    """Autentica um usuário. Retorna True se a senha for válida."""
    if not usuario or not senha:
        return False
    if len(usuario) > MAX_USUARIO or len(senha) > MAX_SENHA:
        return False

    hash_salvo = buscar_hash_senha(usuario, conexao)

    if hash_salvo is None:
        # Verifica contra um hash falso para não dar pistas via Timing.
        return verificar_senha(senha, _DUMMY_HASH)

    return verificar_senha(senha, hash_salvo)


# --------------------------------------------------------------------------- #
# Execução do programa
# --------------------------------------------------------------------------- #

def main() -> None:
    """Loop de autenticação (executado apenas quando o script é chamado
    diretamente, não quando importado)."""
    try:
        conexao = sqlite3.connect(DB_PATH)
    except sqlite3.Error as exc:
        logger.error("Não foi possível abrir o banco de dados: %s", exc)
        sys.exit(1)

    try:
        inicializar_banco(conexao)
    except sqlite3.Error:
        conexao.close()
        sys.exit(1)

    try:
        print("=== Laboratório de Login Seguro ===")
        usuario = input("Usuário: ")
        senha = getpass.getpass("Senha: ")

        if autenticar(usuario, senha, conexao):
            print("Login realizado!")
        else:
            print("Usuário ou senha incorretos.")
    except (EOFError, KeyboardInterrupt):
        print("\nOperação cancelada.")
    finally:
        conexao.close()


if __name__ == "__main__":
    main()
