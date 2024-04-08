import docker


class DockerClientSingleton:
    _client = None

    @classmethod
    def get_client(cls):
        if cls._client is None:
            cls._client = docker.from_env()
        return cls._client
