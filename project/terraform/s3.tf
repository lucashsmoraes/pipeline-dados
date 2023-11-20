resource "aws_s3_bucket" "this" {
  for_each      = {for i, b in local.buckets_name: i => b}
  bucket        = each.value
  force_destroy = true
  tags          = local.common_tags
}

resource "aws_s3_bucket_object" "upload" {
  for_each      = {for i, b in local.buckets_name: i => b}
  bucket        = each.value[0]
  key = "app/"
  source        = "../app"
  force_destroy = true
  content_type  = "application/x-directory"
}

resource "aws_s3_bucket_server_side_encryption_configuration" "bucket_sse" {
  for_each = {for i, b in local.buckets_name: i => b}
  bucket   = each.value
}

resource "aws_s3_bucket_acl" "bucket_acl" {
  for_each = {for i, b in local.buckets_name: i => b}
  bucket   = each.value
  acl      = "private"
}

# Rules for public access block
resource "aws_s3_bucket_public_access_block" "public_access_block" {
  for_each                = {for i, b in local.buckets_name: i => b}
  bucket                  = each.value
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_kms_key" "this" {
  deletion_window_in_days = var.kms_key_deletion_window_in_days
  enable_key_rotation     = var.kms_key_enable_key_rotation

  tags = local.common_tags
}

resource "aws_kms_alias" "this" {
  name          = local.kms_key_alias
  target_key_id = aws_kms_key.this.key_id
}

resource "aws_s3_bucket_policy" "bucket_policy" {
  for_each = {for i, b in local.buckets_name: i => b}
  bucket   = each.value
  policy   = data.aws_iam_policy_document.bucket_policy.json
}

data "aws_iam_policy_document" "bucket_policy" {
  statement {
    sid       = "AllowSSLRequestsOnly"
    actions   = ["s3:*"]
    effect    = "Deny"
    resources = [
      "arn:aws:s3:::${local.prefix}/",
      "arn:aws:s3:::${local.prefix}/*"
    ]
    condition {
      test     = "Bool"
      variable = "aws:SecureTransport"
      values   = ["false"]
    }
    principals {
      type        = "*"
      identifiers = ["*"]
    }
  }
  statement {
    sid     = "AllowBucketLevelOperations"
    actions = [
      "s3:GetObject",
      "s3:GetObjectAcl",
      "s3:ListBucket",
      "s3:PutObject",
      "S3:GetBucketAcl",
      "s3:PutObjectAcl",
      "s3:DeleteObject",
    ]
    effect    = "Allow"
    resources = [
      "arn:aws:s3:::${local.prefix}*/",
      "arn:aws:s3:::${local.prefix}*/*"
    ]
    principals {
      type        = "AWS"
      identifiers = ["*"]
    }
  }
}