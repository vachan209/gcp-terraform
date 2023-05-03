FROM google/cloud-sdk:latest

ARG KEYFILE_PATH

WORKDIR /app

copy scripts/git_to_gcs.sh /app

copy ${KEYFILE_PATH}/credentials.json /app/credentials.json

copy dags/* /app/dags/

RUN chmod +x /app/credentials.json

RUN chmod +x /app/git_to_gcs.sh

ENTRYPOINT ["/app/git_to_gcs.sh"]

