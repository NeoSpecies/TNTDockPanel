from flask import Blueprint, request, jsonify
from docker_manager.images import DockerImages

docker_images = DockerImages()
images = Blueprint('images', __name__)


@images.route('/build', methods=['POST'])
def image_build():
    data = request.json
    message = docker_images.build(**data)
    if 'error' not in message:
        return jsonify(message), 200
    else:
        return jsonify({'error': message}), 400


@images.route('/pull', methods=['POST'])
def image_pull():
    repository = request.json.get('repository')
    tag = request.json.get('tag', None)
    message = docker_images.pull(repository, tag)
    if 'error' not in message:
        return jsonify(message), 200
    else:
        return jsonify({'error': message}), 400


@images.route('/push', methods=['POST'])
def image_push():
    repository = request.json.get('repository')
    tag = request.json.get('tag', None)
    message = docker_images.push(repository, tag)
    if 'error' not in message:
        return jsonify(message), 200
    else:
        return jsonify({'error': message}), 400


@images.route('/list', methods=['GET'])
def image_list():
    message = docker_images.list(**request.args)
    if len(message) == 0 or 'error' not in message[0]:
        return jsonify({'images': message}), 200
    else:
        return jsonify({'error': message[0]}), 400


@images.route('/get/<image_id>', methods=['GET'])
def image_get(image_id):
    message = docker_images.get(image_id)
    if 'error' not in message:
        return jsonify(message), 200
    else:
        return jsonify({'error': message}), 400


@images.route('/remove/<image_id>', methods=['DELETE'])
def image_remove(image_id):
    message = docker_images.remove(image_id)
    if 'error' not in message:
        return jsonify(message), 200
    else:
        return jsonify({'error': message}), 400


@images.route('/prune', methods=['DELETE'])
def image_prune():
    message = docker_images.prune()
    if 'error' not in message:
        return jsonify(message), 200
    else:
        return jsonify({'error': message}), 400


@images.route('/test', methods=['GET'])
def test():
    return jsonify({'error': "654654"}), 200
