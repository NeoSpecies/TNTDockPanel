from flask import Blueprint, send_file, request, jsonify
from docker_manager.containers import DockerContainers
from io import BytesIO

docker_containers = DockerContainers()
containers = Blueprint('containers', __name__)


@containers.route('/run', methods=['POST'])
def container_run():
    data = request.json
    message = docker_containers.run(**data)
    if message:
        return jsonify({'container_id': message.id}), 200
    else:
        return jsonify({'error': message}), 400


@containers.route('/create', methods=['POST'])
def container_create():
    data = request.json
    message = docker_containers.create(**data)
    if message:
        return jsonify({'container_id': message.id}), 200
    else:
        return jsonify({'error': message}), 400


@containers.route('/start/<container_id>', methods=['POST'])
def container_start(container_id):
    data = request.json
    message = docker_containers.start(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@containers.route('/getInfo/<container_id>', methods=['GET'])
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


@containers.route('/getList/', methods=['POST'])
def container_get_list():
    data = request.json
    message = docker_containers.get_list(**data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@containers.route('/getStats/<container_id>', methods=['POST'])
def container_get_stats(container_id):
    data = request.json
    message = docker_containers.get_stats(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@containers.route('/top/<container_id>', methods=['POST'])
def container_top(container_id):
    data = request.json
    message = docker_containers.top(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@containers.route('/getArchive/<container_id>', methods=['GET'])
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


@containers.route('/put_archive/<string:container_id>', methods=['POST'])
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


@containers.route('/rename/<container_id>', methods=['POST'])
def container_rename(container_id):
    data = request.json
    message = docker_containers.rename(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@containers.route('/pause/<container_id>', methods=['GET'])
def container_pause(container_id):
    message = docker_containers.pause(container_id)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@containers.route('/unpause/<container_id>', methods=['GET'])
def container_unpause(container_id):
    message = docker_containers.unpause(container_id)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@containers.route('/resize/<container_id>', methods=['POST'])
def container_resize(container_id):
    data = request.json
    message = docker_containers.resize(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@containers.route('/stop/<container_id>', methods=['POST'])
def container_stop(container_id):
    data = request.json
    message = docker_containers.stop(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@containers.route('/restart/<container_id>', methods=['POST'])
def container_restart(container_id):
    data = request.json
    message = docker_containers.restart(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@containers.route('/kill/<container_id>', methods=['POST'])
def container_kill(container_id):
    data = request.json
    message = docker_containers.kill(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@containers.route('/remove/<container_id>', methods=['POST'])
def container_remove(container_id):
    data = request.json
    message = docker_containers.remove(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@containers.route('/logs/<container_id>', methods=['POST'])
def container_logs(container_id):
    data = request.json
    message = docker_containers.logs(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@containers.route('/diff/<container_id>', methods=['GET'])
def container_diff(container_id):
    message = docker_containers.diff(container_id)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@containers.route('/execRun/<container_id>', methods=['POST'])
def container_exec_run(container_id):
    data = request.json
    message = docker_containers.exec_run(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@containers.route('/wait/<container_id>', methods=['POST'])
def container_wait(container_id):
    data = request.json
    message = docker_containers.wait(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@containers.route('/attach/<container_id>', methods=['POST'])
def container_attach(container_id):
    data = request.json
    message = docker_containers.attach(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@containers.route('/attachSocket/<container_id>', methods=['POST'])
def container_attach_socket(container_id):
    data = request.json
    message = docker_containers.attach_socket(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@containers.route('/prune/', methods=['POST'])
def container_prune():
    data = request.json
    message = docker_containers.prune(**data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@containers.route('/update/<container_id>', methods=['POST'])
def container_update(container_id):
    data = request.json
    message = docker_containers.update(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400


@containers.route('/commit/<container_id>', methods=['POST'])
def container_commit(container_id):
    data = request.json
    message = docker_containers.commit(container_id, **data)
    if message:
        return jsonify({'data': message}), 200
    else:
        return jsonify({'error': message}), 400



