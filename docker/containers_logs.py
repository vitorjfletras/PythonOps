#!/usr/bin/python

# DOC: docker-py.readthedocs.io
import docker


# Connect to Docker API
HOST_DOCKER = 'unix:/var/run/docker.sock'
client = docker.DockerClient(base_url=HOST_DOCKER)

# docker container run --name web -d -P httpd

container_id = '_CONTAINERID_'

getId = client.containers.get(container_id)

for line in getId.logs(stream=True):
    print(line.strip())
