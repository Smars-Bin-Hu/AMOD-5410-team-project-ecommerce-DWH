# Log in Hive 
docker exec -it --user root hive bash

# run
/opt/hive/bin/hive --service metastore 
# after 5 seconds
/opt/hive/bin/hive --service hiveserver2

# check listening ports
netstat -nltp # check 10000, 10002, 9083