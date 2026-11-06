
import sqlite3

# Banco de dados local para fins educacionais
conexao = sqlite3.connect("laboratorio.db")
cursor = conexao.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT NOT NULL,
    senha TEXT NOT NULL
)
""")

cursor.execute("DELETE FROM usuarios")
cursor.execute(
    "INSERT INTO usuarios (usuario, senha) VALUES ('admin', 'senha123')"
)
conexao.commit()

def login(usuario, senha):
    # VULNERABILIDADE: concatenação direta dos dados na consulta SQL
    consulta = (
        "SELECT * FROM usuarios "
        f"WHERE usuario = '{usuario}' AND senha = '{senha}'"
    )

    print("Consulta executada:", consulta)
    cursor.execute(consulta)

    return cursor.fetchone()

usuario = input("Usuário: ")
senha = input("Senha: ")

resultado = login(usuario, senha)

if resultado:
    print("Login realizado!")
else:
    print("Usuário ou senha incorretos.")

conexao.close()
