import os
from datetime import datetime, timedelta

# 현재 날짜 가져오기
today = datetime.now()
# 어제 날짜 가져오기
yesterday = today - timedelta(days=1)

# 날짜를 원하는 형식으로 포맷팅
current_date = today.strftime("%Y%m%d")
yesterday_date = yesterday.strftime("%Y%m%d")

# 파일 이름 생성
TODO_FILE = f"todos_{current_date}.txt"
TODO_FILE_Y = f"todos_{yesterday_date}.txt"

# 할 일 목록 불러오기
def load_todos():
    list = []
    # 파일이 없으면 생성
    if not os.path.exists(TODO_FILE):
        with open(TODO_FILE, "w", encoding="utf-8") as newFile:
            # 이전날짜 파일이 있는지 확인
            if os.path.exists(TODO_FILE_Y):
                with open(TODO_FILE_Y, "r", encoding="utf-8") as oldFile:
                    for line in oldFile.readlines():
                        if not '%완료%' in line.strip():
                            newFile.write(line.strip() + "\n")
                            list.append({"text": line.strip(), "status": ''})
                oldFile.close()
        newFile.close()
    else:
        with open(TODO_FILE, "r", encoding="utf-8") as file:
            for line in file.readlines():
                status = 'completed' if '%완료%' in line.strip() else ''
                text = line.strip().replace('%완료%', '') if '%완료%' in line.strip() else line.strip()
                list.append({"text": text, "status": status})
    return list

# 할 일 목록 저장하기
def save_todo(todo):
    with open(TODO_FILE, "a", encoding="utf-8") as file:
        file.write(todo + "\n")
        file.close()
