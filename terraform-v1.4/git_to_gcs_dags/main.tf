data "google_composer_environment" "my_environment" {
    name =var.cloud_composer_env
    region="asia-east2"
}

resource "null_resource" "copy_file_to_bucket" {
  provisioner "local-exec" {
    command = <<-EOT
      #!/bin/bash
      set -euo pipefail

      # Activate the service account
      /home/ec2-user/google-cloud-sdk/bin/gcloud auth activate-service-account --key-file=${var.gcp_creds_path}/credentials.json

      # Set the active project
      /home/ec2-user/google-cloud-sdk/bin/gcloud config set project kedila-gcp-dev

      # Copy files to the Google Cloud Storage bucket
      /home/ec2-user/google-cloud-sdk/bin/gsutil cp dags/* ${data.google_composer_environment.my_environment.config[0].dag_gcs_prefix}
    EOT
  }
}






