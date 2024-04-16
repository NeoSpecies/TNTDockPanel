from flask import Blueprint, request, jsonify
from docker_manager.volumes import DockerVolume

docker_volume = DockerVolume()
volumes = Blueprint('volumes', __name__)


@volumes.route('/', methods=['GET'])
def list_volumes():
    volumes_info = docker_volume.list()
    if 'error' not in volumes_info:
        return jsonify(volumes_info), 200
    else:
        return jsonify(volumes_info), 500


@volumes.route('/<volume_name>', methods=['GET'])
def get_volume(volume_name):
    volume_info = docker_volume.get(volume_name)
    if 'error' not in volume_info:
        return jsonify(volume_info), 200
    else:
        return jsonify(volume_info), 500


@volumes.route('/remove/<volume_name>', methods=['DELETE'])
def remove_volume(volume_name):
    force_remove = request.args.get('force', 'false').lower() == 'true'
    result = docker_volume.remove(volume_name, force=force_remove)
    if 'error' not in result:
        return jsonify(result), 200
    else:
        return jsonify(result), 500


@volumes.route('/prune', methods=['POST'])
def prune_volumes():
    result = docker_volume.prune()
    if 'error' not in result:
        return jsonify(result), 200
    else:
        return jsonify(result), 500


@volumes.route('/create', methods=['POST'])
def create_volume():
    volume_data = request.json
    result = docker_volume.create(volume_data)
    if 'error' not in result:
        return jsonify(result), 201  # 201 Created 状态码
    else:
        return jsonify(result), 500  # 500 Internal Server Error 状态码


@volumes.route('/test', methods=['GET'])
def test():
    return jsonify({'error': "654654"}), 200
