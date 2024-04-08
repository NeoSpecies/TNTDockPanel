import docker
from typing import Dict, List, Any

from . import DockerClientSingleton


class DockerServices:
    def __init__(self):
        self.client = DockerClientSingleton.get_client()

    def create_service(self, service_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a service and return its id."""
        try:
            service = self.client.services.create(**service_data)
            return {'id': service.id}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}

    def list_services(self) -> List[Dict[str, Any]]:
        """List all services and their details."""
        try:
            services = self.client.services.list()
            services_info = [{'id': service.id, 'name': service.name, 'attrs': service.attrs} for service in services]
            return services_info
        except docker.errors.APIError as e:
            return [{'error': {'code': e.response.status_code, 'message': e.explanation}}]
        except docker.errors.DockerException as e:
            return [{'error': {'message': str(e)}}]

    def get_service(self, service_id: str) -> Dict[str, Any]:
        """Get a service details by its id."""
        try:
            service = self.client.services.get(service_id)
            return {'id': service.id, 'name': service.name, 'attrs': service.attrs}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.NotFound as e:
            return {'error': {'message': 'Service not found'}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}

    def update_service(self, service_id: str, service_data: Dict[str, Any]) -> Dict[str, Any]:
        """Update a service and return a message."""
        try:
            service = self.client.services.get(service_id)
            version = service.attrs['Version']['Index']
            service.update(version=version, **service_data)
            return {'message': 'Service updated'}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}

    def remove_service(self, service_id: str) -> Dict[str, Any]:
        """Remove a service by its id."""
        try:
            service = self.client.services.get(service_id)
            service.remove()
            return {'message': 'Service removed'}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.NotFound as e:
            return {'error': {'message': 'Service not found'}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}
