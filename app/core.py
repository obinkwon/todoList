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
from transformers import GPT2LMHeadModel, PreTrainedTokenizerFast
from utils.date import format_date, str_date

# 현재 날짜 가져오기
current_date = str_date("%Y%m%d")
yesterday_date = str_date("%Y%m%d", 1)

okt = Okt()
kkma = Kkma()

model = GPT2LMHeadModel.from_pretrained("skt/kogpt2-base-v2")
tokenizer = PreTrainedTokenizerFast.from_pretrained(
    "skt/kogpt2-base-v2",
    bos_token="</s>",
    eos_token="</s>",
    unk_token="<unk>",
    pad_token="<pad>",
    mask_token="<mask>",
)


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
            return {"list": list, "date": format_date("%Y-%m-%d", date)}
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
def sentence_todo(list):
    text = ",".join(list)
    input_ids = tokenizer.encode(text, return_tensors="pt")
    gen_ids = model.generate(
        input_ids,
        max_length=len(text) + 10,
        repetition_penalty=2.0,
        pad_token_id=tokenizer.pad_token_id,
        eos_token_id=tokenizer.eos_token_id,
        bos_token_id=tokenizer.bos_token_id,
        use_cache=True,
    )
    generated = tokenizer.decode(gen_ids[0])

    return jsonify(
        {
            "state": "SUCCESS",
            "message": "success",
            "result": generated,
        }
    )
