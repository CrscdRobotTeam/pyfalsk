from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    login_url = url_for('login')
    # return redirect('/login/')  # 输入地址
    return redirect(login_url)  # 用反转获取url，只要函数名不变就行
    return '这是首页'


@app.route('/login/')
def login():
    return '这是登录页'


@app.route('/question/<is_login>/')
def question(is_login):
    if is_login == '1':
        return '这是问答页面'
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run()
