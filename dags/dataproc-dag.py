from airflow import DAG
from airflow import models
from airflow.providers.google.cloud.operators.dataproc import (
    DataprocClusterCreateOperator, DataprocClusterDeleteOperator, DataprocSubmitJobOperator,
    DataprocCreateClusterOperator, DataprocDeleteClusterOperator, DataprocSubmitJobOperator,
    DataprocUpdateClusterOperator,
)
from airflow.utils.dates import days_ago
from datetime import datetime,timedelta

project="data-engineering-383515"
cluster_name="test-dataproc"
region="us-central1"
dag_name="test-dataproc-creation"
connection_id= "dataengineer-id"

default_args = {
    'owner': 'airflow',
    'email': 'vachang9@gmail.com',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

cluster_config = {
    'cluster_name': cluster_name,
    'subnet_uri': 'projects/data-engineering-383515/regions/us-central1/subnetworks/default',
    'software_config': {
        'image_version' : 1.5,
        'properties': {
            'hive:hive.exec.dynamic.partition': 'true',
            'hive:hive.exec.dynamic.partition.mode': 'nonstrict',
            'spark:spark.dynamicAllocation.enabled': 'true',
            'spark:spark.dynamicAllocation.minExecutors': '2',
            'spark:spark.dynamicAllocation.maxExecutors': '10'
        },
        'optional_components': ['ANACONDA', 'JUPYTER', 'COMPONENT_GATEWAY'],

    },
    'worker_config': {
        'machine_type_uri': 'e2-custom-2-32768',
        'num_instances': 2,
        'disk_config': {'boot_disk_type': 'pd-standard',
                       'boot_disk_size_gb': 100 },
    },
    'master_config': {
        'machine_type_uri': 'e2-custom-2-32768',
        'disk_config': {'boot_disk_type': 'pd-standard', 'boot_disk_size_gb': 100},
    },
    'service_account': {
        'email': 'dataproc-admin@data-engineering-383515.iam.gserviceaccount.com',
        'scopes': ['https://www.googleapis.com/auth/cloud-platform']
    },

}

with DAG(dag_name, default_args=default_args, schedule_interval=None) as dag:
    create_cluster = DataprocClusterCreateOperator(
    task_id="create_cluster",
    project_id=project,
    cluster_config=cluster_config,
    region=region,
    connection_id=connection_id)
    create_cluster
                              
   
