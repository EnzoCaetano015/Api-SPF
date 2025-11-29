from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from connection import bdConect

router = APIRouter()


class UpdateScore(BaseModel):
    pontos: int

class LoginData(BaseModel):
    usuario: str
    senha: str


@router.get("/")
def check_database():
    connection = bdConect()
    if bdConect():
        return {"message": "Conectado ao banco de dados"}
    else:
        return {"message": "Não foi possível conectar ao banco de dados"}
    

@router.get("/times")
def get_teams():
    conn = bdConect()
    if not conn:
        raise HTTPException(status_code=500, detail="Falha na conexão com o banco")

    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT time.id, time.nome AS name, pontuacao.pontos AS points
        FROM time
        INNER JOIN pontuacao ON time.idPontos = pontuacao.id
    """)
    times = cursor.fetchall()
    cursor.close()
    conn.close()
    return times


@router.put("/times/{team_id}/pontuacao")
def update_score(team_id: int, payload: UpdateScore):
    conn = bdConect()
    if not conn:
        raise HTTPException(
            status_code=500, detail="Falha na conexão com o banco")

    cursor = conn.cursor(dictionary=True)
    # 1) Busca o time
    cursor.execute("SELECT idPontos FROM `time` WHERE id = %s", (team_id,))
    time_row = cursor.fetchone()
    if not time_row:
        cursor.close()
        conn.close()
        raise HTTPException(status_code=404, detail="Time não encontrado")

    id_pontos = time_row["idPontos"]
    # 2) Atualiza a pontuação
    cursor.execute(
        "UPDATE pontuacao SET pontos = %s WHERE id = %s",
        (payload.pontos, id_pontos)
    )
    conn.commit()

    # 3) Retorna o registro atualizado
    cursor.execute(
        "SELECT id, pontos FROM pontuacao WHERE id = %s", (id_pontos,))
    updated = cursor.fetchone()

    cursor.close()
    conn.close()

    return {"id": updated["id"], "pontos": updated["pontos"]}


@router.post("/login")
def login(data: LoginData):
    conn = bdConect()
    if not conn:
        raise HTTPException(
            status_code=500, detail="Falha na conexão com o banco")

    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT usuario FROM usuario WHERE usuario = %s AND senha = %s",
        (data.usuario, data.senha)
    )
    user = cursor.fetchone()
    cursor.close()
    conn.close()

    if not user:
        raise HTTPException(
            status_code=401, detail="Usuário ou senha inválidos")
    return {"message": "Login bem-sucedido"}
