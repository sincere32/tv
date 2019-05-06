class Client():

    @property
    def is_connected(self):
        return self.__connected

    def __init__(self, channel):

        self.__channel = channel
        self.__channel.name = self.__channel.name.replace(" ", "-")
        self.__container_name = "tv-"+self.__channel.name
        import docker
        docker_url = "http://"+channel.server.address+":"+channel.server.api_port
        try:
            self.__client = docker.DockerClient(base_url=docker_url)
            self.__connected = True
        except:
            self.__client = False
            self.__connected = False

    def start_channel(self):
        container_environment = {
        }
        container_environment["NAME"] = self.__channel
        container_volume = {
            "stream": {
                "bind": "/stream",
                "mode": "rw",
            }
        }

        if self.__channel.source_type == 'YouTube':
            container_environment['INPUT'] = "$(youtube-dl -g " + \
                self.__channel.source+")"
        else:
            container_environment['INPUT'] = self.__channel.source

        try:
            container = self.__client.containers.get(self.__container_name)
            container.remove(force=True)
        except:
            try:
                container = self.__client.containers.run(
                    detach=True,
                    name=self.__container_name,
                    image='tv/reflector',
                    environment=container_environment,
                    restart_policy={"name": 'always'},
                    volumes=container_volume,
                )
            except:
                container = False

        return container

    def stop_channel(self):
        try:
            container = self.__client.containers.get(self.__container_name)
            container.stop()
            return True
        except:
            return False

    def status_channel(self):
        try:
            container = self.__client.containers.get("tv-"+self.__channel.name)
            if container.status == 'running':
                return True
            else:
                return False
        except:
            return False