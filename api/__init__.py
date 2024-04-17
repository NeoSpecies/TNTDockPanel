import os
from flask import Flask
from config import Config
from .tools import register_blueprints
from werkzeug.exceptions import HTTPException
from .middleware import before_request, after_request, teardown_request, teardown_appcontext, errorhandler


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # 注册请求相关的钩子
    @app.before_request
    def before_request_func():
        return before_request(app.config['NO_AUTH'])
    app.after_request(after_request)
    app.teardown_request(teardown_request)
    app.teardown_appcontext(teardown_appcontext)

    # app.errorhandler(errorhandler)
    @app.errorhandler(HTTPException)
    def handle_http_exception(e):
        return errorhandler(e)

    # 自动注册蓝图
    register_blueprints(app, 'api.controller', os.path.join(app.root_path, 'controller'))
    # 可以在这里初始化数据库

    return app
