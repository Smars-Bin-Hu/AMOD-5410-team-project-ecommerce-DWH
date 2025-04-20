# spark_command.py

def build_spark_submit_command(
        deploy_mode: str,
        resources: dict,
        job_args: list,
        script_path: str
) -> str:
    """
        Build Spark on Yarn command

    :param deploy_mode:
    :param resources:
    :param job_args:
    :param script_path:
    :return: spark-submit command string
    """
    if deploy_mode != "cluster" and deploy_mode != "client":
        raise ValueError("deploy_mode must be cluster or client")
    if not resources:
        raise ValueError("resources must be a dict")
    if not job_args:
        raise ValueError("job_args must be a list")
    if not script_path:
        raise ValueError("script_path must be a string")

    resource_str = " ".join([f"{k} {v}" for k, v in resources.items()])
    job_arg_str = " ".join(job_args)

    cmd = (
        "/opt/miniconda3/bin/conda run -n pyspark_env "
        "/opt/spark/bin/spark-submit --master yarn "
        f"--deploy-mode {deploy_mode} "
        f"{resource_str} {script_path} {job_arg_str} "
        ">> /tmp/logs/spark/spark_job_{{ execution_date }}.log 2>&1"
    )

    return cmd
