output "postgres_instance_connection_name" {
  value = google_sql_database_instance.postgres_instance.connection_name
}

output "postgres_instance_ip_address" {
  value = google_sql_database_instance.postgres_instance.first_ip_address
}
output "kubeconfig" {
  value = google_container_cluster.primary.endpoint
}