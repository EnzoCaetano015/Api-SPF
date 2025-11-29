import mysql.connector
from mysql.connector import Error
from dotenv import load_dotenv
import os

load_dotenv()

def bdConect():
    try:
        conexao = mysql.connector.connect(
            host=os.getenv("DB_HOST", "banco"),
            port=os.getenv("DB_PORT", "3306"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", ""),
            database=os.getenv("DB_NAME", "spf")
        )
        return conexao
    except Error as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return None
