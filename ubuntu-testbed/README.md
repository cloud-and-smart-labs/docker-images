# Ubuntu Testbed
To test Dynamic Deployment on a single machine.

## Build Image
```bash
docker image build -t suvambasak/ubuntu:latest .
```
## Start Container in Privileged Mode
```bash
docker container run -it --privileged --rm suvambasak/ubuntu:latest
```

## Setup
Inside the container execute the shell script `setup.sh` to install Docker Engine and create a user called `pi` automatically.
```bash
./setup.sh
```