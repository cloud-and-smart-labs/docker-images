# USB Serial Port

USB port: `/dev/ttyACM0`

## Build Image use locally
```bash
docker image build -t suvambasak/serial:usb .
```
## Start container
```bash
docker container run -it --device=/dev/ttyACM0:/dev/ttyACM0 suvambasak/serial:usb
```

<!-- ## Compose file
```bash
docker-compose up -d
```
```bash
docker-compose down
``` -->