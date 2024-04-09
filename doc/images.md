### 镜像管理
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