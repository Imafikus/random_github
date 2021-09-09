provider "google" {
    credentials = file("key.json")
    project = "random-github-project"
    region  = "europe-west1"
}

resource "google_pubsub_topic" "data_extractor_topic" {
    name = "random-github-project-data-extractor"
}