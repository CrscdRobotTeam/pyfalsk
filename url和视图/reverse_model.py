# 反转url：
# 从视图到url的转换叫做反转url
# 用处：页面重定向（页面跳转），在模板中用
from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def index():
    print(url_for('my_list'))
    print(url_for('article', id='abc'))
    return 'Hello'


@app.route('/list/')
def my_list():
    return 'list'


@app.route('/article/<id>/')
def article(id):
    return '您请求的id是: %s' % id


if __name__ == '__main__':
    app.run()
