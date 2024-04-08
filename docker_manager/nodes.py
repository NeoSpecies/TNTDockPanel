import docker
from typing import Dict, Any

from . import DockerClientSingleton


class DockerNodes:
    def __init__(self):
        self.client = DockerClientSingleton.get_client()

    def list_nodes(self) -> Dict[str, Any]:
        """List all nodes in the swarm."""
        try:
            nodes = self.client.nodes.list()
            nodes_info = [
                {
                    'id': node.id,
                    'hostname': node.attrs['Description']['Hostname'],
                    'status': node.attrs['Status']['State'],
                    'role': node.attrs['Spec']['Role']
                }
                for node in nodes
            ]
            return {'nodes': nodes_info}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except Exception as e:
            return {'error': {'message': str(e)}}

    def get_node_details(self, node_id: str) -> Dict[str, Any]:
        """Get details for a specific node."""
        try:
            node = self.client.nodes.get(node_id)
            return {
                'id': node.id,
                'hostname': node.attrs['Description']['Hostname'],
                'status': node.attrs['Status'],
                'role': node.attrs['Spec']['Role']
            }
        except docker.errors.NotFound:
            return {'error': {'message': f'Node {node_id} not found'}}
        except Exception as e:
            return {'error': {'message': str(e)}}

    def update_node(self, node_id: str, **kwargs) -> Dict[str, Any]:
        """Update a specific node."""
        try:
            node = self.client.nodes.get(node_id)
            version = node.attrs['Version']['Index']
            node.update(version=version, **kwargs)
            return {'message': 'Node updated'}
        except docker.errors.NotFound:
            return {'error': {'message': f'Node {node_id} not found'}}
        except Exception as e:
            return {'error': {'message': str(e)}}

    def remove_node(self, node_id: str) -> Dict[str, Any]:
        """Remove a specific node from the swarm."""
        try:
            node = self.client.nodes.get(node_id)
            node.remove()
            return {'message': 'Node removed'}
        except docker.errors.NotFound:
            return {'error': {'message': f'Node {node_id} not found'}}
        except Exception as e:
            return {'error': {'message': str(e)}}
