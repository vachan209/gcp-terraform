variable "gcp_creds_path" {
  type = string
}

variable "cloud_composer_env"{
    type=string
    default="airflow-dataproc"

}