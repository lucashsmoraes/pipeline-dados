resource "aws_glue_job" "glue_job" {
  for_each      = {for i, b in local.buckets_name: i => b}
  name              = "Job_bronze"
  role_arn          = aws_iam_role.glue_role.arn
  glue_version      = "3.0"
  worker_type       = "Standard"
  number_of_workers = 2
  timeout           = 5

  command {
    for_each      = {for i, b in local.buckets_name: i => b}
    script_location = concat("s3://", each.value[0], "/app/job_bronze/main.py")
    python_version  = "3"
  }

  default_arguments = {
    "--additional-python-modules" = "delta-spark==1.0.0"
  }

  depends_on = [aws_s3_bucket.this, aws_iam_role.glue_role]
}