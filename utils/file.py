import json
import os

from flask import jsonify
from utils.date import str_date

# 현재 날짜 가져오기
current_date = str_date("%Y%m%d")


def export_todo(list, date=current_date):
    """
    완료된 목록 내보내기

    :param list: 완료된 목록
    :param date: 선택 날짜 (default : 오늘)
    """
    print(list)
    print(date)
    if len(list) > 0:
        # 파일 이름 생성
        TODO_FILE = f"{date}-todoList.txt"
        # 파일이 없으면 생성
        with open(TODO_FILE, "w", encoding="utf-8") as newFile:
            for todo in list:
                newFile.write(todo.get("TEXT") + "\n")

        return jsonify({"state": "SUCCESS", "message": "내보내기 성공"})
    else:
        return jsonify({"state": "SUCCESS", "message": "완료된 일이 없습니다."})
