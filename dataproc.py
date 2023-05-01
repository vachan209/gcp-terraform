from airflow import DAG
from airflow import models
from airflow.providers.google.cloud.operators.dataproc import DataprocCreateClusterOperator,DataprocDeleteClusterOperator
from airflow.utils.dates import days_ago
from datetime import datetime,timedelta
from airflow.operators.dummy_operator import DummyOperator

project="data-engineering-383515"
Cluster_name="test-dataproc"
Region="us-central1"
Dag_name="test-dataproc-creation"
Connection_id= "dataengineer-id"

default_args = {
    'owner': 'airflow',
    'email': 'vachang9@gmail.com',
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

cluster_config = {
    "gce_cluster_config": {
        "zone_uri": "us-central1-a",
        "subnetwork_uri": "projects/data-engineering-383515/regions/us-central1/subnetworks/default",
        "service_account": "data-engineer-admin@data-engineering-383515.iam.gserviceaccount.com",
        "service_account_scopes": ["https://www.googleapis.com/auth/cloud-platform"],
        "internal_ip_only": True
        },
    "software_config":{
         "image_version": "1.5",
         "optional_components": ['ANACONDA', 'JUPYTER'],
        },
    "master_config" : {
        "machine_type_uri": "n2-standard-2",
        "disk_config": {"boot_disk_type": "pd-standard", "boot_disk_size_gb": 100},

        },
    "worker_config": {
        "num_instances": 2,
        "machine_type_uri": "n2-standard-2",
        "disk_config": {"boot_disk_type": "pd-standard", "boot_disk_size_gb": 100},
        },        


}


with DAG(Dag_name, start_date=days_ago(1),catchup=False,default_args=default_args, schedule_interval=None) as dag:
    start = DummyOperator(
                 task_id='start',
                 dag=dag)

    create_cluster=DataprocCreateClusterOperator(
                  task_id='create_cluster',
                  project_id=project,
                  cluster_config=cluster_config,
                  region=Region,
                  cluster_name=Cluster_name,
                  gcp_conn_id=Connection_id

    )

    delete_cluster=DataprocDeleteClusterOperator(
                   task_id='delete_cluster',
                   project_id=project,
                   region=Region,
                   cluster_name=Cluster_name,
                   gcp_conn_id=Connection_id

    )
    start >> create_cluster >> delete_cluster          

    
    