### 插件管理

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