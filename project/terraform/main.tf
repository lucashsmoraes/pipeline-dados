
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