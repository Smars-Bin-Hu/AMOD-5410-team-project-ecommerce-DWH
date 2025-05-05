# Docker Commands

Docker Launching
```bash
docker compose -f docker-compose-bigdata.yml up -d
```

Check current running container
```bash
docker ps
```

Log in Docker Container 
```bash
docker exec -it --user root hadoop-master bash
docker exec -it --user root hadoop-worker1 bash
docker exec -it --user root hadoop-worker2 bash
docker exec -it --user root mysql-hive-metastore bash
docker exec -it --user root hive bash
docker exec -it --user root spark bash
docker exec -it --user root airflow bash
docker exec -it --user root oracle-oltp bash
docker exec -it --user root monitoring bash
```

Docker Commit container as Image
```bash
docker commit hadoop-master smarsbhu/proj1-dwh-cluster:hadoop-master-smars-1.1.2
docker commit hadoop-worker1 smarsbhu/proj1-dwh-cluster:hadoop-worker1-smars-1.1.2
docker commit hadoop-worker2 smarsbhu/proj1-dwh-cluster:hadoop-worker2-smars-1.1.2
docker commit mysql-hive-metastore  smarsbhu/proj1-dwh-cluster:mysql-hive-metastore-smars-1.1.2
docker commit hive smarsbhu/proj1-dwh-cluster:hive-smars-1.1.2
docker commit spark smarsbhu/proj1-dwh-cluster:spark-smars-1.1.1
docker commit oracle-oltp smarsbhu/proj1-dwh-cluster:oracle-oltp-smars-1.1.1
docker commit airflow smarsbhu/proj1-dwh-cluster:airflow-smars-1.1.1
docker commit monitoring smarsbhu/proj1-dwh-cluster:monitoring-smars-1.1.0
```

## DockerHub Images

Push images to Docker Hub
```bash
docker push smarsbhu/proj1-dwh-cluster:hadoop-master-smars-1.1.2
docker push smarsbhu/proj1-dwh-cluster:hadoop-worker1-smars-1.1.2
docker push smarsbhu/proj1-dwh-cluster:hadoop-worker2-smars-1.1.2
docker push smarsbhu/proj1-dwh-cluster:hive-smars-1.1.2
docker push smarsbhu/proj1-dwh-cluster:mysql-hive-metastore-smars-1.1.2
docker push smarsbhu/proj1-dwh-cluster:oracle-oltp-smars-1.1.1
docker push smarsbhu/proj1-dwh-cluster:spark-smars-1.1.1
docker push smarsbhu/proj1-dwh-cluster:airflow-smars-1.1.1
docker push smarsbhu/proj1-dwh-cluster:monitoring-smars-1.1.0
```

