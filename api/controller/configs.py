from flask import Blueprint, request, jsonify
from docker_manager.configs import DockerConfigs

docker_configs = DockerConfigs()
configs = Blueprint('configs', __name__)


@configs.route('/create', methods=['POST'])
def create_config():
    data = request.json
    result = docker_configs.create_config(**data)
    if 'id' in result:
        return jsonify(result), 201
    else:
        return jsonify(result), 500


@configs.route('/list', methods=['GET'])
def list_configs():
    result = docker_configs.list_configs()
    if 'configs' in result:
        return jsonify(result), 200
    else:
        return jsonify(result), 500


@configs.route('/details/<config_id>', methods=['GET'])
def get_config_details(config_id):
    result = docker_configs.get_config_details(config_id)
    if 'id' in result:
        return jsonify(result), 200
    else:
        return jsonify(result), 404 if 'code' in result.get('error', {}) and result['error']['code'] == 404 else 500


@configs.route('/remove/<config_id>', methods=['DELETE'])
def remove_config(config_id):
    result = docker_configs.remove_config(config_id)
    if 'message' in result:
        return jsonify(result), 204
    else:
        return jsonify(result), 404 if 'code' in result.get('error', {}) and result['error']['code'] == 404 else 500


@configs.route('/test', methods=['GET'])
def test():
    return jsonify({'error': "654654"}), 200
