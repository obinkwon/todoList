from app.core import del_todo, load_todos, save_todo, tokenize
from flask import Flask, flash, redirect, render_template, request, url_for

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
    if data:
        return save_todo(data)


# 리스트 제거
@app.route("/deleted", methods=["POST"])
def delete():
    data = request.get_json()
    if data:
        return del_todo(data)


# 문장 만들기
@app.route("/sentence", methods=["POST"])
def sentence():
    todos = load_todos()  # 저장된 할 일 불러오기
    return tokenize([todo.get("TEXT") for todo in todos])


if __name__ == "__main__":
    app.template_folder = "templates"
    app.static_folder = "static"
    app.run(debug=True)
