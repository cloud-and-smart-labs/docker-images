apt update -y && apt upgrade -y;
apt install curl vim nano apt-utils git python3 python3-pip net-tools -y;
curl -fsSL https://get.docker.com | sh ;
service docker start ;
pip3 install opera --no-cache-dir ;