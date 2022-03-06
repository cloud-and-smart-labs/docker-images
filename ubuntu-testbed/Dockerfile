FROM ubuntu:20.04
ARG DEBIAN_FRONTEND=noninteractive
WORKDIR /root
RUN apt update -y && apt upgrade -y 
RUN apt install curl nano apt-utils git python3 python3-pip net-tools openssh-client iputils-ping systemd -y 
RUN pip3 install opera --no-cache-dir
COPY *.sh .
RUN chmod +x docker-setup.sh ssh-setup.sh
CMD [ "/bin/bash"]