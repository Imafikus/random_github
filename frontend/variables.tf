variable "github_username" {
    type        = string
    description = "Username used when consuming GitHub API"
    default = "imafikus"
}
variable "github_access_token" {
    type        = string
    description = "Token used when consuming GitHub API"
    sensitive   = true
}
variable "commit_sha" {
    type        = string
    description = "Commit sha for the currently running job"
}
