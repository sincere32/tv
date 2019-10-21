import docker


class Client():

    @property
    def connected(self):
        return self.__connected

    @property
    def error(self):
        return self.__error

    def __init__(self, channel):

        self.__channel = channel
        self.__channel.name = self.__channel.name.replace(" ", "-")
        self.__container_name = "tv-" + \
            str(self.__channel.pk)+"-"+self.__channel.name
        docker_url = "http://{}:{}".format(channel.server.address,
                                           channel.server.api_port)
        self.__error = None

        try:
            self.__client = docker.DockerClient(base_url=docker_url)
            self.__connected = True
        except docker.errors.APIError as ex:
            self.__client = False
            self.__connected = False
            self.__error = ex

    def __repr__(self):
        return self.__connected

    def get_container(self):
        try:
            container = self.__client.containers.get(self.__container_name)
            return container
        except docker.errors.APIError as ex:
            self.__error = ex
            return False

    def start_channel(self):

        container_environment = {
        }

        if self.__channel.source_type == 'YouTube':
            container_environment['YOUTUBE_DL'] = self.__channel.source
        else:
            container_environment['INPUT'] = self.__channel.source

        container_environment["NAME"] = self.__channel
        container_environment['VCODEC'] = self.__channel.codec

        container_volume = {
            "tv-streams": {
                "bind": "/stream",
                "mode": "rw",
            }
        }

        restart_policy = {"Name": "always"}

        try:
            container = self.__client.containers.run(
                detach=True,
                name=self.__container_name,
                image='tv/reflector',
                restart_policy=restart_policy,
                environment=container_environment,
                volumes=container_volume,
                network_mode='host'
            )
        except docker.errors.APIError as ex:
            self.__error = ex
            container = False

        return container

    def stop_channel(self):
        try:
            container = self.get_container()
            if container:
                container.stop()
                return True
        except docker.errors.APIError as ex:
            self.__error = ex
            return False

    def delete_channel(self):
        try:
            container = self.get_container()
            if container:
                container.stop()
                container.remove()
                return True
        except docker.errors.APIError as ex:
            self.__error = ex
            return False

    def rename_channel(self, name):
        try:
            container = self.get_container()
            if container:
                name = name.replace(" ", "-")
                name = "tv-" + str(self.__channel.pk)+"-"+name
                container.rename(name)
                return True
        except docker.errors.APIError as ex:
            self.__error = ex
            return False

    def recreate_channel(self):
        try:
            container = self.get_container()
            if container:
                container.remove(force=True)
            container = self.start_channel()
        except:
            container = self.start_channel()
        return container
