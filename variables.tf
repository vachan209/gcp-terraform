variable "project_id" {
  type = string
}

variable "region" {
  type = string
}

variable "credentials_path" {
  type = string
}

variable "environment_name" {
  type = string
}


variable "machine_type" {
  type = string
}

variable "disk_size_gb" {
  type = number
}

variable "network_name" {
  type = string
  default = "default"
}

variable "subnetwork_name" {
  type = string
  default="default"
}

variable "image_version" {
  type = string
}

variable "python_version" {
  type = string
}

variable "database_machine_type" {
 type = string   
}

variable "web_server_machine_type" {
    type = string
}