### Container Management
`DockerContainers` class provides a range of operations related to Docker containers, such as run, create, start, inspect, list, stats, file operations, rename, pause/unpause, resize, stop, restart, remove, check logs, commit, and execute commands within containers.

#### Usage

First, please make sure that the Docker daemon is running, and that you have the necessary permissions to interact with Docker.
Instantiate the class:

```python
from docker_containers import DockerContainers

docker_containers = DockerContainers()
```

#### Running a Container

```python
######### Example Parameters
params = {
    'image': 'nginx:latest',
    'detach': True
}

##### Example Response
docker.models.containers.Container
```

#### Creating a Container

```python
######### Example Parameters
params = {
    'image': 'nginx:latest',
    'name': 'my_nginx'
}

##### Example Response
docker.models.containers.Container
```

#### Starting a Container

```python
##### Example Parameters
container_id = 'container_id_here'

##### Example Response
{'message': 'Container started'}
```

#### Getting Specific Container Information

```python
##### Example Parameters
container_id = 'container_id_here'

##### Example Response
docker.models.containers.Container
```

#### Getting a List of Containers

```python
##### Example Parameters
params = {'all': True}

##### Example Response
[{'container_id': 'container_id_here', 'status': 'exited'}]
```

#### Getting Real-time Container Statistics

```python
##### Example Parameters
container_id = 'container_id_here'

##### Example Response
Real-time statistics as a dictionary.
```

#### Listing Processes Inside a Container

```python
##### Example Parameters
container_id = 'container_id_here'

##### Example Response
{'Processes': [['PID', 'USER', ...]], 'Titles': ['UID', 'PID', ...]}
```

#### Retrieving an Archive of Files/Folders from Inside a Container

```python
##### Example Parameters
container_id = 'container_id_here'
path = '/path/in/container'

##### Example Response
The content of the file/folder as a stream.
```

#### Uploading a File Archive to a Container's File System

```python
##### Example Parameters
container_id = 'container_id_here'
path = '/path/in/container'
data = b'some_binary_data'

##### Example Response
{'success': True}
```

#### Renaming a Container

```python
##### Example Parameters
container_id = 'container_id_here'
name = 'new_container_name'

##### Example Response
{'message': 'Container renamed'}
```

#### Pausing a Container

```python
##### Example Parameters
container_id = 'container_id_here'

##### Example Response
{'message': 'Container paused'}
```

#### Unpausing a Container

```python
##### Example Parameters
container_id = 'container_id_here'

##### Example Response
{'message': 'Container unpaused'}
```

#### Stopping a Container

```python
##### Example Parameters
container_id = 'container_id_here'

##### Example Response
{'message': 'Container stopped successfully'}
```

#### Restarting a Container

```python
##### Example Parameters
container_id = 'container_id_here'

##### Example Response
{'message': 'Container restarted successfully'}
```

#### Removing a Container

```python
##### Example Parameters
container_id = 'container_id_here'

##### Example Response
{'message': 'Container removed successfully'}
```

#### Inspecting a Container

```python
##### Example Parameters
container_id = 'container_id_here'

##### Example Response
Low-level information about the container as a dictionary.
```

#### Getting Container Logs

```python
##### Example Parameters
container_id = 'container_id_here'

##### Example Response
Container logs as a string or bytes.
```

#### Creating a New Image from a Container's Changes

```python
##### Example Parameters
container_id = 'container_id_here'

##### Example Response
docker.models.images.Image
```

#### Executing Commands Inside a Container

```python
##### Example Parameters
container_id = 'container_id_here'
cmd = 'echo "Hello World"'

##### Example Response
{'exit_code': 0, 'output': 'Hello World\n'}
```
#### Error Handling

When interacting with Docker containers, various errors may occur. To gracefully handle these situations, the `DockerContainers` class should be capable of capturing these errors and providing information about them. The error handling mechanism ensures you can understand the problems that may occur when operating Docker containers and take appropriate action.

If an error occurs during an operation, such as attempting to start a non-existing container or trying to create one from a non-existing image, the response will include an error code and message. This makes troubleshooting and problem resolution more straightforward.

When handling errors, you can expect an error response similar to the following:

```python
# Attempting an operation that may cause an error
try:
    container = docker_containers.start(container_id='nonexisting_container_id')
except docker.errors.ContainerError as e:
    # Catching specific Docker container errors
    error_response = {
        "error": {
            "code": e.status_code,
            "message": e.explanation
        }
    }
except docker.errors.ImageNotFound as e:
    # Catching errors when the image is not found during pulling
    error_response = {
        "error": {
            "code": e.status_code,
            "message": "Image not found: {}".format(e.explanation)
        }
    }
except docker.errors.APIError as e:
    # Catching other Docker API errors
    error_response = {
        "error": {
            "code": e.status_code,
            "message": "Docker API error: {}".format(e.explanation)
        }
    }
except Exception as e:
    # Catching all other exceptions
    error_response = {
        "error": {
            "code": "unknown",
            "message": "An unknown error occurred: {}".format(str(e))
        }
    }
```

##### Example Error Response:

```json
{
  "error": {
    "code": 404,
    "message": "The specified container could not be found: nonexisting_container_id"
  }
}
```