from flask import Flask, render_template, redirect, url_for
from app.core import load_todos, save_todo

app = Flask(__name__)
        
@app.route("/", methods=["GET"])
def index():
    todos = load_todos()  # 저장된 할 일 불러오기
    return render_template("index.html", todos=todos)

@app.route("/saved/<text>", methods=["POST"])
def save(text):
    new_todo = text
    if new_todo:
        save_todo(new_todo)  # 새 할 일을 파일에 저장
    return redirect(url_for("index"))

if __name__ == "__main__":
    app.template_folder = 'templates'
    app.static_folder = 'static'
    app.run(debug=True)
