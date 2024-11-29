import os
from datetime import datetime

# 현재 날짜와 시간 가져오기
current_date = datetime.now()

# 날짜를 원하는 형식으로 포맷팅
formatted_date = current_date.strftime("%Y%m%d")

# 파일 이름 생성
TODO_FILE = f"todos_{formatted_date}.txt"

# 파일이 없으면 생성
if not os.path.exists(TODO_FILE):
    with open(TODO_FILE, "w", encoding="utf-8") as file:
        file.close()

# 할 일 목록 불러오기
def load_todos():
    try:
        with open(TODO_FILE, "r", encoding="utf-8") as file:
            list = []
            for line in file.readlines():
                status = 'completed' if '%완료%' in line.strip() else ''
                text = line.strip().replace('%완료%', '') if '%완료%' in line.strip() else line.strip()
                list.append({"text": text, "status": status})
            return list
    except FileNotFoundError:
        return []

# 할 일 목록 저장하기
def save_todo(todo):
    with open(TODO_FILE, "a", encoding="utf-8") as file:
        file.write(todo + "\n")
        file.close()
