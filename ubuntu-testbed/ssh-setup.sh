export DEBIAN_FRONTEND=noninteractive
apt update -y && apt upgrade -y;
apt install openssh-server -y;
passwd root;
vim /etc/ssh/sshd_config
service ssh start;