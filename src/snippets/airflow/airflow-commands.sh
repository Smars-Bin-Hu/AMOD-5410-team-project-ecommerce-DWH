# enter the virtual environment
source activate

# first db init
airflow db init

# create user
airflow users create \
      --username smars \
      --firstname smars \
      --lastname hu \
      --role Admin \
      --email hubin.smars@gmail.com

# dags unpause
airflow dags unpause etl_oltp_to_dwh_process

# run the airflow dag process
airflow dags trigger -e 2025-04-19 etl_oltp_to_dwh_process

# check the current dags list (under the dags folder)
airflow dags list

# check the dags_folder (could change in the airflow.cfg)
airflow  config get-value core dags_folder

