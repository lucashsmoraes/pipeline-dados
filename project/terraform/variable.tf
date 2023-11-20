#variable "region" {
#  description = "aws region"
#  type        = string
#}
#
#variable "account_id" {
#  description = "aws account id"
#
#}
#
#variable "prefix" {
#  description = "objects prefix"
#  type        = string
#}

variable "glue_job_role_arn" {
  description = "The ARN of the IAM role associated with this job."
  type        = string
}

variable "script_location" {
  description = "The S3 path to a script that executes a job."
  type        = string
}

variable "kms_key_description" {
  description = "The description of the key as viewed in AWS console."
  type        = string
}

variable "kms_key_deletion_window_in_days" {
  description = "Duration in days after which the key is deleted after destruction of the resource, must be between 7 and 30 days."
  type        = number
  default     = 7
}

variable "kms_key_enable_key_rotation" {
  description = "Specifies whether key rotation is enabled."
  type        = bool
  default     = true
}

#variable "buckets_names" {
#  description = "s3 buckets names"
#}
