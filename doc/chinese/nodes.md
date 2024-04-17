### Docker 节点管理

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