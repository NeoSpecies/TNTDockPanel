import docker
from typing import Dict, List, Any

from . import DockerClientSingleton


class DockerNetworks:
    def __init__(self):
        self.client = DockerClientSingleton.get_client()

    def create(self, **kwargs) -> Dict[str, Any]:
        """Create a network and return its id."""
        try:
            network = self.client.networks.create(**kwargs)
            return {'id': network.id, 'name': network.name}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}

    def list(self, **kwargs) -> List[Dict[str, Any]]:
        """List networks and return a list of ids and names."""
        try:
            networks = self.client.networks.list(**kwargs)
            return [{'id': net.id, 'name': net.name} for net in networks]
        except docker.errors.APIError as e:
            return [{'error': {'code': e.response.status_code, 'message': e.explanation}}]
        except docker.errors.DockerException as e:
            return [{'error': {'message': str(e)}}]

    def get(self, network_id: str) -> Dict[str, Any]:
        """Get a network and return its id and name."""
        try:
            network = self.client.networks.get(network_id)
            return {'id': network.id, 'name': network.name}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}

    def remove(self, network_id: str) -> Dict[str, Any]:
        """Remove a network and return a success message."""
        try:
            network = self.client.networks.get(network_id)
            network.remove()
            return {'result': 'success', 'message': f'Network {network_id} removed'}
        except docker.errors.NotFound as e:
            return {'error': {'code': 404, 'message': 'Network not found'}}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}

    def prune(self) -> Dict[str, Any]:
        """Prune unused networks and return the amount of reclaimed space."""
        try:
            pruned_networks = self.client.networks.prune()
            return {
                'networks_deleted': pruned_networks['NetworksDeleted'],
                'space_reclaimed': pruned_networks['SpaceReclaimed']
            }
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}