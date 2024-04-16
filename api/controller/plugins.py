from flask import Blueprint, request, jsonify
from docker_manager.plugins import DockerPlugins

docker_plugins = DockerPlugins()
plugins = Blueprint('plugins', __name__)


@plugins.route('/install', methods=['POST'])
def install_plugin():
    data = request.json
    result = docker_plugins.install(**data)
    if 'error' in result:
        return jsonify(result), 500
    return jsonify(result), 201


@plugins.route('/configure/<plugin_name>', methods=['POST'])
def configure_plugin(plugin_name):
    data = request.json
    result = docker_plugins.configure(plugin_name, **data)
    if 'error' in result:
        return jsonify(result), 500
    return jsonify(result), 200


@plugins.route('/remove/<plugin_name>', methods=['DELETE'])
def remove_plugin(plugin_name):
    result = docker_plugins.remove(plugin_name)
    if 'error' in result:
        return jsonify(result), 500
    return jsonify(result), 204


@plugins.route('/list', methods=['GET'])
def list_plugins():
    result = docker_plugins.list()
    if 'error' in result:
        return jsonify(result), 500
    return jsonify(result), 200


@plugins.route('/details/<plugin_name>', methods=['GET'])
def plugin_details(plugin_name):
    result = docker_plugins.details(plugin_name)
    if 'error' in result:
        return jsonify(result), 500
    return jsonify(result), 200


@plugins.route('/test', methods=['GET'])
def test():
    return jsonify({'error': "654654"}), 200
