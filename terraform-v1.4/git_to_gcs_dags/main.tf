data "google_composer_environment" "my_environment" {
    name =var.cloud_composer_env
    region="asia-east2"
}

resource "null_resource" "copy_file_to_bucket"{
    provisioner "local-exec" {
    command = "gsutil cp dags/* ${google_composer_environment.my_environment.config[0].dag_gcs_prefix}"    
    }
}