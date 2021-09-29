variable "project" {
  type        = string
  description = "GCP project name"
}

variable "stage" {
  type        = string
  description = "Stage name to deploy to"
}

variable "svc" {
  type        = string
  description = "Service name to deploy"
}

variable "label" {
  type        = string
  description = "(Optional) Label to use for containers. Defaults to 'latest'"
  default     = "latest"
}

variable "env" {
  type        = map(string)
  description = "(Optional) Environment variables to put into the service"
  default     = {}
}

variable "no_concurrency" {
  type        = bool
  description = "(Optional) If set to true, requires the container to not have concurrent requests"
  default     = false
}

variable "no_auth" {
  type        = bool
  description = "(Optional) If set to true, the container will not require authentication to invoke."
  default     = false
}

variable "memory" {
  type        = string
  description = "(Optional) Memory allocated for container."
  default     = null
}

variable "max_instances" {
  type        = string
  description = "(Optional) Max instances of the container that can be run at the same time."
  default     = null
}

variable "timeout_seconds" {
  type        = string
  description = "(Optional) TimeoutSeconds holds the max duration the instance is allowed for responding to a request."
  default     = null
}
