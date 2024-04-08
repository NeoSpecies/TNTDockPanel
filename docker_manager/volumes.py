import docker
from typing import Dict, List, Any

from . import DockerClientSingleton


class DockerVolume:
    def __init__(self):
        self.client = DockerClientSingleton.get_client()

    def list(self) -> List[Dict[str, Any]] | Dict[str, Dict[str, Any]]:
        """List volumes and return their information."""
        try:
            volumes = self.client.volumes.list()
            volumes_info = [{'name': vol.name, 'driver': vol.attrs['Driver'], 'mountpoint': vol.attrs['Mountpoint']} for
                            vol in volumes]
            return volumes_info
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}

    def get(self, volume_name: str) -> Dict[str, Any]:
        """Get a volume by name and return its information."""
        try:
            volume = self.client.volumes.get(volume_name)
            return {'name': volume.name, 'driver': volume.attrs['Driver'], 'mountpoint': volume.attrs['Mountpoint']}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}

    def remove(self, volume_name: str, force: bool = False) -> Dict[str, str]:
        """Remove a volume by name."""
        try:
            volume = self.client.volumes.get(volume_name)
            volume.remove(force=force)
            return {'message': 'Volume removed'}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}

    def prune(self) -> Dict[str, Any]:
        """Prune unused volumes and return the amount of reclaimed space."""
        try:
            pruned_volumes = self.client.volumes.prune()
            return {'VolumesDeleted': pruned_volumes.get('VolumesDeleted'),
                    'SpaceReclaimed': pruned_volumes.get('SpaceReclaimed')}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}

    def create(self, volume_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a volume and return its information."""
        try:
            volume = self.client.volumes.create(**volume_data)
            return {'name': volume.name}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}
