import docker
docker_url = "http://192.168.15.253:2375"
client = docker.DockerClient(base_url=docker_url)
container_environment = {
    "NAME": "c5n",
}
container_environment['YOUTUBE'] = "https://www.youtube.com/watch?v=vXRaQ0niKWE"
container_volume = {
    "stream": "/stream",
}
container = client.containers.run(
    detach=True,
    command='/start.sh',
    name="tv-c5n",
    image='tv/reflector',
    environment=container_environment,
    restart_policy='always',
    volumes=container_volume
)
