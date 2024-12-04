from flask import Flask, render_template, redirect, url_for, request, jsonify
from app.core import load_todos, save_todo

app = Flask(__name__)

# 리스트 읽기        
@app.route("/", methods=["GET"])
def index():
    todos = load_todos()  # 저장된 할 일 불러오기
    print(todos)
    return render_template("index.html", todos=todos)

# 리스트 수정
@app.route("/updated", methods=["POST"])
def update():
    data = request.get_json()
    if data:
        return save_todo(data)

if __name__ == "__main__":
    app.template_folder = 'templates'
    app.static_folder = 'static'
    app.run(debug=True)
