# Docker Images and Docker Compose

## Build Image use locally
```bash
docker image build -t suvambasak/pyimg:test .
```
## Push to Docker hub
```bash
docker login
```
```bash
docker push suvambasak/pyimg:test

```

## Multi-CPU Architecture Support
### Login 
```bash
docker login
```

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


### Build the image for multiple architecture and push to the registry
```bash
docker buildx build --platform linux/arm64,linux/amd64,linux/arm/v7,linux/arm/v6 -t suvambasak/pyimg:test --push .
```