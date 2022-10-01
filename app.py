from flask import Flask, render_template, send_file


app = Flask(__name__, template_folder='./')


@app.route("/haruka99")
def index():
    return render_template('index.html')


@app.route("/haruka99/res/<name>")
def res(name: str):
    return send_file(f'res/{name}')
