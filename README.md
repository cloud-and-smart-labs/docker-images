# Docker Images

## Build Image use locally
```bash
$ sudo chmod +x start.sh
$ ./start.sh
```

## Multi-CPU Architecture Support
Login 
```bash
$ ​​docker login
```

Create a new builder
```bash
$ docker buildx ls
$ docker buildx create --name crossbuild
$ docker buildx use crossbuild
$ docker buildx inspect --bootstrap
```

Build the image for multiple architecture and push to the registry
```bash
$ docker buildx build --platform linux/arm64,linux/amd64,linux/arm/v7,linux/arm/v6 -t suvambasak/pyimg:1 --push .
```