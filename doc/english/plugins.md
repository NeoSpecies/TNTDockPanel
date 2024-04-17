### Plugin Management

The `DockerPlugins` class provides a series of methods for managing Docker plugins, including installation, configuration, removal, listing, and obtaining plugin details.

#### How To Use

First, make sure you have the Docker daemon running, and you have the necessary permissions to interact with Docker.

Instantiate the class:

```python
from your_module_name import DockerPlugins  # Replace your_module_name with the actual name of your module

docker_plugins = DockerPlugins()
```

#### Install Plugins

Install a Docker plugin:

##### Example Code:

```python
install_result = docker_plugins.install(name="vieux/sshfs", options={"alias": "sshfs"})
```

##### Example Response:

```json
{
  "message": "Plugin vieux/sshfs installed"
}
```

#### Configure Plugins

Configure an installed Docker plugin:

##### Example Code:

```python
configure_result = docker_plugins.configure(plugin_name="sshfs", options={"DEBUG": "1"})
```

##### Example Response:

```json
{
  "message": "Plugin sshfs configured"
}
```

#### Remove Plugins

Remove a Docker plugin:

##### Example Code:

```python
remove_result = docker_plugins.remove(plugin_name="sshfs")
```

##### Example Response:

```json
{
  "message": "Plugin sshfs removed"
}
```

#### List Plugins

List all installed Docker plugins:

##### Example Code:

```python
list_result = docker_plugins.list()
```

##### Example Response:

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

#### Get Plugin Details

Get details of a specific Docker plugin:

##### Example Code:

```python
details_result = docker_plugins.details(plugin_name="sshfs")
```

##### Example Response:

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

#### Error Handling

If an error occurs, the response will include an error code and message, indicating what went wrong. For example, if you try to install a plugin that does not exist:

##### Example Code:

```python
error_response = docker_plugins.install(name="nonexisting/plugin")
```

##### Example Error Response:

```json
{
  "error": {
    "code": 404,
    "message": "Error: The requested plugin nonexisting/plugin does not exist on Docker Hub"
  }
}
```