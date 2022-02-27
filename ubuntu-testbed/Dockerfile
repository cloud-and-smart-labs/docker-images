FROM ubuntu:20.04
WORKDIR /root
COPY docker-setup.sh .
COPY ssh-setup.sh .
RUN chmod +x docker-setup.sh ssh-setup.sh
RUN apt update -y && apt upgrade -y 
RUN apt install curl vim nano apt-utils git python3 python3-pip net-tools openssh-client iputils-ping -y
RUN pip3 install opera --no-cache-dir
CMD [ "bash"]