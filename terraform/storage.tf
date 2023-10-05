resource "aws_s3_bucket" "buckets" {
  count  = length(var.bucket_names)
  bucket = "${var.prefix}-${var.bucket_names[count.index]}-${var.account_id}"

  force_destroy = true
  tags = local.common_tags
}

resource "aws_s3_object" "glue_script" {
  depends_on = [aws_s3_bucket.buckets]
  bucket = "${var.prefix}-${var.bucket_names[3]}-${var.account_id}"
  key    = "jobs/main.py"
  source = "./app/job/main.py"
  force_destroy = true

  # Define o tipo de conteúdo do objeto
  content_type = "text/x-python"
}

resource "aws_s3_object" "jars" {
  depends_on = [aws_s3_object.glue_script]
  bucket = "${var.prefix}-${var.bucket_names[3]}-${var.account_id}"
  key    = "jars/delta-core_2.12-1.0.0.jar"
  source = "./app/jars/delta-core_2.12-1.0.0.jar"
  force_destroy = true
}

resource "aws_s3_bucket_server_side_encryption_configuration" "bucket_sse" {
  count  = length(var.bucket_names)
  bucket = "${var.prefix}-${var.bucket_names[count.index]}-${var.account_id}"


  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }

   depends_on = [
    aws_s3_bucket.buckets
  ]

}

#resource "aws_s3_bucket_acl" "bucket_acl" {
#  count  = length(var.bucket_names)
#  bucket = "${var.prefix}-${var.bucket_names[count.index]}-${var.account_id}"
#  acl    = "private"
#
#   depends_on = [
#    aws_s3_bucket.buckets
#  ]
#
#}

# Rules for public access block
resource "aws_s3_bucket_public_access_block" "public_access_block" {
  count  = length(var.bucket_names)
  bucket = "${var.prefix}-${var.bucket_names[count.index]}-${var.account_id}"

  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true

  depends_on = [
    aws_s3_bucket.buckets
  ]

}