# database/init_db.py
from database.connection import get_connection

def criar_tabelas():
    conn = get_connection()
    cursor = conn.cursor()

    # --- Tabela de usuários ---
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    );
    """)

    # --- Tabela de colaboradores ---
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS colaboradores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        telefone TEXT,
        descricao TEXT,
        cidade TEXT,
        estado TEXT,
        horas_disponiveis INTEGER,
        tecnologias TEXT,
        interesses TEXT,
        portfolio TEXT
    );
    """)

    # --- Tabela de projetos ---
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS projetos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        id_idealizador INTEGER,
        nivel TEXT,
        categoria TEXT,
        descricao TEXT,           
        status TEXT
    );
    """)

    # --- Tabela de tecnologias ---
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tecnologias (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        id_projeto INTEGER,
        FOREIGN KEY (id_projeto) REFERENCES projetos(id)
    );
    """)

    # --- Tabela de repositórios ---
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS repositorios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        id_projeto INTEGER,
        FOREIGN KEY (id_projeto) REFERENCES projetos(id)
    );
    """)

    # --- Tabela de colaborador_projeto ---
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS colaborador_projeto (
        id_projeto INTEGER,
        id_colaborador INTEGER,
        status TEXT DEFAULT 'ativo',
        PRIMARY KEY (id_projeto, id_colaborador),
        FOREIGN KEY (id_projeto) REFERENCES projetos(id),
        FOREIGN KEY (id_colaborador) REFERENCES colaboradores(id)
    );
    """)

    conn.commit()
    conn.close()
    print("✅ Banco de dados inicializado com sucesso!")

if __name__ == "__main__":
    criar_tabelas()
