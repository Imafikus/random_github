locals {
  root_dir = abspath(".")
}

data "archive_file" "source" {
  type        = "zip"
  output_path = "./${var.function_name}-function.zip"
  
  dynamic "source" {
    for_each = var.files
    content {
      content  = file("${local.root_dir}/${source.value[0]}")
      filename = length(source.value) == 1 ? source.value[0] : source.value[1]
    }
  }
}

resource "google_storage_bucket_object" "zip" {
  # Append file MD5 to force bucket to be recreated
  name   = "source.zip#${data.archive_file.source.output_md5}"
  bucket = var.bucket_name
  source = data.archive_file.source.output_path
}

# Create Cloud Function
resource "google_cloudfunctions_function" "function" {
  name     = "rgp-${var.function_name}-${var.stage}"
  runtime = var.runtime

  available_memory_mb   = var.memory
  
  source_archive_bucket = var.bucket_name
  source_archive_object = google_storage_bucket_object.zip.name
  
  entry_point           = var.function_entry_point
  
  event_trigger {
    event_type = "google.pubsub.topic.publish"
    resource = var.trigger_id 
  }

  environment_variables = var.env
}
