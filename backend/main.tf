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

resource "google_storage_bucket" "cf_all_functions" {
    name = "cf-all-functions-${local.stage}"
    location = "EU"
    uniform_bucket_level_access = true
}

resource "google_pubsub_topic" "data_extractor_topic" {
    name = "random-github-project-data-extractor-${local.stage}"
}


resource "google_cloud_scheduler_job" "data_extractor_trigger" {
    name        = "data-extractor-trigger"
    description = "Triggers the data_extractor every day at 00:00"
    schedule    = "0 0 * * *"
    time_zone = "Europe/London"

    pubsub_target {
        topic_name = google_pubsub_topic.data_extractor_topic.id
        data       = base64encode("{}")
    }
}

module "data_extractor" {
    source = "./terraform/modules/cloud_function"

    project = local.project
    stage   = local.stage
    
    bucket_name = google_storage_bucket.cf_all_functions.name
    function_name = "data_extractor"
    function_entry_point = "main"

    trigger_id = google_pubsub_topic.data_extractor_topic.id
    memory = 128 
    runtime = "python39"
    #FIXME
    env = {
        GITHUB_USERNAME = var.github_username
        GITHUB_ACCESS_TOKEN = var.github_access_token
        
        MAX_COMMENT_NUMBER_PER_REPO = var.max_comment_number_per_repo 
        MAX_COMMENT_NUMBER_GLOBAL = var.max_comment_number_global
        ENV = local.stage
    }
    
    files = [
        ["comment_extractor.py", "main.py"],
        ["models.py", "models.py"],
        ["github_api.py", "github_api.py"],
        ["data_extractor.py", "data_extractor.py"],
        ["datastore_db.py", "datastore_db.py"],
        ["requirements.txt", "requirements.txt"],
        ["trending.py", "trending.py"],
    ]
}

module "server" {
  source = "./terraform/modules/cloudrun"

  project = local.project
  stage   = local.stage
  svc     = "server"
  label   = var.commit_sha

  no_auth = true
  max_instances = 2
}
