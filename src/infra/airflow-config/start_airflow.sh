#!/bin/bash
source /opt/airflow/airflow-env/bin/activate  # 进入虚拟环境
pkill -9 -f "airflow";                        # 彻底杀掉所有进程后重启
pkill -9 -f "gunicorn";                         
airflow webserver -D                          # 启动 Web 服务器
airflow scheduler -D                          # 启动调度器