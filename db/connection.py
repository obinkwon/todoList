import os

import pymysql
from dotenv import load_dotenv

# .env 파일 로드
load_dotenv()


# MySQL 데이터베이스 연결
def get_connection():
    conn = pymysql.connect(
        host=os.getenv("DB_HOST", "localhost"),
        port=int(os.getenv("DB_PORT", 3306)),
        user=os.getenv("DB_USER", "root"),
        password=os.getenv("DB_PASSWORD", ""),
        db=os.getenv("DB_NAME", "mysql"),
        charset="utf8mb3",
    )
    return conn
