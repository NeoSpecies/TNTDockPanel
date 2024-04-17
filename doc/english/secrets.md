### Secret Management

The `DockerSecrets` class provides a series of methods to manage Docker secrets, including creating, listing, retrieving detailed information, and deleting secrets.

#### How To Use

First, ensure you have the Docker daemon running and that you have the necessary permissions to interact with Docker.

Instantiate the class:

```python
from your_module_name import DockerSecrets  # Replace your_module_name with the actual name of your module

docker_secrets = DockerSecrets()
```

##### Create a Secret

Create a new secret:

```python
create_result = docker_secrets.create_secret(name="mysecret", data="secret_data_here")
```

###### Example Response:

```json
{
  "id": "k3mno4567pqr89stuvwx"
}
```

##### List Secrets

List all secrets:

```python
list_result = docker_secrets.list_secrets()
```

###### Example Response:

```json
{
  "secrets": [
    {"id": "abcd1234efgh5678ijkl", "name": "mysecret"}
  ]
}
```

##### Get Secret Details

Retrieve detailed information about a specific secret:

```python
get_result = docker_secrets.get_secret_details(secret_id="abcd1234efgh5678ijkl")
```

###### Example Response:

```json
{
  "id": "abcd1234efgh5678ijkl",
  "name": "mysecret"
}
```

##### Delete a Secret

Delete a secret by ID:

```python
remove_result = docker_secrets.remove_secret(secret_id="abcd1234efgh5678ijkl")
```

###### Example Response:

```json
{
  "message": "Secret removed"
}
```

#### Error Handling

If an error occurs, the response will include an error code and message, indicating what went wrong. For example, if you try to retrieve a non-existent secret:

```python
error_response = docker_secrets.get_secret_details(secret_id="nonexisting")
```

###### Example Error Response:

```json
{
  "error": {
    "code": 404,
    "message": "Secret not found"
  }
}
```