# first db init
airflow db init

# enter the virtual environment
source /opt/airflow/airflow-env/bin/activate

# create user
airflow users create \
      --username smars \
      --firstname smars \
      --lastname hu \
      --role Admin \
      --email hubin.smars@gmail.com

