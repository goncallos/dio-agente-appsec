import sqlite3
from contextlib import closing


def login(usuario, senha, db_path="usuarios.db"):
    query = "SELECT * FROM usuarios WHERE usuario = ? AND senha = ?"
    with closing(sqlite3.connect(db_path)) as conn:
        return conn.execute(query, (usuario, senha)).fetchone()
