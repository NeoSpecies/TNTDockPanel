from flask import Blueprint, request, jsonify
from docker_manager.networks import DockerNetworks

docker_networks = DockerNetworks()
networks = Blueprint('networks', __name__)


@networks.route('/create', methods=['POST'])
def network_create():
    data = request.json
    result = docker_networks.create(**data)
    if 'error' not in result:
        return jsonify(result), 201
    else:
        return jsonify(result), 400


@networks.route('/list', methods=['GET'])
def network_list():
    result = docker_networks.list()
    return jsonify(result), 200 if not any('error' in res for res in result) else 400


@networks.route('/get/<network_id>', methods=['GET'])
def network_get(network_id):
    result = docker_networks.get(network_id)
    if 'error' not in result:
        return jsonify(result), 200
    else:
        return jsonify(result), 400


@networks.route('/remove/<network_id>', methods=['DELETE'])
def network_remove(network_id):
    result = docker_networks.remove(network_id)
    if 'error' not in result:
        return jsonify(result), 200
    else:
        return jsonify(result), 400


@networks.route('/prune', methods=['POST'])
def network_prune():
    result = docker_networks.prune()
    if 'error' not in result:
        return jsonify(result), 200
    else:
        return jsonify(result), 400


@networks.route('/test', methods=['GET'])
def test():
    return jsonify({'error': "654654"}), 200
