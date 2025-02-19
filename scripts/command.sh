# apt update and install common use tools
apt update && apt install -y \
    iputils-ping \
    net-tools \
    netcat \
    procps \
    vim \
    nano \
    curl \
    wget \
    telnet \
    dnsutils \
    htop \
    tree \
    && rm -rf /var/lib/apt/lists/*

# docker exec command
docker exec -it --user root mysql-hive-metastore bash
docker exec -it --user root hive bash
docker exec -it --user root spark bash

# docker commit command
docker commit hadoop-master hadoop-master-image
docker commit hadoop-worker1 hadoop-worker1-image
docker commit hadoop-worker2 hadoop-worker2-image
docker commit mysql-hive-metastore mysql-hive-metastore
docker commit hive hive
docker commit spark spark
# docker compose command
docker compose -f docker-compose-bigdata.yml up -d



docker run -it --name spark --network bigdata-net ubuntu:20.04 bash

conda activate pyspark_env