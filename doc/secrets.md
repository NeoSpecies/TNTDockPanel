### 秘密管理

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