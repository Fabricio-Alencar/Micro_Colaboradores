from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from gerenciar_colaboradores import dao


router = APIRouter(tags=["Colaboradores & Colaborações"])


# ============================================================
# 🔹 MODELOS Pydantic
# ============================================================
class AtualizarStatus(BaseModel):
    status: str


class CriarRelacao(BaseModel):
    id_projeto: int
    id_colaborador: int
    status: str = "Solicitado"

class CriarColaborador(BaseModel):
    nome: str
    telefone: str | None = None
    descricao: str | None = None
    cidade: str | None = None
    estado: str | None = None
    horas_disponiveis: int | None = None
    tecnologias: str | None = None
    interesses: str | None = None
    portfolio: str | None = None


class CriarRelacao(BaseModel):
    id_projeto: int
    id_colaborador: int
    status: str = "Solicitado"


# ============================================================
# 🔹 ENDPOINTS DE CRIAÇÃO
# ============================================================

@router.post("/colaboradores")
def criar_colaborador(dados: CriarColaborador):
    """Cria um novo colaborador."""
    colaborador_id = dao.criar_colaborador(dados)
    if not colaborador_id:
        raise HTTPException(status_code=500, detail="Erro ao criar colaborador")
    return {"mensagem": "Colaborador criado com sucesso!", "id_colaborador": colaborador_id}


@router.post("/colaborador_projeto/{id_projeto}/{id_colaborador}")
def criar_relacao(id_projeto: int, id_colaborador: int, status: str = "Solicitado"):
    status = "Solicitado"
    sucesso = dao.criar_relacao(id_projeto, id_colaborador, status)
    if not sucesso:
        raise HTTPException(status_code=400, detail="Não foi possível criar a relação. Verifique IDs.")
    return {"mensagem": "Relação criada com sucesso!"}










# ============================================================
# 🔹 COLABORADORES
# ============================================================

@router.get("/colaboradores")
def listar_colaboradores():
    """Retorna todos os colaboradores cadastrados."""
    colaboradores = dao.listar_colaboradores()
    if not colaboradores:
        raise HTTPException(status_code=404, detail="Nenhum colaborador encontrado")
    return {"colaboradores": colaboradores}


@router.get("/colaboradores/{id_colaborador}")
def buscar_colaborador(id_colaborador: int):
    """Busca um colaborador específico pelo ID."""
    colaborador = dao.buscar_colaborador_por_id(id_colaborador)
    if not colaborador:
        raise HTTPException(status_code=404, detail="Colaborador não encontrado")
    return {"colaborador": colaborador}


# ============================================================
# 🔹 COLABORADOR ↔ PROJETO
# ============================================================

@router.get("/colaborador_projeto")
def listar_todos():
    """Lista todos os vínculos entre colaboradores e projetos."""
    relacoes = dao.listar_colaboradores_projetos()
    if not relacoes:
        raise HTTPException(status_code=404, detail="Nenhum vínculo encontrado")
    return {"colaborador_projeto": relacoes}


@router.get("/colaborador_projeto/projeto/{id_projeto}")
def listar_por_projeto(id_projeto: int):
    relacoes = dao.listar_por_projeto(id_projeto)
    if not relacoes:
        raise HTTPException(status_code=404, detail="Nenhum colaborador vinculado a este projeto")
    return {"colaboradores": relacoes}


@router.put("/colaborador_projeto/{id_projeto}/{id_colaborador}")
def atualizar_status(id_projeto: int, id_colaborador: int, dados: AtualizarStatus):
    """Atualiza o status de um colaborador em um projeto."""
    atualizado = dao.atualizar_status(id_projeto, id_colaborador, dados.status)
    if not atualizado:
        raise HTTPException(status_code=404, detail="Relação não encontrada")
    return {"mensagem": f"Status atualizado para '{dados.status}' com sucesso!"}


@router.delete("/colaborador_projeto/{id_projeto}/{id_colaborador}")
def deletar_relacao(id_projeto: int, id_colaborador: int):
    """Remove um colaborador de um projeto."""
    sucesso = dao.deletar_relacao(id_projeto, id_colaborador)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Relação não encontrada")
    return {"mensagem": "Colaborador removido do projeto com sucesso!"}
