from flask import request, jsonify,make_response


def check_api_key(api_key):
    # 这里填入你的API密钥检查逻辑
    return api_key == 'YourActualAPIKey'


def authenticate():
    api_key = request.headers.get('Authorization')
    if not check_api_key(api_key):
        response = jsonify({'error': 'authentication failed'})
        return make_response(response, 401)
