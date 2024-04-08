from flask import Flask, send_file, request, jsonify
from io import BytesIO
from docker_manager.containers import DockerContainers
from docker_manager.images import DockerImages
from docker_manager.networks import DockerNetworks
from docker_manager.volumes import DockerVolume
from docker_manager.services import DockerServices
from docker_manager.nodes import DockerNodes
from docker_manager.secrets import DockerSecrets
from docker_manager.configs import DockerConfigs
from docker_manager.plugins import DockerPlugins

app = Flask(__name__)

docker_containers = DockerContainers()
docker_images = DockerImages()
docker_networks = DockerNetworks()
docker_volume = DockerVolume()
docker_services = DockerServices()
docker_nodes = DockerNodes()
docker_secrets = DockerSecrets()
docker_configs = DockerConfigs()
docker_plugins = DockerPlugins()


@app.route('/containers/run', methods=['POST'])
def container_run():
    data = request.json
    message = docker_containers.run(**data)
    if message:
        return jsonify({'container_id': message.id}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/create', methods=['POST'])
def container_create():
    data = request.json
    message = docker_containers.create(**data)
    if message:
        return jsonify({'container_id': message.id}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/start/<container_id>', methods=['POST'])
def container_start(container_id):
    data = request.json
    message = docker_containers.start(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/getInfo/<container_id>', methods=['GET'])
def container_get_info(container_id):
    message = docker_containers.get_info(container_id)
    container_info = {
        'container_id': message.id,
        'name': message.name,
        'status': message.status,
        'image': message.image.tags,
        'labels': message.labels,
        'short_id': message.short_id,
        'raw': message.attrs
    }
    if message:
        return jsonify({'data': container_info}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/getList/', methods=['POST'])
def container_get_list():
    data = request.json
    message = docker_containers.get_list(**data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/getStats/<container_id>', methods=['POST'])
def container_get_stats(container_id):
    data = request.json
    message = docker_containers.get_stats(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/top/<container_id>', methods=['POST'])
def container_top(container_id):
    data = request.json
    message = docker_containers.top(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/getArchive/<container_id>', methods=['GET'])
def container_get_archive(container_id):
    path_to_file = request.args.get('path')  # 从查询参数中获取path
    chunk_size = request.args.get('chunk_size')  # 从查询参数中获取path
    encode_stream = request.args.get('encode_stream')  # 从查询参数中获取path
    print(path_to_file, chunk_size, encode_stream)
    # return "234234"
    if not path_to_file:
        return "Path is required", 400  # 如果没有提供path，返回400错误
    bits, stat = docker_containers.get_archive(container_id, path_to_file, chunk_size, encode_stream)

    file_like_object = BytesIO()
    for chunk in bits:
        file_like_object.write(chunk)
    file_like_object.seek(0)  # 跳转到文件的开头
    # 使用 Flask 的 send_file 方法发送文件
    return send_file(
        file_like_object,
        mimetype='application/octet-stream',
        as_attachment=True,
        download_name='test.tar'  # 设置下载时的文件名
    )


@app.route('/containers/put_archive/<string:container_id>', methods=['POST'])
def upload_file_to_container(container_id):
    # 检查文件是否存在于请求中
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400
    file = request.files['file']
    path = request.form.get('path', '/home/')  # 获取用户想要上传到的容器内的路径，默认为根目录

    # 使用 BytesIO 创建一个类文件对象，用于存放归档内容
    file_object = BytesIO()
    file.save(file_object)  # 将上传的文件保存到 file_object 中
    file_object.seek(0)  # 移动到文件的开头，确保从头开始读取
    message = docker_containers.put_archive(container_id, path, file_object)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/rename/<container_id>', methods=['POST'])
def container_rename(container_id):
    data = request.json
    message = docker_containers.rename(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/pause/<container_id>', methods=['GET'])
def container_pause(container_id):
    message = docker_containers.pause(container_id)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/unpause/<container_id>', methods=['GET'])
def container_unpause(container_id):
    message = docker_containers.unpause(container_id)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/resize/<container_id>', methods=['POST'])
def container_resize(container_id):
    data = request.json
    message = docker_containers.resize(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/stop/<container_id>', methods=['POST'])
def container_stop(container_id):
    data = request.json
    message = docker_containers.stop(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/restart/<container_id>', methods=['POST'])
def container_restart(container_id):
    data = request.json
    message = docker_containers.restart(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/kill/<container_id>', methods=['POST'])
def container_kill(container_id):
    data = request.json
    message = docker_containers.kill(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/remove/<container_id>', methods=['POST'])
def container_remove(container_id):
    data = request.json
    message = docker_containers.remove(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/logs/<container_id>', methods=['POST'])
def container_logs(container_id):
    data = request.json
    message = docker_containers.logs(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/diff/<container_id>', methods=['GET'])
def container_diff(container_id):
    message = docker_containers.diff(container_id)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/execRun/<container_id>', methods=['POST'])
def container_exec_run(container_id):
    data = request.json
    message = docker_containers.exec_run(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/wait/<container_id>', methods=['POST'])
def container_wait(container_id):
    data = request.json
    message = docker_containers.wait(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/attach/<container_id>', methods=['POST'])
def container_attach(container_id):
    data = request.json
    message = docker_containers.attach(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/attachSocket/<container_id>', methods=['POST'])
def container_attach_socket(container_id):
    data = request.json
    message = docker_containers.attach_socket(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/prune/', methods=['POST'])
def container_prune():
    data = request.json
    message = docker_containers.prune(**data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/update/<container_id>', methods=['POST'])
def container_update(container_id):
    data = request.json
    message = docker_containers.update(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/containers/commit/<container_id>', methods=['POST'])
def container_commit(container_id):
    data = request.json
    message = docker_containers.commit(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


# 这里开始都是image的接口部分
@app.route('/images/build', methods=['POST'])
def image_build():
    data = request.json
    message = docker_images.build(**data)
    if 'error' not in message:
        return jsonify(message), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/images/pull', methods=['POST'])
def image_pull():
    repository = request.json.get('repository')
    tag = request.json.get('tag', None)
    message = docker_images.pull(repository, tag)
    if 'error' not in message:
        return jsonify(message), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/images/push', methods=['POST'])
def image_push():
    repository = request.json.get('repository')
    tag = request.json.get('tag', None)
    message = docker_images.push(repository, tag)
    if 'error' not in message:
        return jsonify(message), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/images/list', methods=['GET'])
def image_list():
    message = docker_images.list(**request.args)
    if len(message) == 0 or 'error' not in message[0]:
        return jsonify({'images': message}), 200
    else:
        return jsonify({'error': message[0]}), 400


@app.route('/images/get/<image_id>', methods=['GET'])
def image_get(image_id):
    message = docker_images.get(image_id)
    if 'error' not in message:
        return jsonify(message), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/images/remove/<image_id>', methods=['DELETE'])
def image_remove(image_id):
    message = docker_images.remove(image_id)
    if 'error' not in message:
        return jsonify(message), 200
    else:
        return jsonify({'error': message}), 400


@app.route('/images/prune', methods=['DELETE'])
def image_prune():
    message = docker_images.prune()
    if 'error' not in message:
        return jsonify(message), 200
    else:
        return jsonify({'error': message}), 400


# 以下是网络管理
@app.route('/networks/create', methods=['POST'])
def network_create():
    data = request.json
    result = docker_networks.create(**data)
    if 'error' not in result:
        return jsonify(result), 201
    else:
        return jsonify(result), 400


@app.route('/networks/list', methods=['GET'])
def network_list():
    result = docker_networks.list()
    return jsonify(result), 200 if not any('error' in res for res in result) else 400


@app.route('/networks/get/<network_id>', methods=['GET'])
def network_get(network_id):
    result = docker_networks.get(network_id)
    if 'error' not in result:
        return jsonify(result), 200
    else:
        return jsonify(result), 400


@app.route('/networks/remove/<network_id>', methods=['DELETE'])
def network_remove(network_id):
    result = docker_networks.remove(network_id)
    if 'error' not in result:
        return jsonify(result), 200
    else:
        return jsonify(result), 400


@app.route('/networks/prune', methods=['POST'])
def network_prune():
    result = docker_networks.prune()
    if 'error' not in result:
        return jsonify(result), 200
    else:
        return jsonify(result), 400


# 以下是卷操作
@app.route('/volumes', methods=['GET'])
def list_volumes():
    volumes_info = docker_volume.list()
    if 'error' not in volumes_info:
        return jsonify(volumes_info), 200
    else:
        return jsonify(volumes_info), 500


@app.route('/volumes/<volume_name>', methods=['GET'])
def get_volume(volume_name):
    volume_info = docker_volume.get(volume_name)
    if 'error' not in volume_info:
        return jsonify(volume_info), 200
    else:
        return jsonify(volume_info), 500


@app.route('/volumes/remove/<volume_name>', methods=['DELETE'])
def remove_volume(volume_name):
    force_remove = request.args.get('force', 'false').lower() == 'true'
    result = docker_volume.remove(volume_name, force=force_remove)
    if 'error' not in result:
        return jsonify(result), 200
    else:
        return jsonify(result), 500


@app.route('/volumes/prune', methods=['POST'])
def prune_volumes():
    result = docker_volume.prune()
    if 'error' not in result:
        return jsonify(result), 200
    else:
        return jsonify(result), 500


@app.route('/volumes/create', methods=['POST'])
def create_volume():
    volume_data = request.json
    result = docker_volume.create(volume_data)
    if 'error' not in result:
        return jsonify(result), 201  # 201 Created 状态码
    else:
        return jsonify(result), 500  # 500 Internal Server Error 状态码


# 以下是服务
@app.route('/services/create', methods=['POST'])
def create_service():
    data = request.json
    result = docker_services.create_service(service_data=data)
    if 'id' in result:
        return jsonify(result), 201
    else:
        return jsonify(result), 500


@app.route('/services/list', methods=['GET'])
def list_services():
    services_info = docker_services.list_services()
    return jsonify(services_info), 200


@app.route('/services/<service_id>', methods=['GET'])
def get_service(service_id):
    service_info = docker_services.get_service(service_id=service_id)
    if 'id' in service_info:
        return jsonify(service_info), 200
    else:
        return jsonify(service_info), 404


@app.route('/services/update/<service_id>', methods=['POST'])
def update_service(service_id):
    data = request.json
    result = docker_services.update_service(service_id=service_id, service_data=data)
    if 'message' in result:
        return jsonify(result), 200
    else:
        return jsonify(result), 500


@app.route('/services/remove/<service_id>', methods=['DELETE'])
def remove_service(service_id):
    result = docker_services.remove_service(service_id=service_id)
    if 'message' in result:
        return jsonify(result), 204  # No Content
    else:
        return jsonify(result), 404


# 以下是docker node

@app.route('/nodes', methods=['GET'])
def list_nodes():
    response = docker_nodes.list_nodes()
    if 'error' not in response:
        return jsonify(response), 200
    else:
        return jsonify(response['error']), 500


@app.route('/nodes/<string:node_id>', methods=['GET'])
def get_node_details(node_id):
    response = docker_nodes.get_node_details(node_id)
    if 'error' not in response:
        return jsonify(response), 200
    else:
        return jsonify(response['error']), 404 if response['error']['message'].endswith('not found') else 500


@app.route('/nodes/update/<string:node_id>', methods=['POST'])
def update_node(node_id):
    data = request.json
    response = docker_nodes.update_node(node_id, **data)
    if 'error' not in response:
        return jsonify(response), 200
    else:
        return jsonify(response['error']), 404 if response['error']['message'].endswith('not found') else 500


@app.route('/nodes/remove/<string:node_id>', methods=['DELETE'])
def remove_node(node_id):
    response = docker_nodes.remove_node(node_id)
    if 'error' not in response:
        return jsonify(response), 204
    else:
        return jsonify(response['error']), 404 if response['error']['message'].endswith('not found') else 500


# 以下是secrets
@app.route('/secrets/create', methods=['POST'])
def create_secret():
    data = request.json
    result = docker_secrets.create_secret(**data)
    if 'id' in result:
        return jsonify(result), 201
    else:
        return jsonify(result), 500


@app.route('/secrets/list', methods=['GET'])
def list_secrets():
    result = docker_secrets.list_secrets()
    if any('error' in secret for secret in result):
        return jsonify(result), 500
    else:
        return jsonify(result), 200


@app.route('/secrets/<string:secret_id>', methods=['GET'])
def get_secret_details(secret_id):
    result = docker_secrets.get_secret_details(secret_id)
    if 'id' in result:
        return jsonify(result), 200
    else:
        return jsonify(result), 404


@app.route('/secrets/remove/<string:secret_id>', methods=['DELETE'])
def remove_secret(secret_id):
    result = docker_secrets.remove_secret(secret_id)
    if 'message' in result:
        return jsonify(result), 204
    else:
        return jsonify(result), 500


# 以下是Config
@app.route('/configs/create', methods=['POST'])
def create_config():
    data = request.json
    result = docker_configs.create_config(**data)
    if 'id' in result:
        return jsonify(result), 201
    else:
        return jsonify(result), 500


@app.route('/configs/list', methods=['GET'])
def list_configs():
    result = docker_configs.list_configs()
    if 'configs' in result:
        return jsonify(result), 200
    else:
        return jsonify(result), 500


@app.route('/configs/details/<config_id>', methods=['GET'])
def get_config_details(config_id):
    result = docker_configs.get_config_details(config_id)
    if 'id' in result:
        return jsonify(result), 200
    else:
        return jsonify(result), 404 if 'code' in result.get('error', {}) and result['error']['code'] == 404 else 500


@app.route('/configs/remove/<config_id>', methods=['DELETE'])
def remove_config(config_id):
    result = docker_configs.remove_config(config_id)
    if 'message' in result:
        return jsonify(result), 204
    else:
        return jsonify(result), 404 if 'code' in result.get('error', {}) and result['error']['code'] == 404 else 500

# 以下为插件
@app.route('/plugins/install', methods=['POST'])
def install_plugin():
    data = request.json
    result = docker_plugins.install(**data)
    if 'error' in result:
        return jsonify(result), 500
    return jsonify(result), 201

@app.route('/plugins/configure/<plugin_name>', methods=['POST'])
def configure_plugin(plugin_name):
    data = request.json
    result = docker_plugins.configure(plugin_name, **data)
    if 'error' in result:
        return jsonify(result), 500
    return jsonify(result), 200

@app.route('/plugins/remove/<plugin_name>', methods=['DELETE'])
def remove_plugin(plugin_name):
    result = docker_plugins.remove(plugin_name)
    if 'error' in result:
        return jsonify(result), 500
    return jsonify(result), 204

@app.route('/plugins/list', methods=['GET'])
def list_plugins():
    result = docker_plugins.list()
    if 'error' in result:
        return jsonify(result), 500
    return jsonify(result), 200

@app.route('/plugins/details/<plugin_name>', methods=['GET'])
def plugin_details(plugin_name):
    result = docker_plugins.details(plugin_name)
    if 'error' in result:
        return jsonify(result), 500
    return jsonify(result), 200
if __name__ == "__main__":
    app.run(debug=True)
