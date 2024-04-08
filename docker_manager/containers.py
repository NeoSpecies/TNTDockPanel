import docker
from typing import Any, Dict, List
from . import DockerClientSingleton


class DockerContainers:
    def __init__(self):
        self.client = DockerClientSingleton.get_client()

    def run(self, **kwargs) -> docker.models.containers.Container:
        """Create and run a new container."""
        return self.client.containers.run(**kwargs)

    def create(self, **kwargs) -> docker.models.containers.Container:
        """Create a new container without starting it."""
        return self.client.containers.create(**kwargs)

    def start(self, container_id: str, **kwargs) -> Dict[str, Any]:
        """Start a container."""
        try:
            container = self.client.containers.get(container_id)
            container.start(**kwargs)
            return {'message': 'Container started'}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}

    def get_info(self, container_id: str) -> docker.models.containers.Container:
        """Get information about a specific container."""
        return self.client.containers.get(container_id)

    def get_list(self, **kwargs) -> List[Dict[str, Any]]:
        """List all containers with optional filters."""
        containers = self.client.containers.list(**kwargs)
        return [{'container_id': c.id, 'status': c.status} for c in containers]

    def get_stats(self, container_id: str, **kwargs) -> Dict[str, Any]:
        """Get real-time stats for a container."""
        try:
            container = self.client.containers.get(container_id)
            stats = container.stats(**kwargs)
            return stats
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}

    def top(self, container_id: str, **kwargs) -> Dict[str, Any]:
        """List processes inside a container."""
        try:
            container = self.client.containers.get(container_id)
            top_result = container.top(**kwargs)
            return top_result
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}

    def get_archive(self, container_id: str, path: str, **kwargs) -> Any:
        """Retrieve a file/folder archive from a container."""
        try:
            container = self.client.containers.get(container_id)
            response = container.get_archive(path, **kwargs)
            return response
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}

    def put_archive(self, container_id: str, path: str, data: Any) -> Dict[str, Any]:
        """Upload an archive of files to a container's filesystem."""
        try:
            container = self.client.containers.get(container_id)
            result = container.put_archive(path, data)
            return {'success': result}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}

    def rename(self, container_id: str, name: str) -> Dict[str, Any]:
        """Rename a container."""
        try:
            container = self.client.containers.get(container_id)
            container.rename(name)
            return {'message': 'Container renamed'}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}

    def pause(self, container_id: str) -> Dict[str, Any]:
        """Pause a container."""
        try:
            container = self.client.containers.get(container_id)
            container.pause()
            return {'message': 'Container paused'}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}

    def unpause(self, container_id: str) -> Dict[str, Any]:
        """Unpause a container."""
        try:
            container = self.client.containers.get(container_id)
            container.unpause()
            return {'message': 'Container unpaused'}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}

    # 调整容器的tty大小。
    def resize(self, container_id, **kwargs):
        try:
            container = self.client.containers.get(container_id)
            container.resize(**kwargs)
            return {'message': 'Container resized'}
        except docker.errors.APIError as e:
            message = {
                'error': e.response.status_code,
                'message': e.explanation
            }
            return {'error': message}

    def stop(self, container_id: str, **kwargs) -> Dict[str, Any]:
        """Stop a container."""
        try:
            container = self.client.containers.get(container_id)
            container.stop(**kwargs)
            return {'message': 'Container stopped successfully'}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}

    def restart(self, container_id: str, **kwargs) -> Dict[str, Any]:
        """Restart a container."""
        try:
            container = self.client.containers.get(container_id)
            container.restart(**kwargs)
            return {'message': 'Container restarted successfully'}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}

    def remove(self, container_id: str, **kwargs) -> Dict[str, Any]:
        """Remove a container."""
        try:
            container = self.client.containers.get(container_id)
            container.remove(**kwargs)
            return {'message': 'Container removed successfully'}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}

    def inspect(self, container_id: str) -> Dict[str, Any]:
        """Inspect a container and retrieve low-level information."""
        try:
            container = self.client.containers.get(container_id)
            return container.attrs
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}

    def logs(self, container_id: str, **kwargs) -> dict[str, dict[str, Any]] | Any:
        """Fetch the logs of a container."""
        try:
            container = self.client.containers.get(container_id)
            return container.logs(**kwargs)
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}

    def commit(self, container_id: str, **kwargs) -> docker.models.images.Image:
        """Create a new image from a container's changes."""
        try:
            container = self.client.containers.get(container_id)
            return container.commit(**kwargs)
        except docker.errors.NotFound as e:
            return {'error': {'message': 'Container not found'}}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}

    def exec_run(self, container_id: str, cmd, **kwargs) -> Dict[str, Any]:
        """Run a command inside a container."""
        try:
            container = self.client.containers.get(container_id)
            exec_log = container.exec_run(cmd, **kwargs)
            return {'exit_code': exec_log.exit_code, 'output': exec_log.output}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
