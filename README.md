
# 🚀 API – SPF 2025 (Semana Paulo Freire)

API oficial utilizada pelo site da **Semana Paulo Freire — ETEC Maria Cristina Medeiros**, responsável por autenticação, ranking de equipes e gerenciamento de pontuação.

---

## 📦 Tecnologias Utilizadas
- **FastAPI**
- **MySQL**
- **mysql-connector-python**
- **Pydantic**
- **Uvicorn**
- **Docker**
- **dotenv (.env)**

---

## 📁 Estrutura do Projeto
```
api/
 ├── main.py
 ├── route.py
 ├── connection.py
 ├── Dockerfile
 ├── .dockerignore
 └── .env (necessário criar)
```

---

# 🔌 Endpoints da API

## 🏁 Checar Conexão
```
GET /
```

## 📋 Listar Equipes
```
GET /times
```

## ✏️ Atualizar Pontuação
```
PUT /times/{team_id}/pontuacao
Body: { "pontos": 75 }
```

## 🔐 Login
```
POST /login
Body:
{
  "usuario": "admin",
  "senha": "123"
}
```

---

# 🔧 Configuração do Banco (.env)
```
DB_HOST=localhost
DB_PORT=3306
DB_USER=root
DB_PASSWORD=senha
DB_NAME=spf
CORS_ORIGINS=http://localhost:5173,http://localhost:3000
```

---

# ▶️ Como Rodar Localmente

## 1. Instalar dependências
```
pip install fastapi uvicorn mysql-connector-python python-dotenv
```

## 2. Iniciar servidor
```
uvicorn main:app --reload
```

---

# 🐳 Rodando com Docker

### Build:
```
docker build -t spf-api .
```

### Run:
```
docker run -p 8000:8000 --env-file .env spf-api
```

---

# 📄 Resumo dos Endpoints
| Método | Rota | Descrição |
|--------|--------|------------|
| GET | / | Teste de conexão |
| GET | /times | Lista equipes |
| PUT | /times/{id}/pontuacao | Atualiza pontos |
| POST | /login | Realiza login |

---

# 🧑‍💻 Autor
Desenvolvido para a **Semana Paulo Freire – ETEC Maria Cristina Medeiros**.

