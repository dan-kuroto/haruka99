from flask import Flask, send_file


app = Flask(__name__, template_folder='./')


@app.route("/haruka99")
def index():
    # return render_template('index.html')
    # html里用了vue的 {{}} 之后似乎跟flask的模板语法冲突了，不能用render_template
    with open('index.html', 'r', encoding='utf-8') as file:
        return file.read()


@app.route("/haruka99/res/<name>")
def res(name: str):
    return send_file(f'res/{name}')
