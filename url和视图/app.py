# python2默认编码ASCII，不支持中文，
# 需要在首行添加 （# encoding: utf-8）设置其编码格式，支持中文

# 从flask框架中导入Flask这个类
from flask import Flask

# 初始化一个Flask对象
# Flask()
# 需要传递一个参数 __name__
# 1.方便flask框架寻找资源
# 2.方便flask插件如 Flask-Sqlalchemy出现错误得时候，去定位错误
# 不写__name__可能出错不能抛出
app = Flask(__name__)


# @app.route是一个装饰器
# @开头，并且在函数上面，说明是装饰器
# 这个装饰器得作用，是做一个url与视图函数的映射
# 127.0.0.1:500/ -> 去请求hello_world()这个函数，然后将结果返回给浏览器
@app.route('/')  # '/',分号里代表url
def hello_world():  # 视图函数
    return 'Hello World! 我是第一个程序'


# 当前文件作为入口程序运行，执行app.run()
if __name__ == '__main__':
    # app.run()
    # 启动一个应用服务器，来接收用户的请求
    # while True：
    #   listen()
    app.run()
