resource "aws_glue_job" "glue_job" {
  depends_on = [aws_s3_bucket.buckets, aws_iam_role.glue_role]
  name              = "glue-tcc"
  role_arn          = aws_iam_role.glue_role.arn
  glue_version      = "3.0"
  worker_type       = "Standard"
  number_of_workers = 2
  timeout           = 5

  command {
    script_location = "s3://${local.glue_bucket}/jobs/main.py"
    python_version  = "3"
  }

  default_arguments = {
    "--additional-python-modules" = "delta-spark==1.0.0"
  }
}