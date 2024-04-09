### 容器管理
`DockerContainers` 类提供了与Docker容器相关的一系列操作，例如运行、创建、启动、获取信息、列表、统计、文件操作、重命名、暂停/取消暂停、调整大小、停止、重启、删除、检查、日志、提交以及在容器内执行命令。

#### 使用方式

首先，请确保您有 Docker 守护程序正在运行，并且您有与 Docker 交互的必要权限。
实例化类：

```python
from docker_containers import DockerContainers

docker_containers = DockerContainers()
```

#### 运行容器

```python
######### 示例入参
params = {
    'image': 'nginx:latest',
    'detach': True
}

##### 示例出参
docker.models.containers.Container
```

#### 创建容器

```python
######### 示例入参
params = {
    'image': 'nginx:latest',
    'name': 'my_nginx'
}

##### 示例出参
docker.models.containers.Container
```

#### 启动容器

```python
##### 示例入参
container_id = 'container_id_here'

##### 示例出参
{'message': 'Container started'}
```

#### 获取特定容器信息

```python
##### 示例入参
container_id = 'container_id_here'

##### 示例出参
docker.models.containers.Container
```

#### 获取容器列表

```python
##### 示例入参
params = {'all': True}

##### 示例出参
[{'container_id': 'container_id_here', 'status': 'exited'}]
```

#### 获取容器实时统计信息

```python
##### 示例入参
container_id = 'container_id_here'

##### 示例出参
Real-time statistics as a dictionary.
```

#### 列出容器内的进程

```python
##### 示例入参
container_id = 'container_id_here'

##### 示例出参
{'Processes': [['PID', 'USER', ...]], 'Titles': ['UID', 'PID', ...]}
```

#### 从容器内检索文件/文件夹存档

```python
##### 示例入参
container_id = 'container_id_here'
path = '/path/in/container'

##### 示例出参
The content of the file/folder as a stream.
```

#### 上传文件存档到容器的文件系统

```python
##### 示例入参
container_id = 'container_id_here'
path = '/path/in/container'
data = b'some_binary_data'

##### 示例出参
{'success': True}
```

#### 重命名容器

```python
##### 示例入参
container_id = 'container_id_here'
name = 'new_container_name'

##### 示例出参
{'message': 'Container renamed'}
```

#### 暂停容器

```python
##### 示例入参
container_id = 'container_id_here'

##### 示例出参
{'message': 'Container paused'}
```

#### 取消暂停容器

```python
##### 示例入参
container_id = 'container_id_here'

##### 示例出参
{'message': 'Container unpaused'}
```

#### 停止容器

```python
##### 示例入参
container_id = 'container_id_here'

##### 示例出参
{'message': 'Container stopped successfully'}
```

#### 重启容器

```python
##### 示例入参
container_id = 'container_id_here'

##### 示例出参
{'message': 'Container restarted successfully'}
```

#### 删除容器

```python
##### 示例入参
container_id = 'container_id_here'

##### 示例出参
{'message': 'Container removed successfully'}
```

#### 检查容器

```python
##### 示例入参
container_id = 'container_id_here'

##### 示例出参
Low-level information about the container as a dictionary.
```

#### 获取容器日志

```python
##### 示例入参
container_id = 'container_id_here'

##### 示例出参
Container logs as a string or bytes.
```

#### 从容器的更改创建新镜像

```python
##### 示例入参
container_id = 'container_id_here'

##### 示例出参
docker.models.images.Image
```

#### 在容器内执行命令

```python
##### 示例入参
container_id = 'container_id_here'
cmd = 'echo "Hello World"'

##### 示例出参
{'exit_code': 0, 'output': 'Hello World\n'}
```
#### 错误处理

当与Docker容器交互时，可能会遇到各种错误。为了优雅地处理这些情况，`DockerContainers`类应该能够捕捉这些错误并提供有关它们的信息。错误处理机制确保您能够理解在操作Docker容器时可能发生的问题，并采取相应的措施。

如果在操作过程中出现错误，例如尝试启动一个不存在的容器，或者尝试从不存在的镜像创建容器，响应将包括错误代码和错误消息。这使得调试和修复问题变得更加直接。

在进行错误处理时，您可以期待类似下面的错误响应：

```python
# 尝试执行可能导致错误的操作
try:
    container = docker_containers.start(container_id='nonexisting_container_id')
except docker.errors.ContainerError as e:
    # 捕捉特定的Docker容器错误
    error_response = {
        "error": {
            "code": e.status_code,
            "message": e.explanation
        }
    }
except docker.errors.ImageNotFound as e:
    # 捕捉拉取镜像时找不到镜像的错误
    error_response = {
        "error": {
            "code": e.status_code,
            "message": "Image not found: {}".format(e.explanation)
        }
    }
except docker.errors.APIError as e:
    # 捕捉Docker API的其他错误
    error_response = {
        "error": {
            "code": e.status_code,
            "message": "Docker API error: {}".format(e.explanation)
        }
    }
except Exception as e:
    # 捕捉其他所有异常
    error_response = {
        "error": {
            "code": "unknown",
            "message": "An unknown error occurred: {}".format(str(e))
        }
    }
```

##### 示例错误响应：

```json
{
  "error": {
    "code": 404,
    "message": "无法找到指定容器：nonexisting_container_id"
  }
}
```