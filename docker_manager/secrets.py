import docker
from typing import Dict, List, Any

from . import DockerClientSingleton

class DockerSecrets:
    def __init__(self):
        self.client = DockerClientSingleton.get_client()

    def create_secret(self, **kwargs) -> Dict[str, Any]:
        """Create a secret and return its id."""
        try:
            secret = self.client.secrets.create(**kwargs)
            return {'id': secret.id}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except Exception as e:
            return {'error': {'message': str(e)}}

    def list_secrets(self) -> List[Dict[str, Any]]:
        """List all secrets with their ids and names."""
        try:
            secrets = self.client.secrets.list()
            return [{'id': secret.id, 'name': secret.name} for secret in secrets]
        except docker.errors.APIError as e:
            return [{'error': {'code': e.response.status_code, 'message': e.explanation}}]
        except Exception as e:
            return [{'error': {'message': str(e)}}]

    def get_secret_details(self, secret_id: str) -> Dict[str, Any]:
        """Get details of a specific secret by its id."""
        try:
            secret = self.client.secrets.get(secret_id)
            return {'id': secret.id, 'name': secret.name}
        except docker.errors.NotFound as e:
            return {'error': {'code': e.response.status_code, 'message': 'Secret not found'}}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except Exception as e:
            return {'error': {'message': str(e)}}

    def remove_secret(self, secret_id: str) -> Dict[str, Any]:
        """Remove a secret by its id."""
        try:
            secret = self.client.secrets.get(secret_id)
            secret.remove()
            return {'message': 'Secret removed'}
        except docker.errors.NotFound as e:
            return {'error': {'code': e.response.status_code, 'message': 'Secret not found'}}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except Exception as e:
            return {'error': {'message': str(e)}}