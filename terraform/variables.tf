variable "project_id" {
  description = "The GCP project ID"
  type        = string
}

variable "region" {
  description = "The GCP region"
  default     = "us-central1"
}

variable "db_name" {
  description = "The name of the PostgreSQL database"
  default     = "mydb"
}

variable "db_user" {
  description = "The PostgreSQL user name"
  default     = "user"
}

variable "db_password" {
  description = "The PostgreSQL user password"
  default     = "password"
}