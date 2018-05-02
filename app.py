from flask import Flask
from routes.index import main as index_routes
app = Flask(__name__)
# 设置 secret_key 来使用 flask 自带的 session
app.secret_key = 'test for good'
app.register_blueprint(index_routes)
if __name__ == '__main__':
    # debug 模式可以自动加载你对代码的变动, 所以不用重启程序
    # host 参数指定为 '0.0.0.0' 可以让别的机器访问你的代码
    config = dict(
        debug=True,
        host='0.0.0.0',
        port=4567,
    )
    app.run(**config)