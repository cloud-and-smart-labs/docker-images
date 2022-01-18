# Docker Support
Docker support repository contains all the Dockerfile, Docker-Compose files with the source code of application components.

## Table of Contents
- [Docker Image Building](#docker-image-building)
- [Docker Buildx](#docker-buildx)

## Docker Image Building
There must be a docker file to build an image.
### Build
```bash
docker image build -t username/image_name:image_tag .
```
### Push to Docker Hub
A [Docker Hub](https://hub.docker.com/) account is required.
```bash
docker login
```
Push the image to the Docker Hub.
```bash
docker push username/image_name:image_tag

```

## Docker Buildx
Create Docker Image that supports multiple CPU architectures.

### Create a new builder
```bash
docker buildx ls
```
```bash
docker buildx create --name crossbuild
```
```bash
docker buildx use crossbuild
```
```bash
docker buildx inspect --bootstrap
```


### Build the image for multiple CPU architectures and push it to the Docker Hub
The image will be available for the CPU architecture:
- linux/arm64
- linux/amd64
- linux/arm/v7
- linux/arm/v6

```bash
docker buildx build --platform linux/arm64,linux/amd64,linux/arm/v7,linux/arm/v6 -t username/image_name:image_tag --push .
```