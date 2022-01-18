# USB Serial Port

USB port: `/dev/ttyACM0`

## Start container
```bash
docker container run -it --device=/dev/ttyACM0:/dev/ttyACM0 suvambasak/serial:usb
```