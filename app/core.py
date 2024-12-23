import pymysql
from db.connection import get_connection
from db.queries import (
    DELETE_TODO,
    INSERT_TODO,
    SELECT_HISTORY_TODO_LIST,
    SELECT_TODO_LIST,
    UPDATE_STATUS,
    UPDATE_TODO,
)
from flask import jsonify
from konlpy.tag import Kkma, Okt
from utils.date import str_date

# 현재 날짜 가져오기
current_date = str_date("%Y%m%d")
yesterday_date = str_date("%Y%m%d", 1)

okt = Okt()
kkma = Kkma()


def load_todos() -> list:
    """
    할 일 목록 불러오기

    :return: list
    """
    list = []
    with get_connection() as conn:
        with conn.cursor(
            pymysql.cursors.DictCursor
        ) as cursor:  # 결과를 딕셔너리 형태로 가져온다
            cursor.execute(SELECT_TODO_LIST, (current_date))
            list = cursor.fetchall()
        return list


def load_history_todos(render=True, date=yesterday_date):
    """
    해당날짜 완료된 목록 불러오기

    :param render: 렌더링 여부 (default: true)
    :param date: 선택 날짜 (default: 어제 날짜)
    """
    list = []
    with get_connection() as conn:
        with conn.cursor(
            pymysql.cursors.DictCursor
        ) as cursor:  # 결과를 딕셔너리 형태로 가져온다
            cursor.execute(SELECT_HISTORY_TODO_LIST, (date))
            list = cursor.fetchall()
        if render:
            return {"list": list, "date": date.strftime("%Y-%m-%d")}
        else:
            return jsonify({"state": "SUCCESS", "message": "success", "list": list})


def save_todo(todo):
    """
    할 일 목록 저장하기

    :param todo: 저장할 할일
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            # 새로 추가일때
            if todo.get("id") is None:
                cursor.execute(
                    INSERT_TODO, (todo.get("text"), current_date, current_date)
                )
            # 기존 데이터 수정일때
            elif todo.get("text") is None:
                cursor.execute(UPDATE_STATUS, (current_date, todo.get("id")))
            else:
                cursor.execute(
                    UPDATE_TODO, (todo.get("text"), current_date, todo.get("id"))
                )
        conn.commit()
    return jsonify({"state": "SUCCESS", "message": "success", "todo": todo})


def del_todo(todo):
    """
    할 일 목록 삭제하기

    :param todo: 삭제할 할일
    """
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute(DELETE_TODO, todo.get("id"))
        conn.commit()
    return jsonify({"state": "SUCCESS", "message": "success", "todo": todo})


# 품사 태깅
def tokenize(list):
    return jsonify(
        {
            "state": "SUCCESS",
            "message": "success",
            "nouns": [okt.nouns(text) for text in list],
        }
    )
