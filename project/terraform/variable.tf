variable "region" {
  description = "aws region"
}

variable "account_id" {
  description = "aws account id"
}

variable "prefix" {
  description = "objects prefix"
}

variable "bucket_names" {
  description = "s3 bucket names"
  type        = set(string)
}

variable "glue_job_role_arn" {
  description = "The ARN of the IAM role associated with this job."
}

variable "script_location" {
  description = "The S3 path to a script that executes a job."
}

variable "kms_key_alias" {
  description = "The alias for the KMS key as viewed in AWS console. It will be automatically prefixed with `alias/`"
  type        = string
}

variable "kms_key_description" {
  description = "The description of the key as viewed in AWS console."
  type        = string
}

variable "kms_key_deletion_window_in_days" {
  description = "Duration in days after which the key is deleted after destruction of the resource, must be between 7 and 30 days."
  type        = number
}

variable "kms_key_enable_key_rotation" {
  description = "Specifies whether key rotation is enabled."
  type        = bool
  default     = true
}

variable "buckets_names" {
  description = "s3 buckets names"
  type        = set(string)
}
