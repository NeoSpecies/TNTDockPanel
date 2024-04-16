from flask import Blueprint
import os
import importlib


def register_blueprints(app, package_name, package_path):
    """自动发现并注册蓝图"""
    for filename in os.listdir(package_path):
        if filename.endswith('.py') and not filename.startswith('__'):
            module_name = filename[:-3]
            module = importlib.import_module(f'{package_name}.{module_name}')
            url_prefix = f'/{module_name}'
            for item in dir(module):
                item = getattr(module, item)
                if isinstance(item, Blueprint):
                    app.register_blueprint(item, url_prefix=url_prefix)
