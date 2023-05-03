#!/bin/bash

#activdate google cloud service account
gcloud auth activate-service-account --key-file=/app/credentials.json
gcloud config set project kedila-gcp-dev

#fetch clud composer bucket prefix metadata
DAG_BUCKET_NAME=$( gcloud composer environments describe airflow-dataproc --location=asia-east2 --format='get(config.dagGcsPrefix)')

gsutil cp app/dags/* $DAG_BUCKET_NAME
