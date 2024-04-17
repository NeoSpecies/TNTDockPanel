### Docker Node Management

The `DockerNodes` class provides a series of methods for managing nodes in a Docker Swarm cluster, including listing nodes, retrieving node details, updating nodes, and removing nodes.

#### How To Use

First, ensure that the Docker daemon is running and that you have the necessary permissions to interact with Docker, and that Swarm mode is activated.

Instantiate the class:

```python
from your_module_name import DockerNodes  # Replace your_module_name with the actual name of your module

docker_nodes = DockerNodes()
```

##### Listing Nodes

List all nodes in the Swarm cluster along with their information:

```python
list_nodes_result = docker_nodes.list_nodes()
```

###### Example Response:

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

##### Retrieving Node Details

Retrieve detailed information about a specific node:

```python
get_node_details_result = docker_nodes.get_node_details(node_id="24ifsmvkjbyhk")
```

###### Example Response:

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

##### Updating Nodes

Update the attributes of a specific node:

```python
update_node_result = docker_nodes.update_node(node_id="24ifsmvkjbyhk", role="worker", availability="active")
```

###### Example Response:

```json
{
  "message": "Node updated"
}
```

##### Removing Nodes

Remove a specific node from the Swarm cluster:

```python
remove_node_result = docker_nodes.remove_node(node_id="57fyk3xpe5k8")
```

###### Example Response:

```json
{
  "message": "Node removed"
}
```

#### Error Handling

If an error occurs during the operation, the response will include an error code and message, indicating what went wrong.

For example, if you try to retrieve details for a node that does not exist:

```python
error_response = docker_nodes.get_node_details(node_id="nonexisting-node-id")
```

##### Example Error Response:

```json
{
  "error": {
    "message": "Node nonexisting-node-id not found"
  }
}
``` 

If you try to update a node that does not exist:

```python
error_response = docker_nodes.update_node(node_id="nonexisting-node-id", role="worker")
```

###### Example Error Response:

```json
{
  "error": {
    "message": "Node nonexisting-node-id not found"
  }
}
``` 

If you attempt to remove a node that does not exist:

```python
error_response = docker_nodes.remove_node(node_id="nonexisting-node-id")
```

###### Example Error Response:

```json
{
  "error": {
    "message": "Node nonexisting-node-id not found"
  }
}
``` 