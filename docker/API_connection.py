#!/usr/bin/python

# DOC: docker-py.readthedocs.io
import docker


# Connect to Docker API
HOST_DOCKER = 'unix:/var/run/docker.sock'

client = docker.DockerClient(base_url=HOST_DOCKER)

docker_info = client.version()

components = docker_info['Components']
print(components)

#Docker info
for component in components:
    if component['Name'] == 'Engine':
        version = component['Version']
        print(f'Docker Engine version is {version}')
