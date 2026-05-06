output "nginx_service_name" {
  value = kubernetes_service_v1.nginx.metadata[0].name
}