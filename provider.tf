variable "path" {
    default = "C://terraform-gcp//credentials"
}

provider "google" {
    project = "kedila-gcp-dev"
    region = "us-central-1"
    credentials = "${file("${var.path}/credentials.json")}"

}