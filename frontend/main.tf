locals {
    project = "random-github-project"
    stage = "production"
}

provider "google" {
    project = "${local.project}"
    region  = "europe-west1"
}

terraform {
  backend "gcs" {
    bucket = "tf-state-random-github-project-production"
  }
}

module "frontend" {
  source = "./terraform/modules/cloudrun"

  project = local.project
  stage   = local.stage
  svc     = "frontend"
  label   = var.commit_sha

  no_auth = true
  max_instances = 2
}
