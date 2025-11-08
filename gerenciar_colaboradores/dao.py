from database.connection import get_connection

# ============================================================
# 🔹 COLABORADORES
# ============================================================

def listar_colaboradores():
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT id, nome, telefone, cidade, estado, tecnologias
        FROM colaboradores
    """)
    colunas = [desc[0] for desc in cursor.description]
    dados = [dict(zip(colunas, linha)) for linha in cursor.fetchall()]
    conexao.close()
    return dados


def buscar_colaborador_por_id(id_colaborador: int):
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT id, nome, telefone, cidade, estado, tecnologias
        FROM colaboradores
        WHERE id = ?
    """, (id_colaborador,))
    linha = cursor.fetchone()
    conexao.close()
    if linha:
        colunas = ["id", "nome", "telefone", "cidade", "estado", "tecnologias"]
        return dict(zip(colunas, linha))
    return None


# ============================================================
# 🔹 COLABORADOR_PROJETO
# ============================================================

def listar_colaboradores_projetos():
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT id_projeto, id_colaborador, status
        FROM colaborador_projeto
    """)
    colunas = [desc[0] for desc in cursor.description]
    dados = [dict(zip(colunas, linha)) for linha in cursor.fetchall()]
    conexao.close()
    return dados


def listar_por_projeto(id_projeto: int):
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("""
        SELECT cp.id_colaborador, c.nome, c.tecnologias, cp.status
        FROM colaborador_projeto cp
        JOIN colaboradores c ON cp.id_colaborador = c.id
        WHERE cp.id_projeto = ?
    """, (id_projeto,))
    colunas = [desc[0] for desc in cursor.description]
    dados = [dict(zip(colunas, linha)) for linha in cursor.fetchall()]
    conexao.close()
    return dados


def atualizar_status(id_projeto: int, id_colaborador: int, novo_status: str):
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("""
        UPDATE colaborador_projeto
        SET status = ?
        WHERE id_projeto = ? AND id_colaborador = ?
    """, (novo_status, id_projeto, id_colaborador))
    conexao.commit()
    alterados = cursor.rowcount
    conexao.close()
    return alterados > 0


def deletar_relacao(id_projeto: int, id_colaborador: int):
    conexao = get_connection()
    cursor = conexao.cursor()
    cursor.execute("""
        DELETE FROM colaborador_projeto
        WHERE id_projeto = ? AND id_colaborador = ?
    """, (id_projeto, id_colaborador))
    conexao.commit()
    apagados = cursor.rowcount
    conexao.close()
    return apagados > 0
