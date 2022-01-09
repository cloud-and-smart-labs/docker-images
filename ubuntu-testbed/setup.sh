apt update -y && apt upgrade -y;
apt install openssh-server -y;
curl -fsSL https://get.docker.com | sh;
service docker start;
service ssh start;
adduser pi;
usermod -aG sudo pi;
usermod -aG docker pi;
su - pi;