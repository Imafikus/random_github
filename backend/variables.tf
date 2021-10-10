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
variable "max_comment_number_per_repo" {
    type        = string
    description = "Max number of comments extracted from a single repo"
    default = "10"
}

variable "max_comment_number_global" {
    type        = string
    description = "Max number of comments extracted globally"
    default = "100"
}

variable "commit_sha" {
    type        = string
    description = "Commit sha for the currently running job"
}
