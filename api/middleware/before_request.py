from ..auth import authenticate
from flask import request, jsonify


def before_request(no_auth=None):
    if no_auth is None:
        no_auth = []
    if request.path not in no_auth:
        auth_response = authenticate()
        print(auth_response)
        if auth_response:
            return auth_response
