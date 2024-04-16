from flask import Blueprint, request, jsonify
from docker_manager.services import DockerServices

docker_services = DockerServices()
services = Blueprint('services', __name__)


@services.route('/create', methods=['POST'])
def create_service():
    data = request.json
    result = docker_services.create_service(service_data=data)
    if 'id' in result:
        return jsonify(result), 201
    else:
        return jsonify(result), 500


@services.route('/list', methods=['GET'])
def list_services():
    services_info = docker_services.list_services()
    return jsonify(services_info), 200


@services.route('/<service_id>', methods=['GET'])
def get_service(service_id):
    service_info = docker_services.get_service(service_id=service_id)
    if 'id' in service_info:
        return jsonify(service_info), 200
    else:
        return jsonify(service_info), 404


@services.route('/update/<service_id>', methods=['POST'])
def update_service(service_id):
    data = request.json
    result = docker_services.update_service(service_id=service_id, service_data=data)
    if 'message' in result:
        return jsonify(result), 200
    else:
        return jsonify(result), 500


@services.route('/remove/<service_id>', methods=['DELETE'])
def remove_service(service_id):
    result = docker_services.remove_service(service_id=service_id)
    if 'message' in result:
        return jsonify(result), 204  # No Content
    else:
        return jsonify(result), 404


@services.route('/test', methods=['GET'])
def test():
    return jsonify({'error': "654654"}), 200
