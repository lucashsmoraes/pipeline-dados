variable "region" {
  description = "aws region"
  default     = "us-west-1"
}

variable "account_id" {
  default = 469691162657
}

variable "prefix" {
  description = "objects prefix"
  default     = "tcc"
}

# Prefix configuration and project common tags
locals {
  glue_bucket = "${var.prefix}-${var.bucket_names[3]}-${var.account_id}"
  prefix      = var.prefix
  common_tags = {
    Project = "pipeline-dados"
  }
}

variable "bucket_names" {
  description = "s3 bucket names"
  type        = list(string)
  default = [
    "bronze",
    "silver",
    "gold",
    "scripts"
  ]
}

variable "glue_job_role_arn" {
  description = "The ARN of the IAM role associated with this job."
  default     = null
}