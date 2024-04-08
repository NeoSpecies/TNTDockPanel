import docker
from typing import Dict, Any
from . import DockerClientSingleton


class DockerPlugins:
    def __init__(self):
        self.client = DockerClientSingleton.get_client()

    def install(self, name: str, **options) -> Dict[str, Any]:
        try:
            plugin = self.client.plugins.install(name, **options)
            return {'message': f'Plugin {name} installed'}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}

    def configure(self, plugin_name: str, **kwargs) -> Dict[str, Any]:
        # Placeholder for actual configure logic
        try:
            # Actual implementation may vary significantly
            return {'message': f'Plugin {plugin_name} configured'}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}

    def remove(self, plugin_name: str) -> Dict[str, Any]:
        try:
            plugin = self.client.plugins.get(plugin_name)
            plugin.remove()
            return {'message': f'Plugin {plugin_name} removed'}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}

    def list(self) -> Dict[str, Any]:
        try:
            plugins = self.client.plugins.list()
            plugins_info = [{'name': plugin.name, 'id': plugin.id, 'enabled': plugin.attrs['Enabled']} for plugin in plugins]
            return {'plugins': plugins_info}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}

    def details(self, plugin_name: str) -> Dict[str, Any]:
        try:
            plugin = self.client.plugins.get(plugin_name)
            return {'name': plugin.name, 'id': plugin.id, 'enabled': plugin.attrs['Enabled'], 'settings': plugin.attrs['Settings']}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}
