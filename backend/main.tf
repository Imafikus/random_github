locals {
    project = "random-github-project"
    stage = "production"
}

provider "google" {
    credentials = file("key.json")
    project = "${local.project}"
    region  = "europe-west1"
}

resource "google_storage_bucket" "cf_all_functions" {
    name = "cf-all-functions-${local.stage}"
    location = "EU"
    uniform_bucket_level_access = true
}

resource "google_pubsub_topic" "data_extractor_topic" {
    name = "random-github-project-data-extractor-${local.stage}"
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