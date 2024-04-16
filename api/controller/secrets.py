from flask import Blueprint, request, jsonify
from docker_manager.secrets import DockerSecrets

docker_secrets = DockerSecrets()
secrets = Blueprint('secrets', __name__)


@secrets.route('/create', methods=['POST'])
def create_secret():
    data = request.json
    result = docker_secrets.create_secret(**data)
    if 'id' in result:
        return jsonify(result), 201
    else:
        return jsonify(result), 500


@secrets.route('/list', methods=['GET'])
def list_secrets():
    result = docker_secrets.list_secrets()
    if any('error' in secret for secret in result):
        return jsonify(result), 500
    else:
        return jsonify(result), 200


@secrets.route('/<string:secret_id>', methods=['GET'])
def get_secret_details(secret_id):
    result = docker_secrets.get_secret_details(secret_id)
    if 'id' in result:
        return jsonify(result), 200
    else:
        return jsonify(result), 404


@secrets.route('/remove/<string:secret_id>', methods=['DELETE'])
def remove_secret(secret_id):
    result = docker_secrets.remove_secret(secret_id)
    if 'message' in result:
        return jsonify(result), 204
    else:
        return jsonify(result), 500


@secrets.route('/test', methods=['GET'])
def test():
    return jsonify({'error': "654654"}), 200
