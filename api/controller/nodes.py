from flask import Blueprint, request, jsonify
from docker_manager.nodes import DockerNodes

docker_nodes = DockerNodes()
nodes = Blueprint('nodes', __name__)


@nodes.route('/', methods=['GET'])
def list_nodes():
    response = docker_nodes.list_nodes()
    if 'error' not in response:
        return jsonify(response), 200
    else:
        return jsonify(response['error']), 500


@nodes.route('/<string:node_id>', methods=['GET'])
def get_node_details(node_id):
    response = docker_nodes.get_node_details(node_id)
    if 'error' not in response:
        return jsonify(response), 200
    else:
        return jsonify(response['error']), 404 if response['error']['message'].endswith('not found') else 500


@nodes.route('/update/<string:node_id>', methods=['POST'])
def update_node(node_id):
    data = request.json
    response = docker_nodes.update_node(node_id, **data)
    if 'error' not in response:
        return jsonify(response), 200
    else:
        return jsonify(response['error']), 404 if response['error']['message'].endswith('not found') else 500


@nodes.route('/remove/<string:node_id>', methods=['DELETE'])
def remove_node(node_id):
    response = docker_nodes.remove_node(node_id)
    if 'error' not in response:
        return jsonify(response), 204
    else:
        return jsonify(response['error']), 404 if response['error']['message'].endswith('not found') else 500


@nodes.route('/test', methods=['GET'])
def test():
    return jsonify({'error': "654654"}), 200
