variable "project" {
  type        = string
  description = "GCP project name"
}

variable "bucket_name" {
  type        = string
  description = "Bucket where CF code will be stored"
}

variable "function_name" {
  type        = string
  description = "Name of the CF"
}

variable "stage" {
  type        = string
  description = "Stage name to deploy to"
}

variable "function_entry_point" {
  type        = string
  description = "Entry point for the function"
}

variable "trigger_id" {
  type        = string
  description = "ID of the trigger which will invoke the function"
}

variable "env" {
  type        = map(string)
  description = "(Optional) Environment variables to put into the service"
  default     = {}
}

variable "memory" {
  type        = number
  description = "Amount of memory for the CF"
}

variable "runtime" {
  type        = string
  description = "Runtime env for the function"
}

variable "files" {
  type        = list(list(string))
  description = <<DOC
List of all files in the cloud_function (with their local and cloud paths).

The format is either `[local_path, function_path]` in which case a file from
`local_path` will be renamed to `function_path` in the function environment, or
`[path]`, which is equivalent to `[path, path]`."
DOC
}
