from app.core import del_todo, load_todos, save_todo, tagging
from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)


# 리스트 읽기
@app.route("/", methods=["GET"])
def index():
    todos = load_todos()  # 저장된 할 일 불러오기
    return render_template("index.html", todos=todos)


# 리스트 수정
@app.route("/updated", methods=["POST"])
def update():
    data = request.get_json()
    tagging()
    # 토크나이저 테스트를 위한 임시 주석처리
    # if data:
    #     return save_todo(data)


# 리스트 제거
@app.route("/deleted", methods=["POST"])
def delete():
    data = request.get_json()
    if data:
        return del_todo(data)


if __name__ == "__main__":
    app.template_folder = "templates"
    app.static_folder = "static"
    app.run(debug=True)
