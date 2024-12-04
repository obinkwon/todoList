import os
import json
from datetime import datetime, timedelta
from flask import jsonify

# 현재 날짜 가져오기
today = datetime.now()

# 날짜를 원하는 형식으로 포맷팅
current_date = today.strftime("%Y%m%d")

# 파일 이름 생성
TODO_FILE = f"todoList.json"

# 할 일 목록 불러오기
def load_todos():
    list = []
    try:
        # 파일이 없으면 생성
        if not os.path.exists(TODO_FILE):
            with open(TODO_FILE, "w", encoding="utf-8") as newFile:
                json.dump([], newFile)
        # 파일이 있으면 불러오기
        else:
            with open(TODO_FILE, "r", encoding="utf-8") as file:
                list = json.load(file)
        return list
    except:
        with open(TODO_FILE, "w", encoding="utf-8") as newFile:
            json.dump([], newFile)
        return []

# 할 일 목록 저장하기
def save_todo(todo):
    # data 현재날짜로 기본세팅
    data = {"id":'', "text":todo['text'], "date":current_date, "status":"N"}

    with open(TODO_FILE, encoding="utf-8") as file:
        list = json.load(file)
        idList = [i['id'] for i in list] # id 만 담은 list
        last_id = idList[-1] if len(idList) > 0 else 0 # list에서 마지막 index 값 가져오기

        # 새로 추가일때
        if todo.get('id') is None: 
            data['id'] = last_id + 1 # id 값 새로 부여
            list.append(data)
        # 기존 데이터 수정일때
        else:
            for item in list:
                if int(item.get("id")) == int(todo.get("id")):
                    item["text"] = data.get("text")
                    item["status"] = "C" if item.get("status") == "N" else "N"
        # 파일 업데이트
        with open(TODO_FILE, "w", encoding="utf-8") as newFile:
            json.dump(list, newFile, indent=4, ensure_ascii=False) # 들여쓰기 4, 한글깨짐 False
    return jsonify({'state': 'SUCCESS', 'message': 'success', 'todo': todo})
