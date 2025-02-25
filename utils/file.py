import json
import os

from flask import jsonify
from utils.date import str_date
from utils.sentence import create_sentence

# 현재 날짜 가져오기
current_date = str_date("%Y%m%d")


def export_todo(result):
    """
    완료된 목록 내보내기

    :param list: 완료된 목록
    :param date: 선택 날짜 (default : 오늘)
    """
    list = result.get("list")
    date = result.get("date", current_date)
    sentence = create_sentence([item["TEXT"] for item in list])

    if len(list) > 0:
        # 파일 이름 생성
        TODO_FILE = f"{date}-todoList.txt"
        # 파일이 없으면 생성
        with open(TODO_FILE, "w", encoding="utf-8") as newFile:
            for todo in list:
                newFile.write(todo.get("TEXT") + "\n")
            newFile.write("요약 : " + sentence + "\n")

        return jsonify({"state": "SUCCESS", "message": "내보내기 성공"})
    else:
        return jsonify({"state": "SUCCESS", "message": "완료된 일이 없습니다."})
