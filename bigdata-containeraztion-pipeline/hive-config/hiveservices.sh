#!/bin/bash
HIVE_LOG_DIR=$HIVE_HOME/logs
META_PID=/tmp/meta.pid
SERVER_PID=/tmp/server.pid
mkdir -p  $HIVE_LOG_DIR

function hive_start()
{
    nohup hive --service metastore >$HIVE_LOG_DIR/metastore.log 2>&1 &
    echo $! > $META_PID
    sleep 8
    nohup hive --service hiveserver2 >$HIVE_LOG_DIR/hiveserver2.log 2>&1 &
    echo $! > $SERVER_PID
}

function hive_stop()
{
    if [ -f $META_PID ]
    then
        cat $META_PID | xargs kill -9
        rm $META_PID
    else
        echo "META_PID file is missing，please turn off the service manully"
    fi
    if [ -f $SERVER_PID ]
    then
        cat $SERVER_PID | xargs kill -9
        rm $SERVER_PID
    else
        echo "Server2 PID file is missing，please turn off the service manully"
    fi
}

case $1 in
"start")
    hive_start
    ;;
"stop")
    hive_stop
    ;;
"restart")
    hive_stop
    sleep 2
    hive_start
    ;;
*)
    echo Invalid Args!
    echo 'Usage: '$(basename $0)' start|stop|restart'
    ;;
esac