from flask import Flask

app = Flask(__name__, template_folder="E:/pyflask/templates")


@app.route('/')
def index():
    return 'index'


if __name__ == '__main__':
    app.run()
