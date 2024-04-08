import docker
from typing import Dict, Any

from . import DockerClientSingleton

class DockerConfigs:
    def __init__(self):
        self.client = DockerClientSingleton.get_client()

    def create_config(self, **kwargs) -> Dict[str, Any]:
        """Create a config and return its id."""
        try:
            config = self.client.configs.create(**kwargs)
            return {'id': config.id}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}

    def list_configs(self) -> Dict[str, Any]:
        """List all configs and return their details."""
        try:
            configs = self.client.configs.list()
            configs_info = [{'id': config.id, 'name': config.name} for config in configs]
            return {'configs': configs_info}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}

    def get_config_details(self, config_id: str) -> Dict[str, Any]:
        """Get details of a specific config."""
        try:
            config = self.client.configs.get(config_id)
            return {'id': config.id, 'name': config.name}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.NotFound as e:
            return {'error': {'message': 'Config not found', 'code': 404}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}

    def remove_config(self, config_id: str) -> Dict[str, Any]:
        """Remove a specific config."""
        try:
            config = self.client.configs.get(config_id)
            config.remove()
            return {'message': 'Config removed'}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.NotFound as e:
            return {'error': {'message': 'Config not found', 'code': 404}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}