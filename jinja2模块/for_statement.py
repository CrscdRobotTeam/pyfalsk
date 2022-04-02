from flask import Flask, render_template

# app = Flask(__name__)
# 默认路径 当前文件路径的templates
app = Flask(__name__, template_folder="E:/pyflask/templates")


# for 遍历字典
# @app.route('/<is_login>')
# def index(is_login):
#     if is_login == '1':
#         user = {
#             'username': 'lily',
#             'age': 17
#         }
#         websites=['baidu.com','google.com']
#         # for k,v in user.items():
#         #     print(k)
#         #     print(v)
#         return render_template('index_for.html',user=user,websites=websites)
#     else:
#         return render_template('index_for.html')


@app.route('/')
def index():
    books = [
        {
            'name': '西游记',
            'author': '吴承恩',
            'price': '100元'
        },
        {
            'name': '水浒传',
            'author': '施耐庵',
            'price': '120元'
        },
        {
            'name': '红楼梦',
            'author': '曹雪芹',
            'price': '150元'
        },
        {
            'name': '三国演义',
            'author': '罗贯中',
            'price': '200元'
        }
    ]
    return render_template('index_for.html', books=books)


if __name__ == '__main__':
    app.run()
