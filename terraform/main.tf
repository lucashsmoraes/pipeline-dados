## Define a função lambda
#resource "aws_lambda_function" "create_glue_job" {
#  function_name = "create_glue_job"
#  role          = aws_iam_role.lambda_role.arn
#  handler       = "create_glue_job.lambda_handler"
#  runtime       = "python3.8"
#  s3_bucket = "tcc-script"
#  s3_key = "lambda/create_glue_job.zip"
#
#  # Define as variáveis de ambiente
#  environment {
#    variables = {
#      REGION = var.region
#      ROLE_GLUE = aws_iam_role.lambda_role.arn
#    }
#  }
#}
#
## Cria uma regra de permissão para invocar a função lambda
#resource "aws_lambda_permission" "allow_s3_bucket_to_invoke_lambda" {
#  statement_id  = "AllowExecutionFromS3"
#  action        = "lambda:InvokeFunction"
#  function_name = aws_lambda_function.create_glue_job.function_name
#  principal     = "s3.amazonaws.com"
#  source_arn    = "arn:aws:s3:::${var.bucket_name}"
#}

resource "aws_s3_object" "glue_script" {
  depends_on = [aws_s3_bucket.buckets]
  bucket = "${var.prefix}-${var.bucket_names[3]}-${var.account_id}"
  key    = "create_glue_job.py"
  source = "./files/job/glue-etl.py"
  force_destroy = true

  # Define as permissões de acesso ao objeto
  acl    = "private"
  # Define o tipo de conteúdo do objeto
  content_type = "text/x-python"
}

resource "aws_s3_object" "jars" {
  depends_on = [aws_s3_object.glue_script]
  bucket = "${var.prefix}-${var.bucket_names[3]}-${var.account_id}"
  key    = "jars/delta-core_2.12-1.0.0.jar"
  source = "./files/jars/delta-core_2.12-1.0.0.jar"
  force_destroy = true

  # Define as permissões de acesso ao objeto
  acl    = "private"
}

# Define a função IAM para a função lambda
resource "aws_iam_role" "glue_role" {
  name = "glue_job_role"

  assume_role_policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Action = "sts:AssumeRole"
        Effect = "Allow"
        Principal = {
          Service = "glue.amazonaws.com"
        }
      }
    ]
  })
}

# Anexa a política do Glue Job ao papel do IAM da função lambda
resource "aws_iam_role_policy_attachment" "glue_job_policy" {
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSGlueServiceRole"
  role       = aws_iam_role.glue_role.name
}