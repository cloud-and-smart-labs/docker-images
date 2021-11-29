# Docker Images (Python Flask API with volume)

## Change permission
```bash
sudo chmod +x start.sh build.sh
```
## Build Image use locally
```bash
./build.sh
```
## Start container
```bash
./build.sh
```

## Call API
```bash
curl localhost:80/sensor/12.2
```
## Compose file
```bash
docker-compose up -d
```