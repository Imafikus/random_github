

resource "google_cloud_run_service" "service" {
  name     = "random-github-${var.stage}-${var.svc}"
  location = "europe-west1"

  template {
    spec {

      container_concurrency = var.no_concurrency ? 1 : null
      timeout_seconds = var.timeout_seconds

      containers {
        image = "eu.gcr.io/${var.project}/random-github-me-${var.svc}-${var.stage}:${var.label}"
        dynamic "env" {
          for_each = var.env

          content {
            name  = env.key
            value = env.value
          }
        }

        ports {
          container_port = 8080
        }

        resources {
          limits = {
            memory = var.memory
          }
        }
      }
    }
    
    metadata {
      annotations = {
        "autoscaling.knative.dev/maxScale"  = var.max_instances
      } 
    }
  }
  

  traffic {
    percent         = 100
    latest_revision = true
  }
}

data "google_iam_policy" "noauth" {
  count = var.no_auth ? 1 : 0

  binding {
    role = "roles/run.invoker"
    members = [
      "allUsers",
    ]
  }
}

resource "google_cloud_run_service_iam_policy" "noauth" {
  count = var.no_auth ? 1 : 0

  location = google_cloud_run_service.service.location
  project  = google_cloud_run_service.service.project
  service  = google_cloud_run_service.service.name

  policy_data = data.google_iam_policy.noauth[0].policy_data
}
