# docker run
docker run -it --rm ubuntu:20.04 /bin/bash

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
    openssh-server \
    pkg-config \
    libmysqlclient-dev
    && rm -rf /var/lib/apt/lists/*

docker ps

# docker exec command
docker exec -it --user root mysql-hive-metastore bash
docker exec -it --user root hive bash
docker exec -it --user root spark bash
docker exec -it --user root airflow bash
docker exec -it --user root oracle-oltp bash

# docker commit command
docker commit hadoop-master hadoop-master-image
docker commit hadoop-worker1 hadoop-worker1-image
docker commit hadoop-worker2 hadoop-worker2-image
docker commit mysql-hive-metastore mysql-hive-metastore
docker commit hive hive
docker commit spark spark
docker commit oracle-oltp oracle-oltp
docker commit airflow airflow
# docker compose command
docker compose -f docker-compose-bigdata.yml up -d

# hive
/opt/hive/bin/hive --service metastore
/opt/hive/bin/hive --service hiveserver2

# spark
conda activate pyspark_env
pyspark --master yarn --deploy-mode client

# airflow
cd /opt/airflow
source airflow-env/bin/activate
airflow webserver -D
airflow scheduler -D

# run docker
docker compose -f docker-compose-bigdata.yml up -d
docker compose -f docker-compose-bigdata.yml up -d spark
