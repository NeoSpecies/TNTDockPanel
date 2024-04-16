from flask import jsonify


def errorhandler(e):
    # 这里可以定义一个JSON格式的错误响应
    # e是捕获的HTTP异常对象
    response = jsonify({
        'success': False,
        'error': e.description,
        'code': e.code
    })
    return response, e.code
