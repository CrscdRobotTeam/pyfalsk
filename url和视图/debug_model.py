from flask import Flask

# '''开启debug模式 方法二：'''
# import config # 2
app = Flask(__name__)


# app.config.from_object(config) # 2

@app.route('/')
def hello_world():
    '''
    a = 1
    b = 0
    c = a / b  # 直接运行，出错 Internal server Error
    '''
    '''开启debug模式 方法一：'''
    # Pycharm 2018环境中可以直接右键运行按钮左边下拉菜单的Edit Configurations，
    # 勾上Flask_Debug后面的小勾就好了
    return '我是第一个程序ss'


@app.route('/article/<id>')  # 传参
# (http://127.0.0.1:5000/article/1112)1112输入网址时候写入
def article(id):
    return '您请求的参数是：%s' % id  # 获取1112 显示到页面


if __name__ == '__main__':
    # debug = True
    # 1.debug模式，当程序出错，可把错误抛出到页面
    # 2.debug模式，只修改项目中的'python'文件，程序会自动加载，不需要手动重启服务器
    app.run()
