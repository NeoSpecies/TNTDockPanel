

<div align="center">

# TNTDockPanel 🚀

**一个为现代开发者设计的Docker管理面板**

![Docker](https://img.shields.io/badge/Docker-Container-blue.svg)
![Build Status](https://img.shields.io/badge/build-passing-brightgreen.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

</div>



## 📜 简介

TNTDockPanel是一个直观且高效的Docker管理工具，它提供了易于使用的图形界面，让Docker容器的创建、监控和管理变得轻而易举。我们的目标是让Docker容器的管理工作变得简单有趣，就像点燃TNT一样令人兴奋与高效。


## ✨ 特性

- **用户友好的界面**：一个清晰直观的用户界面，帮助您轻松管理Docker容器。
- **快速部署**：一键即可部署应用，无需复杂配置。
- **实时监控**：实时更新的容器状态显示，一目了然。
- **跨环境管理**：支持多环境容器管理，轻松应对各种部署场景。
- **安全优先**：我们重视您的数据安全，采用行业标准的安全措施。

---

## ⚙️ 安装

```bash
# 克隆仓库
git clone https://github.com/yourusername/TNTDockPanel.git

# 进入项目目录
cd TNTDockPanel

# 使用Docker Compose启动服务
docker-compose up -d
```

---

## 📖 使用指南

这个项目提供了一个简单的API，允许用户通过发送JSON数据来运行和创建Docker容器。

### 安装

首先，确保您的系统上已安装Docker。然后，安装此项目所需的Python库：

```bash
pip install docker
```
#### 镜像管理


`DockerImages` 类提供了一系列方法来管理 Docker 镜像，包括构建、拉取、推送、列出、获取、删除和清理镜像。

#### 使用方式

首先，请确保您有 Docker 守护程序正在运行，并且您有与 Docker 交互的必要权限。

实例化类：

```python
from your_module_name import DockerImages  # 将 your_module_name 替换为您模块的实际名称

docker_images = DockerImages()
```

#### 构建镜像

从 Dockerfile 构建镜像：

```python
build_result = docker_images.build(path=".", tag="my-image:latest")
```

##### 示例响应：

```json
{
  "id": "sha256:1a2b3c4d5e6f...",
  "tag": ["my-image:latest"]
}
```

#### 拉取镜像

从仓库拉取镜像：

```python
pull_result = docker_images.pull(repository="ubuntu", tag="latest")
```

##### 示例响应：

```json
{
  "id": "sha256:1a2b3c4d5e...",
  "tag": ["ubuntu:latest"]
}
```

#### 推送镜像

将镜像推送至仓库：

```python
push_result = docker_images.push(repository="myusername/my-image", tag="latest")
```

##### 示例响应：

```json
{
  "response": "The push refers to repository [docker.io/myusername/my-image]"
}
```

#### 列出镜像

列出所有镜像：

```python
list_result = docker_images.list()
```

##### 示例响应：

```json
[
  {
    "id": "sha256:1a2b3c4d5e...",
    "tags": ["ubuntu:latest"]
  },
  {
    "id": "sha256:7h8i9j0k1l...",
    "tags": ["my-image:latest"]
  }
]
```

#### 获取镜像

通过 ID 获取特定镜像：

```python
get_result = docker_images.get(image_id="sha256:1a2b3c4d5e6f")
```

##### 示例响应：

```json
{
  "id": "sha256:1a2b3c4d5e6f...",
  "tags": ["ubuntu:latest"]
}
```

#### 删除镜像

通过 ID 删除镜像：

```python
remove_result = docker_images.remove(image_id="sha256:1a2b3c4d5e6f")
```

##### 示例响应：

```json
{
  "result": "success"
}
```

#### 清理未使用的镜像

清理未使用的镜像：

```python
prune_result = docker_images.prune()
```

##### 示例响应：

```json
{
  "images_deleted": [
    {"Deleted": "sha256:1a2b3c4d5e6f..."},
    {"Deleted": "sha256:7h8i9j0k1l..."}
  ],
  "space_reclaimed": 1234567
}
```

#### 错误处理

如果出现错误，响应将包括错误代码和消息，指示出了什么问题。例如，如果您尝试拉取一个不存在的镜像：

```python
error_response = docker_images.pull(repository="nonexisting", tag="latest")
```

##### 示例错误响应：

```json
{
  "error": {
    "code": 404,
    "message": "对 nonexisting 的拉取访问被拒绝，仓库不存在或可能需要 'docker login'：拒绝：请求访问资源被拒绝"
  }
}
```
#### 容器管理
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

#### 网络管理

`DockerNetworks` 类提供了一系列方法来管理 Docker 网络，包括创建、列出、获取、删除和清理网络。

#### 使用方式

首先，请确保您有 Docker 守护程序正在运行，并且您有与 Docker 交互的必要权限。

实例化类：

```python
from your_module_name import DockerNetworks  # 将 your_module_name 替换为您模块的实际名称

docker_networks = DockerNetworks()
```

##### 创建网络

创建一个新的网络：

```python
create_result = docker_networks.create(name="my_network", driver="bridge")
```

###### 示例响应：

```json
{
  "id": "4e2a4b9c4e5b6f...",
  "name": "my_network"
}
```

##### 列出网络

列出所有网络：

```python
list_result = docker_networks.list()
```

###### 示例响应：

```json
[
  {
    "id": "4e2a4b9c4e5b6f...",
    "name": "my_network"
  },
  {
    "id": "7f8g9h0i1j2k3l...",
    "name": "another_network"
  }
]
```

##### 获取网络

通过 ID 获取特定网络：

```python
get_result = docker_networks.get(network_id="4e2a4b9c4e5b6f...")
```

###### 示例响应：

```json
{
  "id": "4e2a4b9c4e5b6f...",
  "name": "my_network"
}
```

##### 删除网络

通过 ID 删除网络：

```python
remove_result = docker_networks.remove(network_id="4e2a4b9c4e5b6f...")
```

###### 示例响应：

```json
{
  "result": "success",
  "message": "Network 4e2a4b9c4e5b6f... removed"
}
```

##### 清理未使用的网络

清理未使用的网络：

```python
prune_result = docker_networks.prune()
```

###### 示例响应：

```json
{
  "networks_deleted": ["4e2a4b9c4e5b6f...", "7f8g9h0i1j2k3l..."],
  "space_reclaimed": 32000
}
```

#### 错误处理

如果出现错误，响应将包括错误代码和消息，指示出了什么问题。例如，如果您尝试删除一个不存在的网络：

```python
error_response = docker_networks.remove(network_id="nonexisting")
```

##### 示例错误响应：

```json
{
  "error": {
    "code": 404,
    "message": "Network not found"
  }
}
```
#### DockerVolume 类使用示例

`DockerVolume` 类提供了一系列方法来管理 Docker 卷，包括列出、获取、删除、清理和创建卷。

#### 使用方式

首先，请确保您有 Docker 守护程序正在运行，并且您有与 Docker 交互的必要权限。

实例化类：

```python
from your_module_name import DockerVolume  # 将 your_module_name 替换为您模块的实际名称

docker_volume = DockerVolume()
```

##### 列出卷

列出所有卷以及它们的信息：

```python
list_result = docker_volume.list()
```

###### 示例响应：

```json
[
  {
    "name": "my-volume",
    "driver": "local",
    "mountpoint": "/var/lib/docker/volumes/my-volume/_data"
  },
  ...
]
```

##### 获取卷

通过名称获取特定卷的信息：

```python
get_result = docker_volume.get(volume_name="my-volume")
```

###### 示例响应：

```json
{
  "name": "my-volume",
  "driver": "local",
  "mountpoint": "/var/lib/docker/volumes/my-volume/_data"
}
```

##### 删除卷

通过名称删除特定卷：

```python
remove_result = docker_volume.remove(volume_name="my-volume", force=True)
```

###### 示例响应：

```json
{
  "message": "Volume removed"
}
```

##### 清理未使用的卷

清理未使用的卷并返回回收的空间量：

```python
prune_result = docker_volume.prune()
```

###### 示例响应：

```json
{
  "VolumesDeleted": ["my-unused-volume"],
  "SpaceReclaimed": 1024
}
```

##### 创建卷

创建一个新的卷并返回其信息：

```python
create_result = docker_volume.create(volume_data={"name": "new-volume", "driver": "local"})
```

###### 示例响应：

```json
{
  "name": "new-volume"
}
```

### 错误处理

如果出现错误，响应将包括错误代码和消息，指示出了什么问题。例如，如果您尝试删除一个不存在的卷：

```python
error_response = docker_volume.remove(volume_name="nonexisting-volume")
```

##### 示例错误响应：

```json
{
  "error": {
    "code": 404,
    "message": "卷 nonexisting-volume 不存在"
  }
}
```
#### Docker 节点管理

`DockerNodes` 类提供了一系列方法来管理 Docker Swarm 集群中的节点，包括列出节点、获取节点详细信息、更新节点和删除节点。

#### 使用方式

首先，请确保您有 Docker 守护程序正在运行，并且您有与 Docker 交互的必要权限，并且 Swarm 模式已经被激活。

实例化类：

```python
from your_module_name import DockerNodes  # 将 your_module_name 替换为您模块的实际名称

docker_nodes = DockerNodes()
```

##### 列出节点

列出 Swarm 集群中的所有节点以及它们的信息：

```python
list_nodes_result = docker_nodes.list_nodes()
```

###### 示例响应：

```json
{
  "nodes": [
    {
      "id": "24ifsmvkjbyhk",
      "hostname": "node-1",
      "status": "ready",
      "role": "manager"
    },
    {
      "id": "57fyk3xpe5k8",
      "hostname": "node-2",
      "status": "ready",
      "role": "worker"
    }
  ]
}
```

##### 获取节点详细信息

获取特定节点的详细信息：

```python
get_node_details_result = docker_nodes.get_node_details(node_id="24ifsmvkjbyhk")
```

###### 示例响应：

```json
{
  "id": "24ifsmvkjbyhk",
  "hostname": "node-1",
  "status": {
    "State": "ready",
    "Addr": "192.168.1.100"
  },
  "role": "manager"
}
```

##### 更新节点

更新特定节点的属性：

```python
update_node_result = docker_nodes.update_node(node_id="24ifsmvkjbyhk", role="worker", availability="active")
```

###### 示例响应：

```json
{
  "message": "Node updated"
}
```

##### 删除节点

从 Swarm 集群中删除特定节点：

```python
remove_node_result = docker_nodes.remove_node(node_id="57fyk3xpe5k8")
```

###### 示例响应：

```json
{
  "message": "Node removed"
}
```

#### 错误处理

如果在操作过程中发生错误，响应将包括错误代码和消息，指示出了什么问题。

例如，如果您尝试获取一个不存在的节点的详细信息：

```python
error_response = docker_nodes.get_node_details(node_id="nonexisting-node-id")
```

##### 示例错误响应：

```json
{
  "error": {
    "message": "Node nonexisting-node-id not found"
  }
}
``` 

如果您尝试更新一个不存在的节点：

```python
error_response = docker_nodes.update_node(node_id="nonexisting-node-id", role="worker")
```

###### 示例错误响应：

```json
{
  "error": {
    "message": "Node nonexisting-node-id not found"
  }
}
``` 

如果尝试删除一个不存在的节点：

```python
error_response = docker_nodes.remove_node(node_id="nonexisting-node-id")
```

###### 示例错误响应：

```json
{
  "error": {
    "message": "Node nonexisting-node-id not found"
  }
}
``` 
#### 插件管理

`DockerPlugins` 类提供了一系列方法来管理 Docker 插件，包括安装、配置、删除、列出和获取插件详情。

#### 使用方式

首先，请确保您有 Docker 守护程序正在运行，并且您有与 Docker 交互的必要权限。

实例化类：

```python
from your_module_name import DockerPlugins  # 将 your_module_name 替换为您模块的实际名称

docker_plugins = DockerPlugins()
```

#### 安装插件

安装 Docker 插件：

##### 示例代码：

```python
install_result = docker_plugins.install(name="vieux/sshfs", options={"alias": "sshfs"})
```

##### 示例响应：

```json
{
  "message": "Plugin vieux/sshfs installed"
}
```

#### 配置插件

配置已安装的 Docker 插件：

##### 示例代码：

```python
configure_result = docker_plugins.configure(plugin_name="sshfs", options={"DEBUG": "1"})
```

##### 示例响应：

```json
{
  "message": "Plugin sshfs configured"
}
```

#### 删除插件

删除 Docker 插件：

##### 示例代码：

```python
remove_result = docker_plugins.remove(plugin_name="sshfs")
```

##### 示例响应：

```json
{
  "message": "Plugin sshfs removed"
}
```

#### 列出插件

列出所有已安装的 Docker 插件：

##### 示例代码：

```python
list_result = docker_plugins.list()
```

##### 示例响应：

```json
{
  "plugins": [
    {
      "name": "vieux/sshfs",
      "id": "12345abcdef",
      "enabled": true
    }
  ]
}
```

#### 获取插件详情

获取特定 Docker 插件的详情：

##### 示例代码：

```python
details_result = docker_plugins.details(plugin_name="sshfs")
```

##### 示例响应：

```json
{
  "name": "vieux/sshfs",
  "id": "12345abcdef",
  "enabled": true,
  "settings": {
    "Env": ["DEBUG=0"],
    "Args": [],
    "Devices": [],
    "Mounts": []
  }
}
```

#### 错误处理

如果出现错误，响应将包括错误代码和消息，指示出了什么问题。例如，如果您尝试安装一个不存在的插件：

##### 示例代码：

```python
error_response = docker_plugins.install(name="nonexisting/plugin")
```

##### 示例错误响应：

```json
{
  "error": {
    "code": 404,
    "message": "错误：请求的插件 nonexisting/plugin 在 Docker Hub 中不存在"
  }
}
```
#### Docker服务管理

`DockerServices` 类提供了一系列方法来管理 Docker 服务，包括创建、列出、获取、更新和删除 Docker 服务。

#### 使用方式

首先，请确保您有 Docker 守护程序正在运行，并且您有与 Docker 交互的必要权限。

实例化类：

```python
from your_module_name import DockerServices  # 将 your_module_name 替换为您模块的实际名称

docker_services = DockerServices()
```

#### 创建服务

创建新的 Docker 服务：

```python
service_data = {
    "name": "my_service",
    "task_template": {
        "container_spec": {
            "image": "nginx:latest"
        }
    }
}
create_result = docker_services.create_service(service_data=service_data)
```

##### 示例响应：

```json
{
  "id": "jtnbj4al07nrxkuer2y39vu3h"
}
```

#### 列出服务

列出所有 Docker 服务及其详细信息：

```python
list_result = docker_services.list_services()
```

##### 示例响应：

```json
[
  {
    "id": "jtnbj4al07nrxkuer2y39vu3h",
    "name": "my_service",
    "attrs": {...}  // 服务属性的详细信息
  }
]
```

#### 获取服务

通过 ID 获取特定 Docker 服务的详细信息：

```python
get_result = docker_services.get_service(service_id="jtnbj4al07nrxkuer2y39vu3h")
```

##### 示例响应：

```json
{
  "id": "jtnbj4al07nrxkuer2y39vu3h",
  "name": "my_service",
  "attrs": {...}  // 服务属性的详细信息
}
```

#### 更新服务

更新现有 Docker 服务：

```python
service_data_update = {
    "name": "my_updated_service",
    "task_template": {
        "container_spec": {
            "image": "nginx:latest"
        }
    }
}
update_result = docker_services.update_service(service_id="jtnbj4al07nrxkuer2y39vu3h", service_data=service_data_update)
```

##### 示例响应：

```json
{
  "message": "Service updated"
}
```

#### 删除服务

通过 ID 删除一个 Docker 服务：

```python
remove_result = docker_services.remove_service(service_id="jtnbj4al07nrxkuer2y39vu3h")
```

##### 示例响应：

```json
{
  "message": "Service removed"
}
```

### 错误处理

如果出现错误，响应将包括错误代码和消息，指示出了什么问题。例如，如果您尝试获取一个不存在的服务：

```python
error_response = docker_services.get_service(service_id="nonexistingserviceid")
```

##### 示例错误响应：

```json
{
  "error": {
    "message": "Service not found"
  }
}
```

如果出现其他错误，比如 API 错误或 Docker 异常，响应可能如下：

```json
{
  "error": {
    "code": 500,
    "message": "Internal server error"
  }
}
```
#### Docker配置管理

`DockerConfigs` 类提供了一系列方法来管理 Docker 配置，包括创建、列出、获取详情和删除配置。

#### 使用方式

首先，请确保您有 Docker 守护程序正在运行，并且您有与 Docker 交互的必要权限。

实例化类：

```python
from your_module_name import DockerConfigs  # 将 your_module_name 替换为您模块的实际名称

docker_configs = DockerConfigs()
```

#### 创建配置

创建一个新的配置项：

```python
create_result = docker_configs.create_config(name="myconfig", data="config_data_here")
```

##### 示例响应：

```json
{
  "id": "k3mno4567pqr89stuvwx"
}
```

#### 列出配置

列出所有配置项：

```python
list_result = docker_configs.list_configs()
```

##### 示例响应：

```json
{
  "configs": [
    {"id": "abcd1234efgh5678ijkl", "name": "myconfig"}
  ]
}
```

#### 获取配置详情

获取特定配置的详细信息：

```python
get_result = docker_configs.get_config_details(config_id="abcd1234efgh5678ijkl")
```

##### 示例响应：

```json
{
  "id": "abcd1234efgh5678ijkl",
  "name": "myconfig"
}
```

#### 删除配置

通过 ID 删除配置：

```python
remove_result = docker_configs.remove_config(config_id="abcd1234efgh5678ijkl")
```

##### 示例响应：

```json
{
  "message": "Config removed"
}
```

#### 错误处理

如果出现错误，响应将包括错误代码和消息，指示出了什么问题。例如，如果您尝试获取一个不存在的配置：

```python
error_response = docker_configs.get_config_details(config_id="nonexisting")
```

##### 示例错误响应：

```json
{
  "error": {
    "code": 404,
    "message": "Config not found"
  }
}
```
#### Docker秘密管理

`DockerSecrets` 类提供了一系列方法来管理 Docker 秘密，包括创建、列出、获取详细信息和删除秘密。

#### 使用方式

首先，请确保您有 Docker 守护程序正在运行，并且您有与 Docker 交互的必要权限。

实例化类：

```python
from your_module_name import DockerSecrets  # 将 your_module_name 替换为您模块的实际名称

docker_secrets = DockerSecrets()
```

##### 创建秘密

创建一个新的秘密：

```python
create_result = docker_secrets.create_secret(name="mysecret", data="secret_data_here")
```

###### 示例响应：

```json
{
  "id": "k3mno4567pqr89stuvwx"
}
```

##### 列出秘密

列出所有秘密：

```python
list_result = docker_secrets.list_secrets()
```

###### 示例响应：

```json
{
  "secrets": [
    {"id": "abcd1234efgh5678ijkl", "name": "mysecret"}
  ]
}
```

##### 获取秘密详情

获取特定秘密的详细信息：

```python
get_result = docker_secrets.get_secret_details(secret_id="abcd1234efgh5678ijkl")
```

###### 示例响应：

```json
{
  "id": "abcd1234efgh5678ijkl",
  "name": "mysecret"
}
```

##### 删除秘密

通过 ID 删除秘密：

```python
remove_result = docker_secrets.remove_secret(secret_id="abcd1234efgh5678ijkl")
```

###### 示例响应：

```json
{
  "message": "Secret removed"
}
```

#### 错误处理

如果出现错误，响应将包括错误代码和消息，指示出了什么问题。例如，如果您尝试获取一个不存在的秘密：

```python
error_response = docker_secrets.get_secret_details(secret_id="nonexisting")
```

###### 示例错误响应：

```json
{
  "error": {
    "code": 404,
    "message": "Secret not found"
  }
}
```

---

## 👍 贡献

如果您想为TNTDockPanel做出贡献，请阅读[`CONTRIBUTING.md`](CONTRIBUTING.md)了解详细信息。

---

## ©️ 许可证

该项目遵循MIT许可证。更多信息请查看[`LICENSE`](LICENSE)文件。

---
