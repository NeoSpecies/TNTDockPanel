from flask import request


def after_request(response):
    # 可以在这里修改response对象
    # 比如：添加HTTP头，日志记录等
    print("After request...")
    return response
