from flask import Flask, render_template

# app = Flask(__name__)
# 默认路径 当前文件路径的templates
app = Flask(__name__, template_folder="E:/pyflask/templates")


@app.route('/<is_login>')
def index(is_login):
    if is_login == '1':
        user = {
            'username': 'lily',
            'age': 17
        }
        return render_template('index_if.html', user=user)
    else:
        return render_template('index_if.html')


if __name__ == '__main__':
    app.run()
