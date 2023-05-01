
data "google_service_account" "object_viewer" {
  account_id = "terraform-dev@kedila-gcp-dev.iam.gserviceaccount.com"
}

resource "google_composer_environment" "test" {
  name   = var.environment_name
  region = var.region
 config{
   node_config {
    zone         = "asia-east2-a"
    machine_type = var.machine_type
    network      = var.network_name
    subnetwork   =  var.subnetwork_name
    service_account = "terraform-dev@kedila-gcp-dev.iam.gserviceaccount.com"
    oauth_scopes = ["https://www.googleapis.com/auth/cloud-platform"]
  }
  software_config {
    image_version = var.image_version
    python_version = var.python_version

    }
    database_config {
      machine_type = var.database_machine_type
    }
    web_server_config {
      machine_type = var.web_server_machine_type
    }

  }
 
  
 }

 output "dags_bucket" {
  value = google_composer_environment.test.config[0].dag_gcs_prefix
 }
  
