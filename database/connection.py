# database/connection.py
import sqlite3
from pathlib import Path

# Caminho do banco (cria automaticamente se não existir)
DB_PATH = Path(__file__).resolve().parent.parent / "meusistema.db"

def get_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row  # Permite acessar colunas por nome
    return conn
