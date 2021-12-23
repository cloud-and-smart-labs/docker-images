# Ubuntu Testbed (Docker, xOpera, Ansible, Git)

## Build Image use locally
```bash
docker image build -t suvambasak/ubuntu:testbed .
```
## Start container
```bash
docker container run -it --privileged --rm suvambasak/ubuntu:testbed
```

## Setup
Inside container execute the shell script.
```bash
./setup.sh
```

<!-- ## Compose file
```bash
docker-compose up -d
```
```bash
docker-compose down
``` -->