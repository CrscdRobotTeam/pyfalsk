from flask import Flask, render_template,redirect,url_for

# app = Flask(__name__)
# 默认路径 当前文件路径的templates
app = Flask(__name__, template_folder="E:/pyflask/templates")


@app.route('/')
def index():
    url_content = url_for('content')
    return redirect(url_content)
    return render_template('index_filter.html',avatar='https://avatar.csdn.net/9/0/4/3_ly123963.jpg')
'''例如：过滤器的作用就是，如果有头像就显示头像，没有头像就显示默认的头像（无头像）
过滤器的作用对象是变量'''


@app.route('/content/')
def content():
    # 定义一个评论列表
    comments = [
        {
            'user': '站长',
            'content': u'xxxxxxxxxxxx'
        },
        {
            'user': '你猜',
            'content': u'yxyxyxyxyxy'
        },
        {
            'user': '船长杰克',
            'content': u'tttttttmtmtmtmtd'
        }
    ]
    return render_template('index_filter.html',comments=comments)

if __name__ == '__main__':
    app.run()
