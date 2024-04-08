### 网络管理

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