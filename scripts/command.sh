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
    && rm -rf /var/lib/apt/lists/*

apt update && apt install -y \
    pkg-config \
    libmysqlclient-dev

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

# oracle
docker run -d --name oracle-oltp \
    --network bigdata-net \
    -p 1521:1521 -p 5500:5500 \
    -e ORACLE_SID=ORCLCDB \
    -e ORACLE_PDB=ORCLPDB1 \
    -e ORACLE_PWD=MyStrongPassw0rd \
    -e ORACLE_CHARACTERSET=AL32UTF8 \
    oracle/database:19.3.0-ee

# spark
conda activate pyspark_env
pyspark --master yarn --deploy-mode client

# airflow
cd /opt/airflow
source airflow-env/bin/activate
airflow webserver -D
airflow scheduler -D
