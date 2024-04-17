### Image Management
The `DockerImages` class provides a range of methods for managing Docker images, including building, pulling, pushing, listing, retrieving, deleting, and cleaning up images.

#### How To Use

First, ensure you have the Docker daemon running and that you have the necessary permissions to interact with Docker.

Instantiate the class:

```python
from your_module_name import DockerImages  # Replace your_module_name with the actual name of your module

docker_images = DockerImages()
```

#### Building Images

Build an image from a Dockerfile:

```python
build_result = docker_images.build(path="..", tag="my-image:latest")
```

##### Example Response:

```json
{
  "id": "sha256:1a2b3c4d5e6f...",
  "tag": ["my-image:latest"]
}
```

#### Pulling Images

Pull an image from the repository:

```python
pull_result = docker_images.pull(repository="ubuntu", tag="latest")
```

##### Example Response:

```json
{
  "id": "sha256:1a2b3c4d5e...",
  "tag": ["ubuntu:latest"]
}
```

#### Pushing Images

Push an image to the repository:

```python
push_result = docker_images.push(repository="myusername/my-image", tag="latest")
```

##### Example Response:

```json
{
  "response": "The push refers to repository [docker.io/myusername/my-image]"
}
```

#### Listing Images

List all images:

```python
list_result = docker_images.list()
```

##### Example Response:

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

#### Retrieving Images

Retrieve a specific image by ID:

```python
get_result = docker_images.get(image_id="sha256:1a2b3c4d5e6f")
```

##### Example Response:

```json
{
  "id": "sha256:1a2b3c4d5e6f...",
  "tags": ["ubuntu:latest"]
}
```

#### Deleting Images

Delete an image by ID:

```python
remove_result = docker_images.remove(image_id="sha256:1a2b3c4d5e6f")
```

##### Example Response:

```json
{
  "result": "success"
}
```

#### Cleaning Up Unused Images

Clean up unused images:

```python
prune_result = docker_images.prune()
```

##### Example Response:

```json
{
  "images_deleted": [
    {"Deleted": "sha256:1a2b3c4d5e6f..."},
    {"Deleted": "sha256:7h8i9j0k1l..."}
  ],
  "space_reclaimed": 1234567
}
```

#### Error Handling

If an error occurs, the response will include an error code and message, indicating what went wrong. For example, if you try to pull an image that doesn't exist:

```python
error_response = docker_images.pull(repository="nonexisting", tag="latest")
```

##### Example Error Response:

```json
{
  "error": {
    "code": 404,
    "message": "pull access denied for nonexisting, repository does not exist or may require 'docker login': denied: requested access to the resource is denied"
  }
}
```