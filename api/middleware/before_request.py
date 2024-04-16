from ..auth import authenticate
from flask import request, jsonify


def before_request(no_auth=None):
    if no_auth is None:
        no_auth = []
    print(f"Handling Request: {request.method} {request.path}")
    print(request.path)
    print(request.path not in no_auth)
    if request.path not in no_auth:
        auth_response = authenticate()
        if auth_response:
            return auth_response
