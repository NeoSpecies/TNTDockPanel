### 卷管理
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