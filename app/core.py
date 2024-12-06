import pymysql
from utils.date import str_date
from flask import jsonify
from db.connection import get_connection
from db.queries import SELECT_TODO_LIST, INSERT_TODO, UPDATE_TODO


# 현재 날짜 가져오기
current_date = str_date("%Y%m%d")

# 파일 이름 생성
TODO_FILE = f"todoList.json"

# 할 일 목록 불러오기
def load_todos():
    list = []
    with get_connection() as conn:
        with conn.cursor(pymysql.cursors.DictCursor) as cursor: # 결과를 딕셔너리 형태로 가져온다
            cursor.execute(SELECT_TODO_LIST,(current_date))
            list = cursor.fetchall()
        return list

# 할 일 목록 저장하기
def save_todo(todo):
    print(todo)
    # 새로 추가일때
    with get_connection() as conn:
        with conn.cursor() as cursor:
            if todo.get('id') is None:
                cursor.execute(INSERT_TODO,(todo.get("text"),current_date))
            # 기존 데이터 수정일때
            else:
                cursor.execute(UPDATE_TODO,(todo.get("id")))
        conn.commit()
    return jsonify({'state': 'SUCCESS', 'message': 'success', 'todo': todo})
