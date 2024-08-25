provider "google" {
  credentials = file("${path.module}/gcp-key.json")
  project = var.project_id
  region  =  var.region
}

resource "google_sql_database_instance" "postgres_instance" {
  name             = "postgres-instance"
  database_version = "POSTGRES_13"
  region           =  var.region

  settings {
    tier = "db-f1-micro"  # סוג ה-Instance
    # הגדרת כתובת IP ציבורית
    ip_configuration {
      ipv4_enabled = true
      authorized_networks {
        name  = "allow-all"
        value = "0.0.0.0/0"  # ניתן להחליף בכתובת IP ספציפית לשיפור האבטחה
      }
    }
  }
}

resource "google_sql_database" "default" {
  name     = var.db_name
  instance = google_sql_database_instance.postgres_instance.name
}

resource "google_sql_user" "postgres_user" {
  name     = var.db_user
  password = var.db_password
  instance = google_sql_database_instance.postgres_instance.name
}
resource "google_compute_firewall" "allow_postgres" {
  name    = "allow-postgres"
  network = "default"

  allow {
    protocol = "tcp"
    ports    = ["5432"]
  }

  source_ranges = ["0.0.0.0/0"]  # ניתן להחליף ב-IP ספציפי לשיפור האבטחה
}

resource "google_container_cluster" "primary" {
  name               = "fastapi-cluster"
  location           = "us-central1-c"
  initial_node_count = 1
  deletion_protection = false

  

  node_config {
    machine_type = var.machine_type
  }
}

