import os
from flask import Flask
from config import Config
from .tools import register_blueprints


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)
    # 自动注册蓝图
    register_blueprints(app, 'api.controller', os.path.join(app.root_path, 'controller'))
    # 可以在这里初始化数据库

    return app
