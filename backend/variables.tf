variable "github_username" {
    type        = string
    description = "Username used when consuming GitHub API"
    sensitive   = true
}
variable "github_access_token" {
    type        = string
    description = "Token used when consuming GitHub API"
    sensitive   = true
}
variable "max_comment_number" {
    type        = string
    description = "Max number of comments extracted from a single repo"
    default = "20"
}
