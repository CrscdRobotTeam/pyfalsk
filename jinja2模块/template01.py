from flask import Flask, render_template  # 模板文件

# app = Flask(__name__)
# 默认路径 当前文件路径的templates
app = Flask(__name__, template_folder="E:/pyflask/templates")


@app.route('/')
def index():
    class Person(object):
        name = 'Alex'
        age = 16

    p = Person()

    context = {
        'username': '知了',
        'gender': '男',
        'age': 19,
        'Person': p,
        'websites': {
            'baidu': 'www.baidu.com',
            'google': 'www.google.com'
        }
    }
    return render_template('index.html', **context)
    # return render_template('index.html', username='课堂999',gender='男',age=19)  # 模板传参 后台传参


if __name__ == '__main__':
    app.run()
'''
Flask 渲染Jinja2模板和传参：
1.渲染模板
 * 模板放在“templates”文件夹下
 * 从“flask”中导入“render_template”函数
 * 在视图中，使用“render_template”函数，渲染模板
  注意：只需要填写模板的名字，不需要写“templates”这个文件夹的路径
  （如果你在templates加入一个文件夹，写成：文件夹名/文件名）
2.模板传参
 *如果有少量参数，直接在“render_template”函数中添加关键字传参就可以了
 *如果有多个参数，可以将参数放在字典中，然后在“render_template”中，
    使用 **字典 （把字典转换成关键字参数传进去）传参
3.在模板中，如果使用一个变量，语法是“{{params}}”
4.访问模型中的属性或者是字典，可用“{{}parames.property}”的形式，或者使用“{{parames['property']}}”
'''
