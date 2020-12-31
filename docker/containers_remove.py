#!/usr/bin/python

# DOC: docker-py.readthedocs.io
import docker
import sys

args = sys.argv


# Connect to Docker API
HOST_DOCKER = 'unix:/var/run/docker.sock'
client = docker.DockerClient(base_url=HOST_DOCKER)


def remove_container(container_id):
    try:
        getInfo = client.containers.get(container_id)
        container_name = getInfo.name
        print('Container found')
        try:
            remove = get.remove(force=True) # force=True if container is running.
            print(f'Container {container_name} successfully removed!')
        except Exception as err:
            print(f'Failed to remove the container: {container_id}')
    except Exception as err:
        print('Container NOT found')

if len(args) <= 1:
    print(f'Container id is missing')
    print(f'Usage: python3 containers_remove.py _CONTAINERID_')
else:
    container_id = args[1]
    print(f'Container id {container_id}')
    remove_container(container_id)