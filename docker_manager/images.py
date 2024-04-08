import docker
from typing import Dict, List, Any

from . import DockerClientSingleton


class DockerImages:
    def __init__(self):
        self.client = DockerClientSingleton.get_client()

    def build(self, **kwargs) -> Dict[str, Any]:
        """Build an image and return its id and tags."""
        try:
            image, build_log = self.client.images.build(**kwargs)
            return {'id': image.id, 'tag': image.tags}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.BuildError as e:
            return {'error': {'message': e.msg, 'build_log': e.build_log}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}

    def pull(self, repository: str, tag: str = None) -> Dict[str, Any]:
        """Pull an image and return its id and tags."""
        try:
            image = self.client.images.pull(repository, tag=tag)
            return {'id': image.id, 'tag': image.tags}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}

    def push(self, repository: str, tag: str = None) -> Dict[str, Any]:
        """Push an image and return the response."""
        try:
            response = self.client.images.push(repository, tag=tag)
            return {'response': response}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}

    def list(self, **kwargs) -> List[Dict[str, Any]]:
        """List images and return a list of ids and tags."""
        try:
            images = self.client.images.list(**kwargs)
            return [{'id': image.id, 'tags': image.tags} for image in images]
        except docker.errors.APIError as e:
            return [{'error': {'code': e.response.status_code, 'message': e.explanation}}]
        except docker.errors.DockerException as e:
            return [{'error': {'message': str(e)}}]

    def get(self, image_id: str) -> Dict[str, Any]:
        """Get an image and return its id and tags."""
        try:
            image = self.client.images.get(image_id)
            return {'id': image.id, 'tags': image.tags}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}

    def remove(self, image_id: str) -> Dict[str, Any]:
        """Remove an image and return a success message."""
        try:
            self.client.images.remove(image_id)
            return {'result': 'success'}
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}

    def prune(self) -> Dict[str, Any]:
        """Prune unused images and return the amount of reclaimed space."""
        try:
            pruned_images = self.client.images.prune()
            return {
                'images_deleted': pruned_images['ImagesDeleted'],
                'space_reclaimed': pruned_images['SpaceReclaimed']
            }
        except docker.errors.APIError as e:
            return {'error': {'code': e.response.status_code, 'message': e.explanation}}
        except docker.errors.DockerException as e:
            return {'error': {'message': str(e)}}