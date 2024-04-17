### Volume Management
The `DockerVolume` class offers a range of methods for managing Docker volumes, including listing, retrieving, deleting, pruning, and creating volumes.

#### How To Use

First, make sure you have the Docker daemon running and that you have the necessary permissions to interact with Docker.

Instantiate the class:

```python
from your_module_name import DockerVolume  # Replace your_module_name with the actual name of your module

docker_volume = DockerVolume()
```

#### List Volumes

List all volumes along with their information:

```python
list_result = docker_volume.list()
```

##### Example Response:

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

#### Retrieve Volume

Get information about a specific volume by name:

```python
get_result = docker_volume.get(volume_name="my-volume")
```

##### Example Response:

```json
{
  "name": "my-volume",
  "driver": "local",
  "mountpoint": "/var/lib/docker/volumes/my-volume/_data"
}
```

#### Delete Volume

Delete a specific volume by name:

```python
remove_result = docker_volume.remove(volume_name="my-volume", force=True)
```

##### Example Response:

```json
{
  "message": "Volume removed"
}
```

#### Prune Unused Volumes

Prune unused volumes and return the amount of space reclaimed:

```python
prune_result = docker_volume.prune()
```

##### Example Response:

```json
{
  "VolumesDeleted": ["my-unused-volume"],
  "SpaceReclaimed": 1024
}
```

#### Create Volume

Create a new volume and return its information:

```python
create_result = docker_volume.create(volume_data={"name": "new-volume", "driver": "local"})
```

##### Example Response:

```json
{
  "name": "new-volume"
}
```

### Error Handling

If an error occurs, the response will include an error code and message, indicating what went wrong.
. For example, if you try to delete a non-existing volume:

```python
error_response = docker_volume.remove(volume_name="nonexisting-volume")
```

##### Example Error Response:

```json
{
  "error": {
    "code": 404,
    "message": "Volume nonexisting-volume does not exist"
  }
