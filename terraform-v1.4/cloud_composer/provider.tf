
provider "google" {
    project = "kedila-gcp-dev"
    region = "us-central-1"
    credentials = "${file("${var.gcp_creds_path}/credentials.json")}"

}