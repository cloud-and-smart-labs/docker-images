# docker container run -v /tmp:/home --security-opt seccomp=unconfined suvambasak/pyimg:swarm
docker container run -v /tmp:/home -p 80:5000 -d suvambasak/pyimg:swarm